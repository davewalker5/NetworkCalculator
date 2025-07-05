from enum import IntEnum


class AddressType(IntEnum):
    NETWORK = 0
    FIRST_HOST = 1
    LAST_HOST = 2
    BROADCAST = 3
