import mysql.connector
from mysql.connector import Error

class BackEndInterface:

    def __init__(self, filename, debug=False):
        self.degub = debug

        self.connection = connectDatabase(filename)


    def loaddatabase(self):
        pass

    def saveDatabase(self):
        pass

    def setdebug(self, debugFlag):
        self.degub = debugFlag


    def getdebug(self):
        return self.degub


    def connectDatabase(self,databaseName):
        username = ""
        password = ""
        try:
            self.connection = mysql.connector.connect(host="localhost", database=databaseName, user=username, password=password)

            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                if self.degub:
                    print("Connected to MySQL database at ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select databse();")
                record = self.cursor.fetchone()
                print("You are connected to database", record)

        except Error as e:
            print(" Error while connecting to MySQL: ", e)

        finally:
            if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")



    def disconnectDatabase(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")



    def searchRowsforUsername(self):
        pass

    def selectallfromtable(self):
        pass

    def createtableUsers(self):
        try:
            MySQL_Create_Table_Users = """CREATE TABLE USERS ( 
                                 Id int(11) NOT NULL,
                                 Name varchar(250) NOT NULL,
                                 Password CHAR(64) NOT NULL,
                                 PRIMARY KEY (Id)) """

            self.cursor = self.connection.cursor()
            result = self.cursor.execute(MySQL_Create_Table_Users)
            if self.degub:
                print("Table for Users Created Successfully")

        except mysql.connector.Error as error:
            print("Failed to create table in MySQL: {}".format(error))

        finally:
            if (self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")


    def createrowUser(self, username, password, email):
        try:

            MySQL_Create_Row_Users = "INSERT INTO 'USERS'('NAME', 'PASSWORD', 'EMAIL') VALUES (%s, %s, %s)"

            self.cursor = self.connection.cursor()
            result = self.cursor.execute(MySQL_Create_Row_Users, (username,password, email))
            if self.degub:
                print("Row added successfully to table USERS")

        except Error as e:
            print(e)

        finally:
            if (self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")

        pass


    def deletedatabase(self):
        pass

    def deletetable(self):
        pass

    def deletecolumn(self):
        pass

    def deleterow(self):
        pass

