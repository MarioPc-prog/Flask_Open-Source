import hashlib, os, binascii

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

    def disconnectFromServer(self):
        try:
            self.connections[0].close()
            print("The connection has closed")
        except Error as e:
            print(e)

    def createrowUser(self, username, password, email):
        try:

            MySQL_Create_Row_Users = "INSERT INTO USERS(UserName, Password, Email) VALUES (%s, %s, %s)"

            self.currentTerminal = self.connections[0].cursor()
            print("updated the current terminal")

            dataUser = (username, password, email)

            # dataUser=("Derek","derek123", "derek@uvm.edu")

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

        MySQL_Create_File_Table = """CREATE TABLE ASSETS (
                                         FileID int NOT NULL AUTO_INCREMENT,
                                         FileName varchar(255) NOT NULL,
                                         FileLocation varchar(255) NOT NULL,
                                         FileDescription varchar(255) NOT NULL,
                                         PRIMARY KEY (FileID)
                                         );"""
        try:
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

    def deleteRowAsset(self, filename):

        MySQL_Delete_Asset = """DELETE FROM ASSETS WHERE FileName=%s"""

        dataCommand = (filename)

        try:

            self.currentTerminal = self.connections[0].cursor()

            print("updated the current terminal")

            self.currentTerminal.execute(MySQL_Delete_Asset, dataCommand)

            self.connections[0].commit()


        except Error as e:

            print(e)

    def selectXfromAssets(self, x):

        MySQL_Select_X_Assets = """SELECT * FROM ASSETS"""
        dataCommand = (x, x + 1)

        try:

            self.currentTerminal = self.connections[0].cursor()

            print("updated the current terminal")

            assets = self.currentTerminal.execute(MySQL_Select_X_Assets, dataCommand)
            return assets

        except Error as e:

            print(e)

    def passwordSaltHash(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        passwordHash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        passwordHash = binascii.hexlify(passwordHash)

        return (salt + passwordHash).decode('ascii')

    def passwordVerify(self, stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)

        pwdhash = binascii.hexlify(pwdhash).decode('ascii')

        return pwdhash == stored_password


    def findUser(self, userEmail):
        # This function assumes that no two of the same email will be allowed

        MySQL_Find_User = """SELECT username, password FROM USERS WHERE Email=%s"""

        try:

            self.currentTerminal = self.connections[0].cursor()

            print("attempting to find user from terminal")

            username, password = self.currentTerminal.execute(MySQL_Find_User, userEmail)

            if password != "" and username != "":
                # User exists
                return username, password

            else:
                print("User not found")


        except Error as e:
            print(e)