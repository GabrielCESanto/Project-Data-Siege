import sqlite3
import databaseConnection
from loguru import logger

class createTables():
    def get_connection(self):
        connector = databaseConnection.connection.getInstance()
        return connector.database_connection()

    def create_tables(self):
        conn = self.get_connection()

        cursor = conn.cursor()
        cursor.execute(self.command_create_table_ban_mapas_md1())
        cursor.execute(self.command_create_table_ban_mapas_md3())
        cursor.execute(self.command_create_table_ban_operador())
        cursor.execute(self.command_create_table_jogador())
        cursor.execute(self.command_create_table_jogador_partida())
        cursor.execute(self.command_create_table_mapa())
        cursor.execute(self.command_create_table_operador())
        cursor.execute(self.command_create_table_partida())
        cursor.execute(self.command_create_table_regiao())
        cursor.execute(self.command_create_table_staff())
        cursor.execute(self.command_create_table_time())
        cursor.execute(self.command_create_table_time_partida())

        conn.commit()

    def command_create_table_ban_mapas_md1(self):
        return '''
            CREATE TABLE "ban_mapas_md1" (
            "id_md1"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "id_partida"	INTEGER,
            "id_time"	INTEGER,
            "ban1"	INTEGER,
            "ban2"	INTEGER,
            "ban3"	INTEGER,
            "ban4"	INTEGER,
            "pick"	INTEGER,
            FOREIGN KEY("pick") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("ban4") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("ban3") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("ban2") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("ban1") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("id_time") REFERENCES "time"("id_time"),
            FOREIGN KEY("id_partida") REFERENCES "partida"("id_partida")
        );'''

    def command_create_table_ban_mapas_md3(self):
        return '''
            CREATE TABLE "ban_mapas_md3" (
            "id_md3"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "id_partida"	INTEGER,
            "id_time"	INTEGER,
            "ban1"	INTEGER,
            "ban2"	INTEGER,
            "pick"	INTEGER,
            "ban3"	INTEGER,
            "decider"	INTEGER,
            FOREIGN KEY("ban3") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("pick") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("ban2") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("ban1") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("decider") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("id_time") REFERENCES "partida"("id_partida"),
            FOREIGN KEY("id_partida") REFERENCES "partida"("id_partida")
        );'''

    def command_create_table_ban_operador(self):
        return '''
            CREATE TABLE "ban_operador" (
            "id_ban"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "id_partida"	INTEGER,
            "id_time"	INTEGER,
            "ban1"	INTEGER,
            "ban2"	INTEGER,
            FOREIGN KEY("ban2") REFERENCES "operador"("id_operador"),
            FOREIGN KEY("ban1") REFERENCES "operador"("id_operador"),
            FOREIGN KEY("id_time") REFERENCES "time"("id_time"),
            FOREIGN KEY("id_partida") REFERENCES "partida"("id_partida")
        );'''

    def command_create_table_jogador(self):
        return '''
           CREATE TABLE "jogador" (
            "id_jogador"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "nome_jogador"	INTEGER,
            "foto"	BLOB,
            "id_time"	INTEGER,
            FOREIGN KEY("id_time") REFERENCES "time"("id_time")
        );'''

    def command_create_table_jogador_partida(self):
        return '''
            CREATE TABLE "jogador_partida" (
            "id_jogador_partida"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "id_jogador"	INTEGER,
            "id_partida"	INTEGER,
            "id_time"	INTEGER,
            "kills"	INTEGER,
            "deaths"	INTEGER,
            "plants"	INTEGER,
            "disarms"	INTEGER,
            "1vX"	INTEGER,
            "HS"	INTEGER,
            "id_operador_atk"	INTEGER,
            "id_operador_def"	INTEGER,
            "open_kill"	INTEGER,
            "open_death"	INTEGER,
            FOREIGN KEY("id_operador_def") REFERENCES "operador"("id_operador"),
            FOREIGN KEY("id_operador_atk") REFERENCES "operador"("id_operador"),
            FOREIGN KEY("id_time") REFERENCES "time"("id_time"),
            FOREIGN KEY("id_partida") REFERENCES "partida"("id_partida"),
            FOREIGN KEY("id_jogador") REFERENCES "jogador"("id_jogador")
        );'''

    def command_create_table_mapa(self):
        return '''
           CREATE TABLE "mapa" (
            "id_mapa"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "map_name"	TEXT,
            "nome_mapa"	TEXT,
            "foto"	BLOB
        );'''

    def command_create_table_operador(self):
        return '''
           CREATE TABLE "operador" (
            "id_operador"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "nome_operador"	TEXT,
            "lado_operador"	TEXT(3),
            "icone"	BLOB,
            "foto"	BLOB
        );'''

    def command_create_table_partida(self):
        return '''
            CREATE TABLE "partida" (
            "id_partida"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "id_regiao"	INTEGER NOT NULL,
            "data"	TEXT,
            "md1"	INTEGER(1),
            "md3"	INTEGER(1),
            "id_md1"	INTEGER,
            "id_md3"	INTEGER,
            "id_ban1"	INTEGER,
            "id_ban2"	INTEGER,
            "id_mapa1"	INTEGER NOT NULL,
            "id_mapa2"	INTEGER,
            "id_mapa3"	INTEGER,
            "id_time1"	INTEGER,
            "id_time2"	INTEGER,
            "qtd_rounds"	INTEGER,
            FOREIGN KEY("id_mapa2") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("id_mapa1") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("id_time2") REFERENCES "time_partida"("id_time_partida"),
            FOREIGN KEY("id_md3") REFERENCES "ban_mapas_md3"("id_md3"),
            FOREIGN KEY("id_mapa3") REFERENCES "mapa"("id_mapa"),
            FOREIGN KEY("id_ban1") REFERENCES "ban_operador"("id_ban"),
            FOREIGN KEY("id_md1") REFERENCES "ban_mapas_md1"("id_md1"),
            FOREIGN KEY("id_regiao") REFERENCES "regiao"("id_regiao"),
            FOREIGN KEY("id_time1") REFERENCES "time_partida"("id_time_partida"),
            FOREIGN KEY("id_ban2") REFERENCES "ban_operador"("id_ban")
        );'''

    def command_create_table_regiao(self):
        return '''
            CREATE TABLE "regiao" (
            "id_regiao"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "nome_regiao"	TEXT,
            "foto"	BLOB
        );'''

    def command_create_table_staff(self):
        return '''
           CREATE TABLE "staff" (
            "id_staff"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "nome_staff"	TEXT,
            "id_time"	INTEGER,
            "funcao"	TEXT,
            "foto"	BLOB,
            FOREIGN KEY("id_time") REFERENCES "time"("id_time")
        );'''

    def command_create_table_time(self):
        return '''
            CREATE TABLE "time" (
            "id_time"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "nome_time"	TEXT,
            "foto"	BLOB,
            "id_regiao"	INTEGER,
            FOREIGN KEY("id_regiao") REFERENCES "regiao"("id_regiao")
        );'''

    def command_create_table_time_partida(self):
        return '''
            CREATE TABLE "time_partida" (
            "id_time_partida"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            "id_time"	INTEGER,
            "id_partida"	INTEGER,
            "vitoria"	INTEGER,
            "rounds_vencidos"	INTEGER,
            "rounds_perdidos"	INTEGER,
            FOREIGN KEY("id_partida") REFERENCES "partida"("id_partida"),
            FOREIGN KEY("id_time") REFERENCES "time"("id_time")
        );'''