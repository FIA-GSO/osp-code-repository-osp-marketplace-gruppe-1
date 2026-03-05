from repository.boothRepository import BoothRepository
from service.emailService import EmailService

class BoothService:

    STATUS_REJECTED = 2
    STATUS_ACCEPTED = 3
    STATUS_IN_PROGRESS = 1

    def __init__(self):
        self.boothRepository = BoothRepository()
        self.emailService = EmailService()
        pass

    def getBoothRegestrationsForEvent(self, eventID: int,):
        return self.boothRepository.getByEventID(eventID)
    
    def rejectBoothRegistration(self, boothID: int):
        self.boothRepository.updateById(
            boothID, 
            [
                {"status": self.STATUS_REJECTED},
            ]
        )
        contactPersionEmail = self.boothRepository.getById(lectureID)[0]['email']
        self.emailService.sendUpdateNotifictionMail(contactPersionEmail, self.boothRepository.getById(boothID))
    
    def acceptBoothRegistration(self, boothID: int):
        self.boothRepository.updateById(
            boothID, 
            [
                {"status": self.STATUS_ACCEPTED},
            ]
        )
        contactPersionEmail = self.boothRepository.getById(lectureID)[0]['email']
        self.emailService.sendUpdateNotifictionMail(contactPersionEmail, self.boothRepository.getById(boothID))

    def getBoothRegistrationsForUser(self, userID: int):
        return self.boothRepository.getByUserID(userID)
    
    def updateBooth(self, uid: int, first_name: str, last_name: str, email: str, telephone: str, note: str, table_count: str, chair_count: str, staus: str):
        self.boothRepository.updateById(
            uid,
            [
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'telephone': telephone,
                    'note': note,
                    'table_count': table_count,
                    'chair_count': chair_count,
                    'status': staus
                }
            ]
        )
    
    def deleteBooth(self, uid):
        self.boothRepository.updateById(
            uid,
            [
                {'disabled': 1}
            ]
        )

    def getBoothById(self, uid):
        return self.boothRepository.getById(uid)[0]