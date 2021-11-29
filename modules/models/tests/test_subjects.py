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
from subjects import Subjects


class TesteSubjects(TestCase):
    def setUp(self):
        self.subjects = Subjects(1, "computer science", 5)

    def test_subjects_attr_id_e_int(self):
        self.assertIsInstance(self.subjects.get_id(), int)

    def test_subjects_attr_id_e_is_not_int(self):
        self.subjects.set_id("teste")
        self.assertNotEqual(type(self.subjects.get_id()), int)

    def test_subjects_attr_name_e_str(self):
        self.assertIsInstance(self.subjects.get_name(), str)

    def test_subjects_attr_name_e_is_not_str(self):
        self.subjects.set_name(1)
        self.assertNotEqual(type(self.subjects.get_name()), str)

    def test_subjects_attr_period_e_int(self):
        self.assertIsInstance(self.subjects.get_period(), int)
    
    def test_subjects_attr_period_e_is_not_int(self):
        self.subjects.set_period("teste")
        self.assertNotEqual(self.subjects.get_period(), int)

    def test_subjects_attr_period_e_less_1(self):
        self.subjects.set_period(0)
        self.assertLess(self.subjects.get_period(), 1)

    def test_subjects_attr_period_e_less_8(self):
        self.subjects.set_period(1)
        self.assertLess(self.subjects.get_period(), 8)

    def test_subjects_attr_period_e_greater_1(self):
        self.subjects.set_period(8)
        self.assertGreater(self.subjects.get_period(), 1)

    def test_subjects_attr_period_e_greater_8(self):
        self.subjects.set_period(9)
        self.assertGreater(self.subjects.get_period(), 8)

if __name__ == '__main__':
    main(verbosity=2)