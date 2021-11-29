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
from professor import Professor

class TesteProfessor(TestCase):
    def setUp(self):
        self.professor = Professor(1, "Juliano", "photo", "(81)99994-0000", "jmb@cesar.school", "Juliano", "(81)99994-0000")

    def test_professor_attr_id_e_int(self):
        self.assertIsInstance(self.professor.get_id(), int)

    def test_professor_attr_id_e_is_not_int(self):
        self.professor.set_id("teste")
        self.assertNotEqual(type(self.professor.get_id()), int)

    def test_professor_attr_name_e_str(self):
        self.assertIsInstance(self.professor.get_name(), str)

    def test_entity_attr_name_e_is_not_str(self):
        self.professor.set_name(1)
        self.assertNotEqual(type(self.professor.get_name()), str)

    def test_professor_attr_photo_e_str(self):
        self.assertIsInstance(self.professor.get_photo(), str)

    def test_entity_attr_photo_e_is_not_str(self):
        self.professor.set_photo(1)
        self.assertNotEqual(type(self.professor.get_photo()), str)

    def test_professor_attr_contact_e_str(self):
        self.assertIsInstance(self.professor.get_contact(), str)

    def test_entity_attr_contact_e_is_not_str(self):
        self.professor.set_contact(1)
        self.assertNotEqual(type(self.professor.get_contact()), str)

    def test_professor_attr_email_e_str(self):
        self.assertIsInstance(self.professor.get_email(), str)

    def test_entity_attr_email_e_is_not_str(self):
        self.professor.set_email(1)
        self.assertNotEqual(type(self.professor.get_email()), str)

    def test_professor_attr_slack_e_str(self):
        self.assertIsInstance(self.professor.get_slack(), str)

    def test_entity_attr_slack_e_is_not_str(self):
        self.professor.set_slack(1)
        self.assertNotEqual(type(self.professor.get_slack()), str)

    def test_professor_attr_whatsapp_e_str(self):
        self.assertIsInstance(self.professor.get_whatsapp(), str)

    def test_entity_attr_whatsapp_e_is_not_str(self):
        self.professor.set_whatsapp(1)
        self.assertNotEqual(type(self.professor.get_whatsapp()), str)

if __name__ == '__main__':
    main(verbosity=2)