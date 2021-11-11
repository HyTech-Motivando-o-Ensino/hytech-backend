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
from pathlib import PosixPath

class TesteConnectDB(TestCase):
    def setUp(self):
        self.connect = ConnectDB()
    
    def test_class_init_dotenv_values_db(self):
        dotenv_return = self.connect.initialize()
        self.assertEqual(dotenv_return, PosixPath('modules/../.env'))

    def test_connection_db(self):
        self.connect.initialize()
        db_return = self.connect.connect()
        self.assertIsInstance(db_return, CMySQLConnection)
        db_return.close()

if __name__ == '__main__':
    main(verbosity=2)