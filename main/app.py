import sys
sys.path.append('/home/thiago/Projetos/dataSiege/Project-Data-Siege')
from loguru import logger
import utils.request
from database.insertData import insertData
from app_base import app_base

class app(app_base):
    def get_matches_info(self):
        insersor = insertData()
        results = {
            'sumary' : {},
            'match0' : {},
            'match1' : {},
            'match2' : {}
        }
        requests_maker=  utils.request.request()
        matches_info = requests_maker.request_info(5850)

        results.update(self.set_sumary_info(results, matches_info))
        results.update(self.set_all_info_each_map(results, matches_info))
        results['sumary']['qtd_rounds'] = self.qtd_rounds

        insersor.insert_data_ban_operator(results)
        id_last_match = insersor.insert_data_match(results)
        insersor.insert_data_team_match(results, id_last_match)
        insersor.insert_data_player_match(results, id_last_match)


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
                            'clutch': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['clutch']['count']
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

if __name__ == '__main__': 
    app().get_matches_info()