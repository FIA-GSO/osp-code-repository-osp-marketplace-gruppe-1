from repository.eventRepository import EventRepository
from repository.boothRepository import BoothRepository
from repository.lectureRepository import LectureRepository
from repository.userRepository import UserRepository
from service.userService import UserService



class EventService:
    def __init__(self):
        self.eventRepository = EventRepository()
        self.boothRepository = BoothRepository()
        self.lectureRepository = LectureRepository()
        self.userRepository = UserRepository()
        self.userService = UserService()
        pass

    def getCurrentEvents(self):
       return self.eventRepository.getAll()