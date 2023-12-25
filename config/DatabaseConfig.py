import MySQLdb

import settings


class DatabaseConfig:
    def __init__(self):
        self.connection = MySQLdb.connect(**settings.DATABASES)

    def getConnection(self):
        return self.connection
