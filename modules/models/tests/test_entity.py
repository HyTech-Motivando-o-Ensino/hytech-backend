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
from entity import Entity


class TesteEntity(TestCase):
    def setUp(self):
        self.entity = Entity(1, "name_entity", "Photo")

    def test_entity_attr_id_e_int(self):
        self.assertIsInstance(self.entity.get_id(), int)

    def test_entity_attr_id_e_is_not_int(self):
        self.entity.set_id("teste")
        self.assertNotEqual(type(self.entity.get_id()), int)
        
    def test_entity_attr_name_e_str(self):
        self.assertIsInstance(self.entity.get_name(), str)

    def test_entity_attr_name_e_is_not_str(self):
        self.entity.set_name(1)
        self.assertNotEqual(type(self.entity.get_name()), str)

    def test_entity_attr_photo_e_str(self):
        self.assertIsInstance(self.entity.get_photo(), str)

    def test_entity_attr_photo_e_is_not_str(self):
        self.entity.set_photo(1)
        self.assertNotEqual(type(self.entity.get_photo()), str)


if __name__ == '__main__':
    main(verbosity=2)