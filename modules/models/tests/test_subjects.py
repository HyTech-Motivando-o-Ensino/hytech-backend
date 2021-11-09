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
        self.subjects = Subjects()