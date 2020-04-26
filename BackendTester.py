
from flask import Flask

from backEnd import BackEndInterface
from mysql.connector import Error

# create app object

global app

app = Flask(__name__)

serverInterface = BackEndInterface("205final")
serverInterface.connectToServer()
# register the Blueprint by importing and registering

from flask import Blueprint, render_template, request



# create the first grouping for the blueprint


@app.route('/')

def home():

#    try:
#        serverInterface.connectToServer()
#        print("No error while connecting")
#    except:
#        print("there was an error connecting")
    #return "<h1>This is Backend Tester Code</h1>"
    return testSelectID()



@app.route('/CreateRow')

def testCreateUserRow():
    try:
        serverInterface.createrowUser("Derek","derek123", "derek@uvm.edu")
        print(serverInterface.currentTerminal)
        print("Check User Table for Charlie")
    except Error as e:
        print(e)
    return "<h1>Check the Database</h1>"

@app.route('/CreateAsset')
def testCreateAsset():
    try:
        serverInterface.createFileTable()
        print(serverInterface.currentTerminal)
    except Error as e:
        print(e)
    return "<h1>Check that the table has been created</h1>"

@app.route('/CreateRow2')
def testCreateAssetRow():
    try:
        serverInterface.createRowAssetTable("TestFile1","../Testfile1.txt", "A Testing File")
        print(serverInterface.currentTerminal)
    except Error as e:
        print(e)
    return "<h1>Check that the row has been created</h1>"


@app.route('/DeleteRow')
def testDeleteUserRow():
    try:
        serverInterface.deleteRowUser("Derek", "derek123")
        print(serverInterface.currentTerminal)
    except Error as e:
        print(e)
    return "<h1>Check that the row has been created</h1>"


@app.route('/SelectX')
def testSelectX():

    try:
        serverInterface.selectXfromAssets(1)
        print(serverInterface.currentTerminal)
    except Error as e:
        print(e)
    return "<h1>Check the terminal for output</h1>"

@app.route('/SelectID')
def testSelectID():

    try:
        serverInterface.getUserID('bcaruso@uvm.edu')
        print(serverInterface.currentTerminal)
    except Error as e:
        print(e)
    return "<h1>Check the terminal for output</h1>"

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=80)

