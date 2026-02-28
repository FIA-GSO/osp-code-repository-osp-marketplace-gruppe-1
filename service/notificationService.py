from repository.notificationRepository import NotificationRepository

class NotificationService:

    STATUS_REJECTED = 2
    STATUS_ACCEPTED = 3
    STATUS_IN_PROGRESS = 1

    def __init__(self):
        self.notificationRepository = NotificationRepository()
        pass

    def saveNotification(self, userId: int, message: string,):
        self.notificationRepository.insert(
            {'user': userId},
            {'message': message},
        )