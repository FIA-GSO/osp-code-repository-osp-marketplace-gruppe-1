import mysql.connector

class BaseRepository:
    table_name = ""

    def __init__ (self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            port=3306,
            database = "osp"
        )

        self.cursor = self.connection.cursor(dictionary=True)

    def getById (self, id: int):
        return

    def getAll(self):
        self.cursor.execute('SELECT * FROM ' + self.table_name)
        return self.cursor.fetchall()
    
    def deleteById(self):
        return
    

    def updateById(self, id: int, field: list):
        """updates fields in database
        
        fields:
        example of field array:
            [
                {"fieldName": NewFieldValue},
                {"fieldName2": NewFieldValue2},
            ]
        """
        return
    
    def insert(self, fields: list):
        """insterts fields in database
        
        fields:
        example of field array:
            [
                {"fieldName": NewFieldValue},
                {"fieldName2": NewFieldValue2},
            ]
        """
        return
    