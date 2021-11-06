from .connect import ConnectDB

# variavel que vai carregar a instância do banco de dados
db_instance = None

def main():
    global db_instance
    db_instance = ConnectDB().connect()

if __name__ == '__main__':
    main()