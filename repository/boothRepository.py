from repository.baseRepository import BaseRepository


class BoothRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "booth"