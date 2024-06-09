from loguru import logger
from database.insertData import insertData
from main.app_base import app_base

class app(app_base):
    def get_matches_info(self, matches_info={}, match_url = ''):
        try:
            self.qtd_rounds = 0
            insersor = insertData()
            results = {
                'sumary' : {},
                'match0' : {},
                'match1' : {},
                'match2' : {}
            }
            results.update(self.set_sumary_info(results, matches_info))
            logger.critical(match_url)
            results.update(self.set_all_info_each_map(results, matches_info))
            results['sumary']['qtd_rounds'] = self.qtd_rounds
            results['sumary']['url'] = match_url

            insersor.insert_data_ban_operator(results)

            if results['sumary']['championship']['matchFormat'] == 1:
                id_last_match = insersor.insert_data_match_md_1(results)
            if results['sumary']['championship']['matchFormat'] == 3:
                id_last_match = insersor.insert_data_match_md_3(results)
            if results['sumary']['championship']['matchFormat'] == 5:
                id_last_match = insersor.insert_data_match_md_5(results)

            insersor.insert_data_team_match(results, id_last_match)
            insersor.insert_data_player_match(results, id_last_match)
            self.create_matches_cache(match_url)

        except Exception as e:
            logger.error('ERROR')
            logger.error(e)

    def set_sumary_info(self, results={}, match={}):
        results['sumary']['championship'] = self.get_championship_info(match)
        results['sumary']['team_info'] =  self.get_team_info(match)
        results['sumary']['date'] = match['match']['date']
        results['sumary']['qtd_rounds'] = 0
        return results

    def get_team_info(self, match = {}):
        sumary = {}

        for contador in range(len(match['teams'])):
            sumary.update({
                f'team{contador}':{
                    'name' : match['teams'][contador]['name'].strip(),
                    'score_in_match' : match['match']['teams'][contador]['score']
                }
            })
        team0_score = sumary[f'team0']['score_in_match']
        team1_score = sumary[f'team1']['score_in_match']

        if team0_score> team1_score:
            sumary[f'team0']['winner'] = 1
            sumary[f'team1']['winner'] = 0
            return sumary

        sumary[f'team0']['winner'] = 0
        sumary[f'team1']['winner'] = 1
        return sumary

    def get_championship_info(self, match = {}):
        return {  
            'name' : match['championship']['name'].strip(),
            'competition' : match['competition']['name'].strip(),
            'matchFormat' : match['match']['matchFormatNumberOfGames'],
            'region' : match['championship']['name'].strip().split(' ')[-1]
        }

    def set_all_info_each_map(self, results={}, match={}):
        for game in range(results['sumary']['championship']['matchFormat']):
            match_happened = len(match['match']['games'][game]['rounds']) > 1

            if f'match{game}' not in results:
                results.update({
                    f'match{game}':{}
                })

            results[f'match{game}'].update({
                'map' : match['match']['games'][game]['map']['name'],
                'qtd_rounds':len(match['match']['games'][game]['rounds']) if match_happened else 0
            })

            self.qtd_rounds += len(match['match']['games'][game]['rounds']) if match_happened else 0

            if match_happened:
                for info_match in range(len(match['match']['games'][game]['teams'])):

                    results[f'match{game}'].update({
                        results['sumary']['team_info'][f'team{info_match}']['name']:{
                            'team_info':{
                                'score' : match['match']['games'][game]['teams'][info_match]['score'],
                                'banAtk' : self.translator.remove_acentos(
                                    match['match']['games'][game]['teams'][info_match]['operatorBans'][0]['name'].lower()),
                                'banDef' : self.translator.remove_acentos(
                                    match['match']['games'][game]['teams'][info_match]['operatorBans'][1]['name'].lower())
                            },
                            'player_info':{}
                        }
                    })

                    results = self.get_players_infos(results, match, game, info_match)
                results = self.set_team_winner_map(results, match, game)

        return results

    def get_players_infos(self, results={}, match= {}, game=0, info_match=0):
        for player_info in range(len(match['match']['games'][game]['teams'][info_match]['players'])):
            results[f'match{game}'][results['sumary']['team_info'][f'team{info_match}']['name']]["player_info"].update({
                        match['match']['games'][game]['teams'][info_match]['players'][player_info]['name'].upper() : {
                            'kills': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['kills']['count'],
                            'deaths': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['deaths']['count'],
                            'plants': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['diffuserPlanted']['count'],
                            'disarms': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['diffuserDisabled']['count'],
                            'oneVX': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['oneVsMultiple']['count'],
                            'HS': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['headshots']['count'],
                            'open_deaths': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['openingDeaths']['count'],
                            'open_kill': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['openingKills']['count'],
                            'clutch': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['clutch']['count'],
                            'kost': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['kost'],
                            'eps' : match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['eps']
                    }
                }
            )
        return results

    def set_team_winner_map(self, results={}, match={}, game=0):
        team0_score = results[f'match{game}'][results['sumary']['team_info']['team0']['name']]['team_info']['score']
        team1_score = results[f'match{game}'][results['sumary']['team_info']['team1']['name']]['team_info']['score']

        if team0_score> team1_score:
            results[f'match{game}'][results['sumary']['team_info']['team0']['name']]['team_info']['winner'] = 1
            results[f'match{game}'][results['sumary']['team_info']['team1']['name']]['team_info']['winner'] = 0

            return results

        results[f'match{game}'][results['sumary']['team_info']['team1']['name']]['team_info']['winner'] = 1
        results[f'match{game}'][results['sumary']['team_info']['team0']['name']]['team_info']['winner'] = 0

        return results

    def create_matches_cache(self, match= ''):
        try:
            with open('/home/thiago/Projetos/dataSiege/Project-Data-Siege/main/cache_matches.txt', 'a') as file:
                file.write(f"{match}\n")
        except Exception as e:
            logger.error('ERROR')
            logger.error(e)
if __name__ == '__main__': 
    app().get_matches_info()