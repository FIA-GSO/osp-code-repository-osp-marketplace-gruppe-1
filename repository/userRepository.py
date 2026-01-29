from repository.baseRepository import BaseRepository
from utiltiy.hashUtility import HashUtility

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "user"

    def getByPasswordAndEmail(self, email: str, password: str):
        print(password)
        sql = 'SELECT * FROM ' + self.table_name + ' WHERE email = "' + email + '" AND password_hash = "' + HashUtility.hash(password)+ '"'
        self.cursor.execute(sql)
        return self.cursor.fetchall()
