import typing
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
from class_ import Class


class TesteClass(TestCase):
    def setUp(self):
        self.class_ = Class(1, 1, 2, "923 8870 5812")
    
    def test_class_attr_id_e_int(self):
        self.assertIsInstance(self.class_.get_id(), int)

    def test_class_attr_id_e_is_not_int(self):
        self.class_.set_id("teste")
        self.assertNotEqual(type(self.class_.get_id()), int)
    
    def test_class_attr_course_id_e_int(self):
        self.assertIsInstance(self.class_.get_course_id(), int)

    def test_class_attr_course_id_e_in_not_int(self):
        self.class_.set_course_id("teste")
        self.assertNotEqual(type(self.class_.get_course_id()), int)
    
    def test_class_attr_period_e_int(self):
        self.assertIsInstance(self.class_.get_period(), int)
    
    def test_class_attr_period_e_is_not_int(self):
        self.class_.set_period("teste")
        self.assertNotEqual(self.class_.get_period(), int)

    def test_class_attr_period_e_less_1(self):
        self.class_.set_period(0)
        self.assertLess(self.class_.get_period(), 1)

    def test_class_attr_period_e_less_8(self):
        self.class_.set_period(1)
        self.assertLess(self.class_.get_period(), 8)

    def test_class_attr_period_e_greater_1(self):
        self.class_.set_period(8)
        self.assertGreater(self.class_.get_period(), 1)

    def test_class_attr_period_e_greater_8(self):
        self.class_.set_period(9)
        self.assertGreater(self.class_.get_period(), 8)
    
    def test_class_attr_zoom_id_e_str(self):
        self.assertIsInstance(self.class_.get_zoom_id(), str)

    def test_class_attr_zoom_id_e_is_not_str(self):
        self.class_.set_zoom_id(1)
        self.assertNotEqual(type(self.class_.get_zoom_id()), str)

if __name__ == '__main__':
    main(verbosity=2)