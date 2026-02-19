from repository.eventRepository import EventRepository


class EventService:
    def __init__(self):
        self.eventRepository = EventRepository()
        pass

    def getCurrentEvents(self):
       return self.eventRepository.getAll()

    def registerEvent(self, date: str):
        self.eventRepository.insert(
            [
                {
                    'date': date,
                }
            ]
        )
