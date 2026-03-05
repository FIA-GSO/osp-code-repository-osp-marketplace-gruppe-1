from repository.boothRepository import BoothRepository

class BoothService:

    STATUS_REJECTED = 2
    STATUS_ACCEPTED = 3
    STATUS_IN_PROGRESS = 1

    def __init__(self):
        self.boothRepository = BoothRepository()
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
    
    def acceptBoothRegistration(self, boothID: int):
        self.boothRepository.updateById(
            boothID, 
            [
                {"status": self.STATUS_ACCEPTED},
            ]
        )

    def getBoothRegistrationsForUser(self, userID: int):
        return self.boothRepository.getByUserID(userID)
    
    def updateBooth(self, uid: int, first_name: str, last_name: str, email: str, telephone: str, note: str, table_count: str, chair_count: str):
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