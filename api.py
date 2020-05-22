from flask import Flask,Blueprint,request
from datetime import date
from database_utils import DatabaseUtils
import MySQLdb

api = Blueprint("api", __name__)
db = DatabaseUtils()


@api.route('/api/cancelBooking',methods=['PUT'])
def cancel():
    prams = [
        request.args.get('username'),
        request.args.get('password'),
        request.args.get('bookingid'),
        request.args.get('carid')
    ] 
    if None in prams:
        return "Missing Parameters"

    if db.getUser(prams):
        return db.cancelBooking(prams)
    else:
        return "Not Authenticated"

@api.route('/api/bookingHistory',methods=['GET'])
def history():
    prams = [
        request.args.get('username'),
        request.args.get('password')
    ]
    if db.getUser(prams):
        return str(db.bookingHistory(db.getUserID(prams)))
    else:
        return "Not Authenticated"
    

@api.route('/api/register',methods=['POST'])
def register():
    prams = [
        request.args.get('type'),
        request.args.get('username'),
        request.args.get('password'),
        request.args.get('fistname'),
        request.args.get('lastname'),
        request.args.get('email')
    ] 
    if None in prams:
        return "Missing Parameters"

    if db.registerUser(prams):
        return "Sucessful Register"

    return "Registration Error"

@api.route('/api/login',methods=['GET'])
def login():
    prams = [
        request.args.get('username'),
        request.args.get('password')
    ] 
    if None in prams:
        return "Missing Parameters"

    if db.getUser(prams):
        return "User Exists"

    return "No Such User"

@api.route('/api/availableCars',methods=['GET'])
def getAvailableCars():
    return str(db.availableVehicles())


@api.route('/api/carDetails',methods=['GET'])
def getCar():
    prams = [
        request.args.get('carid')
    ] 
    return str(db.getVehicle())

@api.route('/api/book',methods=['POST'])
def bookVehicle():
    prams = [
        request.args.get('username'),
        request.args.get('password'),
        "placeholder",
        request.args.get('carid')
    ] 
    if None in prams:
        return "Missing Parameters"

    if db.getUser(prams):
        prams[2] = db.getUserID(prams)
        return str(db.bookVehicle(prams))
    else:
        return "Not Authenticated"












#For Demo Purposes
#Location parameters left at null
#Need to implement Google MAP API
@api.route('/api/populateCars',methods=['GET'])
def populateCarsTable():
    car1 = [
        "Toyota",
        "Sedan",
        "Gray",
        5,
        20,
        1
    ] 
    car2 = [
        "Toyota",
        "Pickup Truck",
        "Black",
        5,
        40,
        1
    ] 
    car3 = [
        "Ford",
        "SUV",
        "White",
        7,
        80,
        1
    ] 

    db.addVehicle(car1)
    db.addVehicle(car2)
    db.addVehicle(car3)
    
    return "Done Populating"



