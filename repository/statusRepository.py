from repository.baseRepository import BaseRepository


class StatusRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "status"
