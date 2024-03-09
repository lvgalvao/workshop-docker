import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

class PostgresLoader:
    def __init__(self):
        """
        Inicializa a instância de PostgresLoader, carregando as configurações de banco de dados
        a partir de variáveis de ambiente.
        """
        load_dotenv()  # Carrega variáveis de ambiente do arquivo .env
        
        # Define as configurações do banco de dados a partir das variáveis de ambiente
        self.database_host = os.getenv('POSTGRES_HOST')
        self.database_user = os.getenv('POSTGRES_USER')
        self.database_password = os.getenv('POSTGRES_PASSWORD')
        self.database_name = os.getenv('POSTGRES_DB')

        # Cria a string de conexão com o banco de dados
        self.connection_string = f'postgresql://{self.database_user}:{self.database_password}@{self.database_host}/{self.database_name}'

        # Inicializa a engine do SQLAlchemy
        self.engine = create_engine(self.connection_string)

    def load_csv_to_postgres(self, csv_path, table_name):
        """
        Carrega dados de um arquivo CSV para uma tabela PostgreSQL específica.

        Args:
            csv_path (str): Caminho do arquivo CSV a ser carregado.
            table_name (str): Nome da tabela destino no PostgreSQL.
        """
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, self.engine, if_exists='append', index=False, method='multi', chunksize=1000)
        print(f'Dados carregados com sucesso para a tabela {table_name}.')

    def run(self):
        """
        Executa o processo de carregamento para todos os arquivos CSV especificados.
        """
        # Caminhos dos arquivos CSV a serem carregados
        csv_files = {
            'users': 'data/users.csv',
            'products': 'data/products.csv',
            'sales': 'data/sales.csv'
        }

        # Carrega cada arquivo CSV para a tabela correspondente no PostgreSQL
        for table_name, csv_path in csv_files.items():
            self.load_csv_to_postgres(csv_path, table_name)

if __name__ == '__main__':
    loader = PostgresLoader()
    loader.run()
