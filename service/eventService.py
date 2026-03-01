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

        if donation:
            self.userRepository.updateById(
                self.userService.getUserUid(),
                [
                    {
                        'donation': donation
                    }
                ]
            )

        for eventId in events:
            eventId = str(eventId)

            firstName = form.get('firstName')
            lastName = form.get('lastName')
            email =  form.get('email')
            telephone =  form.get('telephone')
            fax =  form.get('fax')
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
                            'fax': fax,
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
                            'fax': fax,
                            'table_count': tables,
                            'chair_count': chairs
                        }
                    ]
                )