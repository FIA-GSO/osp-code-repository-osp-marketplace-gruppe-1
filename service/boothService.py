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
        self.boothRepository.updateById
        (
            boothID, 
            [
                {"status": self.STATUS_REJECTED},
            ]
        )
    
    def acceptBoothRegistration(self, boothID: int):
        self.boothRepository.updateById
        (
            boothID, 
            [
                {"status": self.STATUS_ACCEPTED},
            ]
        )