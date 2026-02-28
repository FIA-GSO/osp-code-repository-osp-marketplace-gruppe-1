from repository.baseRepository import BaseRepository


class NotificationRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table_name = "notification"