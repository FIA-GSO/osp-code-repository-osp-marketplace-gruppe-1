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

    def getById (self, id: int, respectDisabled:bool = True):
        sql = 'SELECT * FROM ' + self.table_name + ' WHERE'
        if respectDisabled:
            sql += ' disabled = 0'

        sql += ' AND uid = %s'
        print(sql)
        self.cursor.execute(sql, (id,))
        return self.cursor.fetchall()

    def getAll(self, respectDisabled:bool = True):
        sql = 'SELECT * FROM ' + self.table_name
        if respectDisabled:
            sql += ' WHERE disabled = 0'

        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def deleteById(self, id: int):
        sql = 'UPDATE ' + self.table_name + ' SET disabled = true WHERE uid = ' + str(id)
        self.cursor.execute(sql)
        self.connection.commit()
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

        self.cursor.execute(sql)
        self.connection.commit()

        columns = []
        values = []

        for field in fields:
            for key, value in field.items():
                columns.append(key)
                values.append(value)

        # Platzhalter für prepared statement
        placeholders = ", ".join(["%s"] * len(values))
        column_names = ", ".join(columns)

        sql = f"""
                INSERT INTO {self.table_name} ({column_names})
                VALUES ({placeholders})
            """

        self.cursor.execute(sql, values)
        self.connection.commit()

        return self.cursor.lastrowid
    
    def insert(self, fields: list):
        """inserts fields in database

        fields:
        example of field array:
            [
                {"fieldName": NewFieldValue},
                {"fieldName2": NewFieldValue2},
            ]
        """

        keys = []
        values = []

        for field in fields:
            for key, value in field.items():
                keys.append(key)
                values.append(value)

        placeholders = ", ".join(["%s"] * len(values))  # sqlite: ?, postgres/mysql: %s

        sql = f"""
                INSERT INTO {self.table_name} ({', '.join(keys)})
                VALUES ({placeholders})
            """

        self.cursor.execute(sql, values)
        self.connection.commit()
    