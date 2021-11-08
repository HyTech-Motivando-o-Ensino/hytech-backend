from enum import Enum

class Status(Enum):
    SENDING = "sending"
    SENT = "sent"
    ERROR = "error"