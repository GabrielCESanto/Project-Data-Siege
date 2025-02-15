from loguru import logger
import sys
sys.path.append('/home/thiago/Projetos/dataSiege/Project-Data-Siege')
from database.databaseConnection import connection

class insertData:
    connector = connection.getInstance()
    cursor = connector.database_cursor()

    def insert_data_ban_operator (self, json={}, tentativas= 0):
        try:
            self.id_bans = {
                json['sumary']['team_info']['team0']['name']:{},
                json['sumary']['team_info']['team1']['name']:{}
            }
            sql_code_to_retrieve_last_id = 'SELECT TOP(1) id_ban from ban_operator ORDER BY id_ban DESC'
            for qtd_matches in range(len(json.keys()) - 1):
                if 'qtd_rounds' in json[f'match{qtd_matches}']:
                    if json[f'match{qtd_matches}']['qtd_rounds'] != 0:
                        for time in json['sumary']['team_info']:
                            team_name = json['sumary']['team_info'][time]['name']

                            sql_code = f'''
                            INSERT INTO ban_operator (
                            id_team,
                            ban1,
                            ban2,
                            date_match,
                            id_url)
                            VALUES('''

                            sql_code += f'''
                                (SELECT id_team FROM team WHERE name_team = '{json['sumary']['team_info'][time]['name']}'),
                                (SELECT id_operator FROM operator WHERE name_operator = '{json[f'match{qtd_matches}'][team_name]['team_info']['banAtk']}'),
                                (SELECT id_operator FROM operator WHERE name_operator = '{json[f'match{qtd_matches}'][team_name]['team_info']['banDef']}'),
                                '{json['sumary']['date']}',
                                {json['sumary']['url'][-4:]}
                            )
                            '''
                            logger.info(sql_code)
                            self.cursor.execute(sql_code)
                            self.cursor.commit()

                            self.cursor.execute(sql_code_to_retrieve_last_id)
                            self.id_bans[json['sumary']['team_info'][time]['name']].update({
                                    f'ban{qtd_matches}': self.cursor.fetchone()[0]
                            })
        except Exception as e:
            logger.debug("ERROR")
            logger.debug(e)
            if tentativas < 1 :
                tentativas += 1
                self.cursor.close()
                self.connector.getInstance()
                self.insert_data_ban_operator(json, tentativas)

    def insert_data_match_md_3(self, json={}, tentativas=0):
        try:
            sql_code_to_retrieve_last_id = 'SELECT TOP(1) id_match from matchs ORDER BY id_match DESC'

            sql_code = f'''
                INSERT INTO matchs (
                    id_championship,
                    date_match,
                    md{json['sumary']['championship']['matchFormat']},
                    id_map1,
                    id_map2,
                    id_map3,
                    '''
            qtd_total_bans = len(self.id_bans[json['sumary']['team_info']['team0']['name']]) * 2

            for id_ban in range(1, (qtd_total_bans + 1)):
                sql_code += f'''
                    id_ban{id_ban},
                    ''' if id_ban<=2 else f'''
                    id_ban{id_ban}_md3,
                    '''

            sql_code += f'''
                    id_team1,
                    id_team2,
                    qtd_rounds,
                    url_match)
                VALUES (
                    (SELECT id_championship FROM championships where name_championship = '{json['sumary']['championship']['competition']}'),
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

            sql_code += f"{json['sumary']['qtd_rounds']},"
            sql_code += f"'{json['sumary']['url']}'"
            sql_code += ')'
            logger.info(sql_code)

            self.cursor.execute(sql_code)
            self.cursor.commit()
            self.cursor.execute(sql_code_to_retrieve_last_id)
            return self.cursor.fetchone()[0]
        except Exception as e:
            logger.debug("ERROR")
            logger.debug(e)
            if tentativas < 1 :
                tentativas += 1
                self.cursor.close()
                self.connector.getInstance()
                self.insert_data_match_md_3(json, tentativas)

    def insert_data_match_md_5(self, json={}, tentativas=0):
        try:
            sql_code_to_retrieve_last_id = 'SELECT TOP(1) id_match from matchs ORDER BY id_match DESC'

            sql_code = f'''
                INSERT INTO matchs (
                    id_championship,
                    date_match,
                    md{json['sumary']['championship']['matchFormat']},
                    id_map1,
                    id_map2,
                    id_map3,
                    id_map4,
                    id_map5,
                    '''
            qtd_total_bans = len(self.id_bans[json['sumary']['team_info']['team0']['name']]) * 2

            for id_ban in range(1, (qtd_total_bans + 1)):
                if id_ban <=2 :
                    sql_code += f'''
                        id_ban{id_ban},
                    '''
                if id_ban >2 and id_ban<=6:
                    sql_code+= f'''
                        id_ban{id_ban}_md3,
                    '''
                if id_ban > 6:
                    sql_code += f'''
                        id_ban{id_ban}_md5,
                    '''

            sql_code += f'''
                    id_team1,
                    id_team2,
                    qtd_rounds,
                    url_match)
                VALUES (
                    (SELECT id_championship FROM championships where name_championship = '{json['sumary']['championship']['competition']}'),
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

            sql_code += f"{json['sumary']['qtd_rounds']},"
            sql_code += f"'{json['sumary']['url']}'"
            sql_code += ')'
            logger.info(sql_code)

            self.cursor.execute(sql_code)
            self.cursor.commit()
            self.cursor.execute(sql_code_to_retrieve_last_id)
            return self.cursor.fetchone()[0]
        except Exception as e:
            logger.debug("ERROR")
            logger.debug(e)
            if tentativas < 1 :
                tentativas += 1
                self.cursor.close()
                self.connector.getInstance()
                self.insert_data_match_md_5(json, tentativas)

    def insert_data_match_md_1(self, json={}, tentativas = 0):
        try:
            sql_code_to_retrieve_last_id = 'SELECT TOP(1) id_match from matchs ORDER BY id_match DESC'

            sql_code = f'''
                INSERT INTO matchs (
                    id_championship,
                    date_match,
                    md{json['sumary']['championship']['matchFormat']},
                    id_map1,
                    id_ban1,
                    id_ban2,
                    '''

            sql_code += f'''
                    id_team1,
                    id_team2,
                    qtd_rounds,
                    url_match
                    )
                VALUES (
                    (SELECT id_championship FROM championships where name_championship = '{json['sumary']['championship']['competition']}'),
                    '{json['sumary']['date']}',
                    1,
                    (SELECT id_map FROM maps WHERE name_map = '{json[f'match0']['map']}'),
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

            sql_code += f"{json['sumary']['qtd_rounds']},"
            sql_code += f"'{json['sumary']['url']}'"
            sql_code += ')'
            logger.info(sql_code)

            self.cursor.execute(sql_code)
            self.cursor.commit()
            self.cursor.execute(sql_code_to_retrieve_last_id)
            return self.cursor.fetchone()[0]

        except Exception as e:
            logger.debug("ERROR")
            logger.debug(e)
            if tentativas < 1 :
                tentativas += 1
                self.cursor.close()
                self.connector.getInstance()
                self.insert_data_match_md_1(json, tentativas)

    def insert_data_team_match(self, json={}, id_last_match=0, tentativas=0):
        try:
            for match in range(len(json.keys())-1):
                if 'qtd_rounds' in json[f'match{match}']:
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
        except Exception as e:
            logger.debug("ERROR")
            logger.debug(e)
            if tentativas < 1 :
                tentativas += 1
                self.cursor.close()
                self.connector.getInstance()
                self.insert_data_team_match(json, tentativas)

    def insert_data_player_match(self, json={}, id_last_match=0, tentativas=0):
        try:
            for match in range(len(json.keys())-1):
                if 'qtd_rounds' in json[f'match{match}']:
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
                                        clutchs,
                                        kost,
                                        eps)
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
                                        {stats['clutch']},
                                        '{stats['kost']}',
                                        {stats['eps']}
                                    )'''
                                logger.info(sql_code)
                                self.cursor.execute(sql_code)
                                self.cursor.commit()
        except Exception as e:
            logger.debug("ERROR")
            logger.debug(e)
            if tentativas < 1 :
                tentativas += 1
                self.cursor.close()
                self.connector.getInstance()
                self.insert_data_player_match(json, tentativas)