from repository.baseRepository import BaseRepository


class EventRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "event"
