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
        self.classroom = Classroom()
        

if __name__ == '__main__':
    main(verbosity=2)