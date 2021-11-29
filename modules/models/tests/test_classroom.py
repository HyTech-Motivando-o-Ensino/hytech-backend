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
from classroom import Classroom


class TesteClassroom(TestCase):
    def setUp(self):
        self.classroom = Classroom(1, 2, 3)
        
    def test_classroom_attr_id_e_int(self):
        self.assertIsInstance(self.classroom.get_id(), int)

    def test_classroom_attr_id_e_is_not_int(self):
        self.classroom.set_id("teste")
        self.assertNotEqual(type(self.classroom.get_id()), int)

    def test_classroom_attr_classroom_id_e_int(self):
        self.assertIsInstance(self.classroom.get_id(), int)

    def test_classroom_attr_classroom_id_e_is_not_int(self):
        self.classroom.set_id("teste")
        self.assertNotEqual(type(self.classroom.get_id()), int)

    def test_classroom_attr_subject_id_e_int(self):
        self.assertIsInstance(self.classroom.get_id(), int)

    def test_classroom_attr_subject_id_e_is_not_int(self):
        self.classroom.set_id("teste")
        self.assertNotEqual(type(self.classroom.get_id()), int)

if __name__ == '__main__':
    main(verbosity=2)