import sys
sys.path.append('/home/thiago/Projetos/dataSiege/Project-Data-Siege')
import utils.request
from loguru import logger

class app:
    def get_matches_info(self):
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
        for i in results.keys():
            logger.debug(results[i])


    def set_sumary_info(self, results={}, match={}):
        results['sumary']['championship'] = self.get_championship_info(match)
        results['sumary']['team_info'] =  self.get_team_info(match)
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

        return sumary

    def get_championship_info(self, match = {}):
        return {  
            'name' : match['championship']['name'].strip(),
            'competition' : match['competition']['name'].strip(),
            'matchFormat' : match['match']['matchFormatNumberOfGames']
        }

    def set_all_info_each_map(self, results={}, match={}):
        for game in range(results['sumary']['championship']['matchFormat']):
            results[f'match{game}'].update({
                'map' : match['match']['games'][game]['map']['name']
            })

            if len(match['match']['games'][game]['rounds']) > 1:

                for info_match in range(len(match['match']['games'][game]['teams'])):

                    results[f'match{game}'].update({
                        results['sumary']['team_info'][f'team{info_match}']['name']:{
                            'team_info':{
                                'score' : match['match']['games'][game]['teams'][info_match]['score'],
                                'banAtk' : match['match']['games'][game]['teams'][info_match]['operatorBans'][0]['name'] ,
                                'banDef' : match['match']['games'][game]['teams'][info_match]['operatorBans'][1]['name'] 
                            },
                            'player_info':{}
                        }
                    })

                    results = self.get_players_infos(results, match, game, info_match)

        return results

    def get_players_infos(self, results={}, match= {}, game=0, info_match=0):
        for player_info in range(len(match['match']['games'][game]['teams'][info_match]['players'])):
            results[f'match{game}'][results['sumary']['team_info'][f'team{info_match}']['name']]["player_info"].update({
                        match['match']['games'][game]['teams'][info_match]['players'][player_info]['name'] : {
                            'kills': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['kills']['count'],
                            'deaths': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['deaths']['count'],
                            'plants': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['diffuserPlanted']['count'],
                            'disarms': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['diffuserDisabled']['count'],
                            'oneVX': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['oneVsMultiple']['count'],
                            'HS': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['headshots']['count'],
                            'open_deaths': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['openingDeaths']['count'],
                            'open_kill': match['match']['games'][game]['teams'][info_match]['players'][player_info]['stats']['openingKills']['count']
                    }
                }
            )
        return results

if __name__ == '__main__': 
    app().get_matches_info()