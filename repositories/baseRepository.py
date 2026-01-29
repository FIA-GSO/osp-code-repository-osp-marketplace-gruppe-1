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
        self.cursor.execute('SELECT * FROM ' + self.table_name + 'WHERE uid = ' + id)
        return self.cursor.fetchall()

    def getAll(self):
        self.cursor.execute('SELECT * FROM ' + self.table_name)
        return self.cursor.fetchall()
    
    def deleteById(self):
        return
    

    def updateById(self, id: int, fields: list):
        """updates fields in database
        
        fields:
        example of field array:
            [
                {"fieldName": NewFieldValue},
                {"fieldName2": NewFieldValue2},
            ]
        """

        sql = 'UPDATE ' + self.table_name + ' SET '
        conditions = []


        for field in fields:
            for key, value in field.items():
                conditions.append(key + ' = "' + value + '"')

        sql += ', '. join(conditions)
        sql += ' WHERE uid = ' + str(id)

        print(sql)

        self.cursor.execute(sql)
        self.connection.commit()

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
    