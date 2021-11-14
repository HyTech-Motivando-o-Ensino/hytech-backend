from .connect import ConnectDB

# variavel que vai carregar a instância do banco de dados
db_instance = None
db_cursor = db_instance

def main():
    global db_instance
    global db_cursor
    
    db_instance = ConnectDB().connect()

def get_status_db():
    try:
        db_cursor = db_instance.cursor()
        db_cursor.execute("SELECT * FROM test")
        result = db_cursor.fetchall()
        return result[0][0]
    except Exception as e:
        raise e

def get_class():
    try:
        db_cursor = db_instance.cursor()
        db_cursor.execute("SELECT id, course_id, period, zoom_id FROM class")
        result = db_cursor.fetchall()
        
        for obj in result:
            print(obj)
        return "Finished"
    except Exception as e:
        raise e

if __name__ == '__main__':
    main()