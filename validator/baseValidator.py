import re

class BaseValidator:
    IS_EMPTY_ERROR_MESSAGE = "Bitte Füllen sie dieses Feld aus"
    IS_NOT_NUMMBER_ERROR_MESSAGE = "Bitte geben sie eine zahl ein"
    IS_NOT_EMAIL_ERROR_MESSAGE = "Bitte geben sie eine Gültige E-Mail adresse ein"


    def validateAsNumber(self, value):
        return str(value.isdigit())
    
    def validateAsNotEmpty(self, value:str):
        if value != "":
            return True
        return False

    def validateAsEmail(self, value):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if re.match(email_pattern, value):
            return True
        return False
    


    