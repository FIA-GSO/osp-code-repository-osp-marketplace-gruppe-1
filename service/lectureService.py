from repository.lectureRepository import LectureRepository
from service.emailService import EmailService
from service.notificationService import NotificationService

class LectureService:

    STATUS_REJECTED = 2
    STATUS_ACCEPTED = 3
    STATUS_IN_PROGRESS = 1

    def __init__(self):
        self.lectureRepository = LectureRepository()
        self.emailService = EmailService()
        self.notificationService = NotificationService()
        pass

    def getTechnicalLectureRegestrationsForEvent(self, eventID: int):
        return self.lectureRepository.getByEventID(eventID)
    
    def rejectLectureRegistration(self, lectureID: int):
        self.lectureRepository.updateById(
            lectureID, 
            [
                {"status": self.STATUS_REJECTED},
            ]
        )
        lecture = self.lectureRepository.getById(lectureID)[0]
        contactPersionEmail = lecture['email']
        userId = lecture["user"]
        self.emailService.sendUpdateNotifictionMail(contactPersionEmail, self.lectureRepository.getById(lectureID))
        self.notificationService.saveNotificationForStatusChange(userId,  "Abgelehnt")
    
    def acceptLectureRegistration(self, lectureID: int):
        self.lectureRepository.updateById(
            lectureID,
            [
                {"status": self.STATUS_ACCEPTED},
            ]
        )
        contactPersionEmail = self.lectureRepository.getById(lectureID)[0]['email']
        lecture = self.lectureRepository.getById(lectureID)[0]
        contactPersionEmail = lecture['email']
        userId = lecture["user"]
        self.emailService.sendUpdateNotifictionMail(contactPersionEmail, self.lectureRepository.getById(lectureID))
        self.notificationService.saveNotificationForStatusChange(userId, "Angenommen")
    
    def getlectureRegistrationsForUser(self, userID: int):
        return self.lectureRepository.getByUserID(userID)
    
    def updateLecture(self, uid: int, first_name: str, last_name: str, email: str, telephone: str, note: str, topic: str, duration: int, status: str):
        self.lectureRepository.updateById(
            uid,
            [
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'telephone': telephone,
                    'note': note,
                    'topic': topic,
                    'duration': duration,
                    'status': status
                }
            ]
        )
    
    def deleteLecture(self, uid):
        self.lectureRepository.updateById(
            uid,
            [
                {'disabled': 1}
            ]
        )

    def getLectureById(self, uid):
        return self.lectureRepository.getById(uid)[0]