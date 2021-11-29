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
        self.professor = Professor(1, "Juliano Machado Borges", photo, "(81)99990-0000", "jmb@cesar.school", "Juliano", "(81)99990-0000")


if __name__ == '__main__':
    main(verbosity=2)