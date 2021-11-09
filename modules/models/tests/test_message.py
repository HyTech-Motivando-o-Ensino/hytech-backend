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
from message import Message


class TesteMessage(TestCase):
    def setUp(self):
        self.message = Message()



if __name__ == '__main__':
    main(verbosity=2)