from validator.baseValidator import BaseValidator



class RegisterForEventValidator(BaseValidator):
    def validateFirstName(self, value, errors:dict):
        valueKey="firstName"

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE
    
    def validateLastName(self, value, errors:dict):
        valueKey="lastName"

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE

    def validateEmail(self, value, errors:dict):
        valueKey="email"

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE

        if (not self.validateAsEmail(value)):
            errors[valueKey] = self.IS_NOT_EMAIL_ERROR_MESSAGE

    def validateTelephone(self, value, errors:dict):
        valueKey="telephone"

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE

        if (not self.validateAsNumber(value)):
            errors[valueKey] = self.IS_NOT_NUMMBER_ERROR_MESSAGE
    
    def validateFax(self, value, errors:dict):
        valueKey="fax"

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE

        if (not self.validateAsNumber(value)):
            errors[valueKey] = self.IS_NOT_NUMMBER_ERROR_MESSAGE

    def validateTables(self, value, errors:dict, eventId):
        valueKey="tables"+eventId

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE

        if (not self.validateAsNumber(value)):
            errors[valueKey] = self.IS_NOT_NUMMBER_ERROR_MESSAGE

    def validateChairs(self, value, errors:dict, eventId):
        valueKey="chairs"+eventId

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE

        if (not self.validateAsNumber(value)):
            errors[valueKey] = self.IS_NOT_NUMMBER_ERROR_MESSAGE

    def validateTechnicalLectureTitle(self, value, errors:dict, eventId):
        valueKey="technicalLectureTitle"+eventId

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE

    def validateTechnicalLectureDuration(self, value, errors:dict, eventId):
        valueKey="technicalLectureDuration"+eventId

        if (not self.validateAsNotEmpty(value)):
            errors[valueKey] = self.IS_EMPTY_ERROR_MESSAGE

        if (not self.validateAsNumber(value)):
            errors[valueKey] = self.IS_NOT_NUMMBER_ERROR_MESSAGE


    



    
    