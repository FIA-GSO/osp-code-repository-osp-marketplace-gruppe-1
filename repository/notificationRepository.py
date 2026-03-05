from repository.baseRepository import BaseRepository


class NotificationRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "notification"

    def getByUserID(self, userID: int, respectDisabled:bool = True):
        sql = 'SELECT * FROM ' + self.table_name + ' WHERE user = "' + str(userID) + '"'
        if respectDisabled:
            sql += ' AND disabled = 0'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
        