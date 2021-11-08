from .connect import ConnectDB

# variavel que vai carregar a instância do banco de dados
db_instance = None
db_cursor = db_instance

def main():
    global db_instance
    global db_cursor
    
    db_instance = ConnectDB().connect()
    db_cursor = db_instance.cursor()


if __name__ == '__main__':
    main()