from repository.baseRepository import BaseRepository


class BoothRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "booth"

    def getByEventID(self, eventID: int, respectDisabled:bool = True):
        sql = 'SELECT * FROM ' + self.table_name + ' WHERE event = "' + str(eventID) + '"'
        if respectDisabled:
            sql += ' AND disabled = 0'
        self.cursor.execute(sql)
        return self.cursor.fetchall()