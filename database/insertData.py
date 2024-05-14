from loguru import logger
import sys
sys.path.append('/home/thiago/Projetos/dataSiege/Project-Data-Siege')
from database.databaseConnection import connection

class insertData:
    connector = connection.getInstance()
    cursor = connector.database_cursor()

    def insert_data_ban_operator (self, json={}):
        self.id_bans = {
            json['sumary']['team_info']['team0']['name']:{},
            json['sumary']['team_info']['team1']['name']:{}
        }
        sql_code_to_retrieve_last_id = 'SELECT TOP(1) id_ban from ban_operator ORDER BY id_ban DESC'

        for qtd_matches in range(len(json.keys()) - 1):
            if json[f'match{qtd_matches}']['qtd_rounds'] != 0:
                for time in json['sumary']['team_info']:
                    team_name = json['sumary']['team_info'][time]['name']

                    sql_code = f'''
                    INSERT INTO ban_operator (
                    id_team,
                    ban1,
                    ban2,
                    date_match)
                    VALUES('''

                    sql_code += f'''
                        (SELECT id_team FROM team WHERE name_team = '{json['sumary']['team_info'][time]['name']}'),
                        (SELECT id_operator FROM operator WHERE name_operator = '{json[f'match{qtd_matches}'][team_name]['team_info']['banAtk']}'),
                        (SELECT id_operator FROM operator WHERE name_operator = '{json[f'match{qtd_matches}'][team_name]['team_info']['banDef']}'),
                        '{json['sumary']['date']}'
                    )
                    '''
                    logger.info(sql_code)
                    self.cursor.execute(sql_code)
                    self.cursor.commit()

                    self.cursor.execute(sql_code_to_retrieve_last_id)
                    self.id_bans[json['sumary']['team_info'][time]['name']].update({
                            f'ban{qtd_matches}': self.cursor.fetchone()[0]
                    })

    def insert_data_match(self, json={}):
        sql_code_to_retrieve_last_id = 'SELECT TOP(1) id_match from matchs ORDER BY id_match DESC'

        sql_code = f'''
            INSERT INTO matchs (
                id_region,
                date_match,
                md{json['sumary']['championship']['matchFormat']},
                id_map1,
                id_map2,
                id_map3,
                '''
        qtd_total_bans = len(self.id_bans[json['sumary']['team_info']['team0']['name']])*2
        for id_ban in range(1, (qtd_total_bans + 1)):
            sql_code += f'''
                id_ban{id_ban},
                ''' if id_ban<=2 else f'''
                id_ban{id_ban}_md3,
                '''

        sql_code += f'''
                id_team1,
                id_team2,
                qtd_rounds)
            VALUES (
                (SELECT id_region FROM region WHERE name_region = '{json['sumary']['championship']['region']}'),
                '{json['sumary']['date']}',
                1,
            '''

        for qtd_matches in range(len(json.keys()) - 1):
            sql_code+= f'''
                (SELECT id_map FROM maps WHERE name_map = '{json[f'match{qtd_matches}']['map']}'),
            '''

        for team in json['sumary']['team_info'].keys():
            for ban_info in self.id_bans[json['sumary']['team_info'][team]['name']]:
                sql_code += f'''
                {self.id_bans[json['sumary']['team_info'][team]['name']][ban_info]}, 
                '''

        for time in json['sumary']['team_info'].keys():
            sql_code+= f'''
                (SELECT id_team FROM team WHERE name_team = '{json['sumary']['team_info'][time]['name']}'),
            '''

        sql_code += f"{json['sumary']['qtd_rounds']}"
        sql_code += ')'
        logger.info(sql_code)

        self.cursor.execute(sql_code)
        self.cursor.commit()
        self.cursor.execute(sql_code_to_retrieve_last_id)
        return self.cursor.fetchone()[0]

    def insert_data_team_match(self, json={}, id_last_match=0):
        for match in range(len(json.keys())-1):
            qtd_rounds = json[f'match{match}']['qtd_rounds']
            if qtd_rounds > 1:
                for key in json[f'sumary']['team_info'].keys():
                    name_team = json[f'sumary']['team_info'][key]['name']
                    total_won = json[f'match{match}'][name_team]['team_info']['score']
                    total_lost = qtd_rounds - total_won
                    sql_code = f"""
                    INSERT INTO team_match (
                        id_team,
                        id_match,
                        victory,
                        w_rounds,
                        l_rounds,
                        id_map)
                        VALUES(
                            (SELECT id_team FROM team WHERE name_team = '{name_team}'),
                            {id_last_match},
                            {json['sumary']['team_info'][key]['winner']},
                            {total_won},
                            {total_lost},
                            (SELECT id_map FROM maps WHERE name_map = '{json[f'match{match}']['map']}')
                        )"""
                    logger.info(sql_code)
                    self.cursor.execute(sql_code)
                    self.cursor.commit()

    def insert_data_player_match(self, json={}, id_last_match=0):
        for match in range(len(json.keys())-1):
            qtd_rounds = json[f'match{match}']['qtd_rounds']
            if qtd_rounds > 1:
                for key in json[f'sumary']['team_info'].keys():
                    name_team = json[f'sumary']['team_info'][key]['name']
                    for player, stats in json[f'match{match}'][name_team]['player_info'].items():
                        sql_code = f'''
                            INSERT INTO player_match (
                                id_player,
                                id_match,
                                id_team,
                                kills,
                                deaths,
                                plants,
                                disarms,
                                OnevX,
                                HS,
                                open_kills,
                                open_deaths,
                                id_map,
                                clutchs)
                            VALUES(
                                (SELECT id_player FROM player WHERE name_player='{player}'),
                                {id_last_match},
                                (SELECT id_team FROM team WHERE name_team = '{name_team}'),
                                {stats['kills']},
                                {stats['deaths']},
                                {stats['plants']},
                                {stats['disarms']},
                                {stats['oneVX']},
                                {stats['HS']},
                                {stats['open_kill']},
                                {stats['open_deaths']},
                                (SELECT id_map FROM maps WHERE name_map = '{json[f'match{match}']['map']}'),
                                {stats['clutch']}
                            )'''
                        logger.info(sql_code)
                        self.cursor.execute(sql_code)
                        self.cursor.commit()