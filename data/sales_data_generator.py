from faker import Faker
import csv
import os

class DataGenerator:
    """
    Classe para gerar dados falsos e salvá-los em arquivos CSV.
    
    Atributos:
        num_users (int): Número de usuários para gerar.
        num_products (int): Número de produtos para gerar.
        num_sales (int): Número de vendas para gerar.
        data_path (str): Caminho do diretório para salvar os arquivos CSV gerados.
    """
    def __init__(self, num_users=100, num_products=50, num_sales=100, data_path='data'):
        """
        Inicializa a instância de DataGenerator com os valores padrão ou personalizados.
        """
        self.fake = Faker()
        self.num_users = num_users
        self.num_products = num_products
        self.num_sales = num_sales
        self.data_path = data_path
        os.makedirs(self.data_path, exist_ok=True)
    
    def generate_users_csv(self):
        """Gera um arquivo CSV para usuários com id, nome, email e data de nascimento."""
        with open(os.path.join(self.data_path, 'users.csv'), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'email', 'birthdate'])
            for _ in range(self.num_users):
                writer.writerow([self.fake.unique.random_int(min=1, max=9999), self.fake.name(), self.fake.email(), self.fake.date_of_birth()])

    def generate_products_csv(self):
        """Gera um arquivo CSV para produtos com id, nome, categoria e preço."""
        with open(os.path.join(self.data_path, 'products.csv'), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'category', 'price'])
            for _ in range(self.num_products):
                writer.writerow([self.fake.unique.random_int(min=1, max=9999), self.fake.word(), self.fake.word(), self.fake.random_number(digits=2)])
    
    def generate_sales(self):
        """
        Gera um arquivo CSV para vendas com id, id do cliente, id do produto, quantidade e preço de venda.
        Utiliza os arquivos users.csv e products.csv gerados anteriormente.
        """
        products_file = os.path.join(self.data_path, 'products.csv')
        users_file = os.path.join(self.data_path, 'users.csv')
        products = []
        users = []
        
        with open(products_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                products.append(row['id'])
        
        with open(users_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                users.append(row['id'])
        
        with open(os.path.join(self.data_path, 'sales.csv'), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'customer_id', 'product_id', 'quantity', 'sale_price'])
            for _ in range(self.num_sales):
                product_id = self.fake.random.choice(products)
                customer_id = self.fake.random.choice(users)
                quantity = self.fake.random_int(min=1, max=10)
                sale_price = float(self.fake.random_number(digits=2))
                writer.writerow([self.fake.unique.random_int(min=1, max=9999), customer_id, product_id, quantity, sale_price])
    
    def start(self):
        """
        Inicia a geração de todos os arquivos CSV especificados: usuários, produtos e vendas.
        """
        self.generate_users_csv()
        self.generate_products_csv()
        self.generate_sales()

if __name__ == "__main__":
    # Inicializa e inicia a geração de dados com 5 mil vendas
    generator = DataGenerator(
        num_sales=5000
    )
    generator.start()
