from validator.registerForEventValidator import RegisterForEventValidator
from service.userService import UserService

class ValidatorService:

    def __init__(self):
        super().__init__()
        self.registerForEventValidator = RegisterForEventValidator()

    def validateRegisterForEventForm(self, form, errors:dict):
        events =  form.getlist('events[]')
        firstName = form.get('firstName')
        lastName = form.get('lastName')
        email =  form.get('email')
        telephone =  form.get('telephone')
        fax =  form.get('fax')

        self.registerForEventValidator.validateFirstName(firstName, errors)
        self.registerForEventValidator.validateLastName(lastName, errors)
        self.registerForEventValidator.validateEmail(email, errors)
        self.registerForEventValidator.validateTelephone(telephone, errors)
        self.registerForEventValidator.validateFax(fax, errors)

        for eventId in events:
            eventId = str(eventId)

            booth =  form.get('booth'+eventId)
            tables =  form.get('tables'+eventId)
            chairs =  form.get('chairs'+eventId)
            technicalLecture =  form.get('technicalLecture'+eventId)
            technicalLectureTitle = form.get('technicalLectureTitle'+eventId)
            technicalLectureDuration = form.get('technicalLectureDuration'+eventId)

            if (technicalLecture):
                self.registerForEventValidator.validateTechnicalLectureTitle(technicalLectureTitle, errors, eventId)
                self.registerForEventValidator.validateTechnicalLectureDuration(technicalLectureDuration, errors, eventId)

            if (booth):
                self.registerForEventValidator.validateTables(tables, errors, eventId)
                self.registerForEventValidator.validateChairs(chairs, errors, eventId)
