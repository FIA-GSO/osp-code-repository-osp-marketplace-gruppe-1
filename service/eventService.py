from repository.eventRepository import EventRepository
from repository.boothRepository import BoothRepository
from repository.lectureRepository import LectureRepository
from repository.statusRepository import StatusRepository
from repository.userRepository import UserRepository
from service.emailService import EmailService
from service.userService import UserService



class EventService:
    def __init__(self):
        self.eventRepository = EventRepository()
        self.boothRepository = BoothRepository()
        self.lectureRepository = LectureRepository()
        self.statusRepository = StatusRepository()
        self.userRepository = UserRepository()
        self.userService = UserService()
        self.emailService = EmailService()
        pass

    def getCurrentEvents(self):
       return self.eventRepository.getAll()

    def registerEvent(self, name: str, date: str, slots: int):
        self.eventRepository.insert(
            [
                {
                    'name': name,
                    'date': date,
                    'slots': slots
                }
            ]
        )

    def updateEvent(self, uid: int, name: str, date: str, slots: int):
        self.eventRepository.updateById(
            uid,
            [
                {
                    'name': name,
                    'date': date,
                    'slots': slots
                }
            ]
        )

    def registerForEvent(self, form):
        events =  form.getlist('events[]')
        donation = form.get('donation')

        if donation == "on":
            self.userRepository.updateById(
                self.userService.getUserUid(),
                [
                    {
                        'donation': 1
                    }
                ]
            )
            userCompany = self.userService.getUser()[0]['company']
            self.emailService.sendSupportAssociationMail(self.userService.getUserEmail(), userCompany)

        for eventId in events:
            eventId = str(eventId)

            firstName = form.get('firstName')
            lastName = form.get('lastName')
            email =  form.get('email')
            telephone =  form.get('telephone')
            booth =  form.get('booth'+eventId)
            tables =  form.get('tables'+eventId)
            chairs =  form.get('chairs'+eventId)
            technicalLecture =  form.get('technicalLecture'+eventId)
            technicalLectureTitle = form.get('technicalLectureTitle'+eventId)
            technicalLectureDuration = form.get('technicalLectureDuration'+eventId)

            if (technicalLecture):
                self.lectureRepository.insert(
                    [
                        {
                            'user': self.userService.getUserUid(),
                            'first_name': firstName,
                            'last_name': lastName,
                            'event': eventId,
                            'status': 1,
                            'email': email,
                            'telephone': telephone,
                            'topic': technicalLectureTitle,
                            'duration': technicalLectureDuration
                        }
                    ]
                )

            if (booth):
                self.boothRepository.insert(
                    [
                        {
                            'user': self.userService.getUserUid(),
                            'first_name': firstName,
                            'last_name': lastName,
                            'event': eventId,
                            'status': 1,
                            'email': email,
                            'telephone': telephone,
                            'table_count': tables,
                            'chair_count': chairs
                        }
                    ]
                )

    def getAll(self):
        return self.eventRepository.getAll()

    def getById(self, uid):
        return self.eventRepository.getById(uid)
    
    def deleteById(self, uid):
        self.eventRepository.deleteById(uid)