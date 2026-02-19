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
    
    def registerForEvent(self, form):
        events =  form.getlist('events[]')

        donation = form('donation')

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

            firstName = form('firstName')
            lastName = form('lastName')
            email =  form('email')
            telefon =  form('telefon')
            fax =  form('fax')
            booth =  form('booth'+eventId)
            tables =  form('tables'+eventId)
            chairs =  form('chairs'+eventId)
            technicalLecture =  form('technicalLecture'+eventId)
            technicalLectureTitle = form('technicalLectureTitle'+eventId)
            technicalLectureDuration = form('technicalLectureDuration'+eventId)


            if (technicalLecture):
                self.lectureRepository.insert(
                    [
                        {
                            'user': self.userService.getUserUid(),
                            'first_name': firstName,
                            'lastName': lastName,
                            'event': eventId,
                            'status': 1,
                            'email': email,
                            'telephone': telefon,
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
                            'lastName': lastName,
                            'event': eventId,
                            'status': 1,
                            'email': email,
                            'telephone': telefon,
                            'fax': fax,
                            'table_count': tables,
                            'chair_count': chairs
                        }
                    ]
                )

                 


