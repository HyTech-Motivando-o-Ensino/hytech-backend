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


class TesteConnectDB(TestCase):
    def setUp(self):
        self.connect = ConnectDB()
    
    def test_class_construct_erro_acessando_dotenv(self):
        self.assertEqual(ConnectDB(), "modules/../.env")

    def test_connection_db(self):
        db_return = self.connect.connect()
        self.assertIsInstance(db_return, )
    
    def test_class_attr_id_e_int(self):
        self.assertIsInstance(self.class_.get_id(), int)
    
    def test_class_attr_course_id_e_int(self):
        self.assertIsInstance(self.class_.get_course_id(), int)
    
    def test_class_attr_period_e_int(self):
        self.assertIsInstance(self.class_.get_period(), int)

    def test_class_attr_zoom_id_e_str(self):
        self.assertIsInstance(self.class_.get_zoom_id(), str)

if __name__ == '__main__':
    main(verbosity=2)