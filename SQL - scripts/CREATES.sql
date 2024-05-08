CREATE TABLE region (
id_region INT IDENTITY(1,1) PRIMARY KEY,
name_region NVARCHAR(MAX), 
picture NVARCHAR(MAX)
);

CREATE TABLE team (
id_team INT IDENTITY(1,1) PRIMARY KEY,
name_team NVARCHAR(MAX), 
picture NVARCHAR(MAX),
id_region INT
);

CREATE TABLE staff(
id_staff INT IDENTITY(1,1) PRIMARY KEY,
name_staff NVARCHAR(MAX),
id_team INT,
encharge NVARCHAR(MAX),
picture NVARCHAR(MAX)
);

CREATE TABLE player(
id_player INT IDENTITY(1,1) PRIMARY KEY,
name_player NVARCHAR(MAX),
id_team INT,
picture NVARCHAR(MAX)
);

CREATE TABLE maps(
id_map INT IDENTITY(1,1) PRIMARY KEY,
name_map NVARCHAR(MAX),
picture NVARCHAR(MAX)
);

DROP TABLE mapa;

CREATE TABLE operator(
id_operator INT IDENTITY(1,1) PRIMARY KEY,
name_operator NVARCHAR(MAX),
side NVARCHAR(3),
picture NVARCHAR(MAX),
icon NVARCHAR(MAX)
);

CREATE table matchs (
id_match INT IDENTITY(1,1) PRIMARY KEY,
id_region INT,
date_match DATE,
md1 BIT,
md3 BIT,
id_md1 INT,
id_md3 INT,
id_ban1 INT,
id_ban2 INT,
id_map1 INT,
id_map2 INT,
id_map3 INT,
id_team1 INT,
id_team2 INT,
qtd_rounds INT
);

CREATE table team_match (
id_team_match INT IDENTITY(1,1) PRIMARY KEY,
id_team INT,
id_match INT,
victory BIT,
w_rounds INT,
l_rounds INT
);

CREATE TABLE player_match (
id_team_match INT IDENTITY(1,1) PRIMARY KEY,
id_player INT,
id_match INT,
id_team INT,
kills INT,
deaths INT,
plants INT,
disarms INT,
OnevX INT,
HS INT,
id_atk_operator INT,
id_def_operator INT,
open_kills INT,
open_deaths INT
);

CREATE TABLE ban_operator(
id_ban INT IDENTITY(1,1) PRIMARY KEY,
id_match INT,
id_team INT,
ban1 INT,
ban2 INT
);

CREATE TABLE map_ban_md3(
id_md3 INT IDENTITY(1,1) PRIMARY KEY,
id_match INT,
id_team INT,
ban1 INT,
ban2 INT,
pick INT,
ban3 INT,
decider INT
);

CREATE TABLE map_ban_md1(
id_md1 INT IDENTITY(1,1) PRIMARY KEY,
id_match INT,
id_team INT,
ban1 INT,
ban2 INT,
ban3 INT,
ban4 INT,
pick INT
);

