import os, re
from loguru import logger
from translate import translate_names

class getImages:
    disk_path = 'image/'

    def get_all_elements_in_dir(self, name_dir:str = None):
        return os.listdir(self.disk_path + name_dir)

    def get_maps_images_from_disk(self) -> list: 
        list_image_maps = {}
        name_dir = 'maps/'
        all_images = self.get_all_elements_in_dir(name_dir)

        nomes_mapas = translate_names().translate_map_names()

        for image in all_images:
            map_name = re.sub('r6-maps-', '', image)
            map_name = re.sub('.png', '', map_name)

            list_image_maps.update({
                map_name:{
                    "name":map_name,
                    "nome":nomes_mapas[map_name],
                    'image': self.disk_path + name_dir +  image
                    }}
                )

        return list_image_maps

    def get_times_images_from_disk(self) -> dict: 
        list_image_times = {}
        name_dir = 'teams/'
        all_images = self.get_all_elements_in_dir(name_dir)
        for image in all_images:

            name_team = re.sub('time_', '', image)
            name_team = re.sub('.png', '', name_team)

            list_image_times.update({
                name_team: self.disk_path + name_dir + image
            })

        return list_image_times

    def get_leagues_images_from_disk(self) -> dict: 
        list_image_leagues = {}
        name_dir = 'regiao/'
        all_images = self.get_all_elements_in_dir(name_dir)
        for image in all_images:

            region_name = image.split('_')[1]

            list_image_leagues.update({
                region_name: self.disk_path + name_dir + image
            })

        return list_image_leagues

    def get_operators_images_from_disk(self) -> list: 
        operator_names=[]

        name_dir_icons = 'operador/icon/'
        name_dir_img = 'operador/foto/'

        dict_all_images_operators= {}

        all_icons = sorted(self.get_all_elements_in_dir(name_dir_icons))
        all_images = sorted(self.get_all_elements_in_dir(name_dir_img))

        for img in all_icons:
            operator_names.append(img.split('.png')[0].capitalize())

        for i in range(len(all_icons)):
            dict_all_images_operators.update({
                    operator_names[i]:{
                        'icon': name_dir_icons + all_icons[i],
                        'image': name_dir_img + all_images[i],
                    }
                })

        return dict_all_images_operators


    def get_players_name_from_disk(self) -> dict:
        dict_all_team_players = {}
        name_dir_players_base = self.disk_path + 'players/'

        for dir_name in os.listdir(name_dir_players_base):
            dict_all_team_players.update({
                dir_name :{
                    'players':[player.split('.png')[0] for player in os.listdir(name_dir_players_base + dir_name)],
                    'images':os.listdir(name_dir_players_base + dir_name)
                }
            })

        return dict_all_team_players

    def get_staff_name_from_disk(self) -> dict:
        dict_all_team_staff = {}
        name_dir_staff_base = self.disk_path + 'staff/'

        for dir_name in os.listdir(name_dir_staff_base):
            dict_all_team_staff.update({
                dir_name :{
                    'staff':[player.split('.png')[0] for player in os.listdir(name_dir_staff_base + dir_name)],
                    'images':os.listdir(name_dir_staff_base + dir_name)
                }
            })

        return dict_all_team_staff
