INSERT INTO team (name_team, picture, id_region) 
VALUES 
('Black Dragons', 'https://liquipedia.net/commons/images/thumb/a/aa/Black_Dragons_e-Sports_allmode.png/600px-Black_Dragons_e-Sports_allmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil')),
('E1 Sports', 'https://liquipedia.net/commons/images/b/b1/E1_Sports_allmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil')),
('Faze Clan', 'https://liquipedia.net/commons/images/thumb/7/79/FaZe_Clan_November_2021_full_lightmode.png/600px-FaZe_Clan_November_2021_full_lightmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil')),
('Fluxo', 'https://liquipedia.net/commons/images/thumb/e/e3/Fluxo_lightmode.png/600px-Fluxo_lightmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil')),
('Furia Esports', 'https://liquipedia.net/commons/images/thumb/b/bd/FURIA_Esports_full_lightmode.png/600px-FURIA_Esports_full_lightmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil')),
('Team Liquid', 'https://liquipedia.net/commons/images/thumb/f/f5/Team_Liquid_2024_full_lightmode.png/600px-Team_Liquid_2024_full_lightmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil')),
('MIBR', 'https://liquipedia.net/commons/images/thumb/8/85/MIBR_2018_lightmode.png/600px-MIBR_2018_lightmode.png',1),
('Ninja in Pyjamas', 'https://liquipedia.net/commons/images/thumb/4/42/Ninjas_in_Pyjamas_2021_full_lightmode.png/600px-Ninjas_in_Pyjamas_2021_full_lightmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil')),
('Vivo Keyd Stars', 'https://liquipedia.net/commons/images/thumb/a/ab/Keyd_Stars_2022_full_lightmode.png/600px-Keyd_Stars_2022_full_lightmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil')),
('W7M', 'https://liquipedia.net/commons/images/thumb/7/79/W7M_esports_full_allmode.png/600px-W7M_esports_full_allmode.png',(SELECT id_region FROM region WHERE name_region = 'Brazil'));

