from enum import Enum

"""
All valid server lists
"""


class ServerLists(Enum):
    ServerLamp = 'lamp'
    ServerLnmp = 'lnmp'
    ServerLnmpWordpress = 'lnmp-wordpress'
    ServerDjangoUwsgi = 'django-uwsgi'
