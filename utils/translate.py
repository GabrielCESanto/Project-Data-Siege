import unicodedata
class translate_names:
    def translate_map_names(self) -> dict: 
        return {
            'kafe' : 'café dostoyevsky',
            'chalet' : 'chalé',
            'border' : 'fronteira',
            'oregon' : 'oregon',
            'consulate' : 'consulado',
            'clubhouse' : 'clube',
            'skyscraper' : 'arranha céu',
            'nighthaven_labs' : 'laboratorios nighthaven',
            'bank' : 'banco'
        }

    def remove_acentos(self, string) -> str:
        string = unicodedata.normalize("NFD", string)
        string = string.encode('ascii', 'ignore')
        formatted_string = string.decode('utf-8')

        return formatted_string
