import hashlib, os, binascii

import mysql.connector

from mysql.connector import Error

import html

import pandas as pd
import pymysql




class BackEndInterface:

    def __init__(self, filename, debug=False):
        mysql_connection = pymysql.connect(host='localhost', user='root',password='cs205',db='205final',charset='utf8',cursorclass= pymysql.cursors.DictCursor)
        self.connection = mysql_connection
        self.connections = []
        self.connections.append(mysql_connection)

        self.currentTerminal = mysql_connection.cursor()
 

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
                                         ImageLocation varchar(255),
                                         PRIMARY KEY (FileID)
                                         );"""
        try:
            self.currentTerminal = self.connections[0].cursor()
            print("updated the current terminal")
            self.currentTerminal.execute(MySQL_Create_File_Table)
            self.connections[0].commit()


        except Error as e:

            print(e)



    def createRowAssetTable(self, FileName, FileDescription):

       FileLocation = "static/" + FileName
        FileImageLocation = "static/Images/"+ FileName #support for images not available currently


        try:

            MySQL_Create_Row_Asset = """INSERT INTO ASSETS (FileName, FileLocation, FileDescription, ImageLocation) VALUES (%s, %s, %s, %s)"""

            dataAsset = (FileName, FileLocation, FileDescription, FileImageLocation)

    

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

        query = """SELECT * FROM ASSETS LIMIT """ + str(x)

        try:

            self.currentTerminal = self.connections[0].cursor()

            print("updated the current terminal")

            assets = pd.read_sql(query, self.connection)

            print(assets)
            print()

            fileInfo = assets.values.tolist()
            print(fileInfo)


            
            
            return fileInfo

        except Error as e:

            print(e)


    def selectAssetToDownload(self, AssetName):

        MySQL_Asset_Download = """SELECT FileLocation FROM ASSETS WHERE FileName=%s"""
        dataCommand = (AssetName)

        try:
            self.currentTerminal = self.connections[0].cursor()
            print("Updated the current terminal")
            assetLocation = self.currentTerminal.execute(MySQL_Asset_Download, dataCommand)
            return assetLocation
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


    def verifyUser(self, userEmail, userPassword):
        # This function assumes that no two of the same email will be allowed

        MySQL_Verify_User = """SELECT Password FROM USERS WHERE Email='""" + str(userEmail) + """'"""
        print(MySQL_Verify_User)


        try:

            self.currentTerminal = self.connections[0].cursor()

            print("attempting to find user from terminal")


            password = self.currentTerminal.execute(MySQL_Verify_User, userEmail)

            return self.passwordVerify(password, userPassword)

            password = pd.read_sql(MySQL_Verify_User, self.connection)
            print(password)
            passwordFinal = password.values.to_list()
            print(passwordFinal)

            if isUser(userEmail):

                return passwordVerify(str(passwordFinal[0]), userPassword)

            else:
                return False


        except Error as e:
            print(e)


    def signUser(self, userEmail, username, userPassword):
        # Sanitize input here
        s = html.escape("""& < " ' >""")  # s = '&amp; &lt; &quot; &#x27; &gt;'

        MySQL_Find_User = """SELECT username FROM USERS WHERE Email=%s"""

        try:

            if self.verifyUser(userEmail, userPassword):
                return False
            else:
                self.createrowUser(userEmail, username, self.passwordSaltHash(userPassword))

    def isUser(self, userEmail):
         MySQL_Check_User = """SELECT Password FROM USERS WHERE Email='""" + str(userEmail) + """'"""
         print(MySQL_Check_User)

         try:
             self.currentTerminal = self.connections[0].cursor()

             print("Searching for user")

             result = self.currentTerminal.execute(MySQL_Check_User)

             if result == 0:
                 print("User desn't exist. isUser returns False")
                 return False
             else:
                 print("User exists. isUser returns True")
                 return True
         except Exception as e:
             print(e)

    def signUser(self, username, userPassword, userEmail):

        try:

            if self.isUser(userEmail):
                print("USER ALREADY EXISTS")
                return False
            else:
                print("CREATING USER")
                self.createrowUser(username, self.passwordSaltHash(userPassword), userEmail)

                return True

        except Error as e:
            print(e)

    def sanitizeInput(self, input):
        # Transform input to lowercase
        input = input.lower()

        DANGER_STRINGS = ["delete", "insert", "update", "select"]

