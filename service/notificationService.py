from repository.notificationRepository import NotificationRepository

class NotificationService:

    STATUS_REJECTED = 2
    STATUS_ACCEPTED = 3
    STATUS_IN_PROGRESS = 1

    def __init__(self):
        self.notificationRepository = NotificationRepository()
        pass

    def saveNotificationForStatusChange(self, userId: int, status: str):
        headline = "Der Status ihrer event anmeldung wurde aktualisiert"
        message = "Der Status ihrer event anmeldung wurde auf " + str(status) + " geendert."
        self.saveNotification(userId, headline, message)

    def saveNotification(self, userId: int, headline: str, message: str,):
        self.notificationRepository.insert(
            [
                {'user': userId},
                {'headline': headline},
                {'message': message},
            ]
        )
    
    def getNotificationByUser(self, userId:int):
        return self.notificationRepository.getByUserID(userId)