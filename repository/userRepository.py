from repositories.baseRepository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "user"