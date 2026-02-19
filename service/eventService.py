from repository.eventRepository import EventRepository


class EventService:
    def __init__(self):
        self.eventRepository = EventRepository()
        pass