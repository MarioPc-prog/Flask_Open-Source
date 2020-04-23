

import mysql.connector

from mysql.connector import Error


class BackEndInterface:


    def __init__(self, filename, debug=False):

        self.degub = debug

        self.connections = []

        self.databaseName = filename

        self.currentTerminal = 0


    def connectToServer(self):

        username = "root"

        password = "cs205"


        try:

            newconnection = mysql.connector.connect(host='localhost',

                                                 database='205final',

                                                 user=username,

                                                 password=password)

            self.connections.append(newconnection)
            print("made the connection")

            self.currentConnection = newconnection

            self.currentTerminal = newconnection.cursor()
            print("updated current terminal")
            print(self.currentTerminal)

        except Error as e:

            print("Error while connecting to MySQL", e)


        return ("You're connected to database", self.currentTerminal.fetchone())


    def createrowUser(self, username, password, email):
        try:

            MySQL_Create_Row_Users = "INSERT INTO USERS(UserName, Password, Email) VALUES (%s, %s, %s)"

            self.currentTerminal = self.connections[0].cursor()
            print("updated the current terminal")

            dataUser = (username, password, email)

            #dataUser=("Derek","derek123", "derek@uvm.edu")

            self.currentTerminal.execute(MySQL_Create_Row_Users, dataUser)


            self.connections[0].commit()

        except Error as e:

            print(e)


    def deleteRowUser(self, username, password):
        MySQL_Delete_User = """DELETE FROM USERS WHERE UserName=%s AND Password=%s"""
        dataCommand = (username, password)
        try:
            self.currentTerminal = self.connections[0].cursor()
            print("updated the current terminal")
            self.currentTerminal.execute(MySQL_Delete_User, dataCommand)
            self.connections[0].commit()

        except Error as e:
            print(e)


    def createFileTable(self):

        try:

            MySQL_Create_File_Table = """CREATE TABLE ASSETS (

                                         FileID int NOT NULL AUTO_INCREMENT,

                                         FileName varchar(255) NOT NULL,

                                         FileLocation varchar(255) NOT NULL,

                                         FileDescription varchar(255) NOT NULL,

                                         PRIMARY KEY (FileID)

                                         );"""

            self.currentTerminal = self.connections[0].cursor()

            print("updated the current terminal")

    

            self.currentTerminal.execute(MySQL_Create_File_Table)

    

            self.connections[0].commit()


        except Error as e:

            print(e)


    def createRowAssetTable(self, FileName, FileLocation, FileDescription):

        try:

            MySQL_Create_Row_Asset = """INSERT INTO ASSETS (FileName, FileLocation, FileDescription) VALUES (%s, %s, %s)"""

            

            dataAsset = (FileName, FileLocation, FileDescription)

            

            self.currentTerminal = self.connections[0].cursor()

            print("updated the current terminal")

            self.currentTerminal.execute(MySQL_Create_Row_Asset, dataAsset)

            self.connections[0].commit()

        except Error as e:

            print(e)
