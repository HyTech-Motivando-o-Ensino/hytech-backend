from unittest import TestCase, main, mock
try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..'
            )
        )
    )
except:
    raise
from connect import ConnectDB
from mysql.connector.connection_cext import CMySQLConnection

class TesteConnectDB(TestCase):
    def setUp(self):
        self.connect = ConnectDB()
    
    def test_class_construct_erro_acessando_dotenv(self):
        self.assertEqual(self.connect.initialize(), "modules/../.env")

    def test_connection_db(self):
        db_return = self.connect.connect()
        self.assertIsInstance(db_return, CMySQLConnection)

if __name__ == '__main__':
    main(verbosity=2)