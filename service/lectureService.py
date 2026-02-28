from repository.lectureRepository import LectureRepository

class LectureService:

    STATUS_REJECTED = 2
    STATUS_ACCEPTED = 3
    STATUS_IN_PROGRESS = 1

    def __init__(self):
        self.lectureRepository = LectureRepository()
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
    
    def acceptLectureRegistration(self, lectureID: int):
        self.lectureRepository.updateById(
            lectureID, 
            [
                {"status": self.STATUS_ACCEPTED},
            ]
        )