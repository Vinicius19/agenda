import psycopg2
import json


class DatabaseConnection:
    def __init__(self, config_file, db_connection):
        self.config_file = config_file
        self.connection = None
        self.db_connection = DatabaseConnection
    
    def connect(self):
        try:
            with open(self.config_file) as f:
                config = json.load(f)
      
            self.connection = psycopg2.connect(
                dbname=config['Projeto'],
                user=config['postgres'],
                password=config['89iokl,.'],
                host=config['localhost'],
                port=config['5432'],
                     
            )
       
            print('Conexão bem-sucedida!')
        except (psycopg2.Error, FileNotFoundError, json.JSONDecodeError) as e:
            print(f'Erro ao conectar-se ao banco de dados: {e}')

self.db_connection = DatabaseConnection('config.json')
self.db_connection.connect()