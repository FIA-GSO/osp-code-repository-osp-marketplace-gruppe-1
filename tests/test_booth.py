import unittest
from repository.boothRepository import BoothRepository
from service.boothService import BoothService
from service.eventService import EventService

class test_booth(unittest.TestCase):

    boothRepository = BoothRepository()
    boothService = BoothService()
    eventService = EventService()

    def test_add_booth(self):
        self.eventService.registerForEvent()

if __name__ == "__main__":
    unittest.main()
