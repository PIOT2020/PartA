from flask import Flask,Blueprint,request
from datetime import date
from database_utils import DatabaseUtils
import MySQLdb
from passlib.hash import sha256_crypt

def encrypt(password):
    hashedPassword = sha256_crypt.using(salt="salting").hash(password)
    print(hashedPassword)
    hashedPassword = hashedPassword[:-4]
    print(hashedPassword)
    return hashedPassword

api = Blueprint("api", __name__)
db = DatabaseUtils()

@api.route('/api/returnCar',methods=['GET'])
def returnCar():
    prams = [
        request.args.get('username'),
        encrypt(request.args.get('password')),
        "placeholderuserid",
        request.args.get('carid')
    ]

    if None in prams:
        print("Missing Parameters")
        return "Missing Parameters"

    if db.getUser2(prams):
        prams[2] = db.getUserID2(prams)
        if db.checkBooking(prams):
            return str(db.returnCar(prams))
        else:
            return "No Booking Found"
    else:
        print("Not Authenticated")
        return "Not Authenticated"

@api.route('/api/findBooking',methods=['GET'])
def findBooking():
    prams = [
        request.args.get('username'),
        encrypt(request.args.get('password')),
        "placeholderuserid",
        request.args.get('carid')
    ]

    if None in prams:
        return "Missing Parameters"

    if db.getUser(prams):
        prams[2] = db.getUserID(prams)
        return str(db.findBooking(prams))
    else:
        return "Not Authenticated"

@api.route('/api/findBooking2',methods=['GET'])
def findBooking2():
    prams = [
        request.args.get('username'),
        encrypt(request.args.get('password')),
        "placeholderuserid",
        request.args.get('carid')
    ]
    if None in prams:
        return "Missing Parameters"

    if db.getUser2(prams):
        prams[2] = db.getUserID2(prams)
        return str(db.findBooking(prams))
    else:
        return "Not Authenticated"

@api.route('/api/cancelBooking',methods=['PUT'])
def cancel():
    prams = [
        request.args.get('username'),
        encrypt(request.args.get('password')),
        request.args.get('bookingid')
    ]
    print(request.args.get('bookingid'))
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
        encrypt(request.args.get('password'))
    ]
    if db.getUser(prams):
        print(type(db.bookingHistory(db.getUserID(prams))))

        results = db.bookingHistory(db.getUserID(prams))

        for x in results:
            temp = x.get("date")
            print(str(temp))
            x["date"] = str(temp)

        return str(results)
    else:
        return "Not Authenticated"
    

@api.route('/api/register',methods=['POST'])
def register():
    prams = [
        request.args.get('type'),
        request.args.get('username'),
        encrypt(request.args.get('password')),
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
        encrypt(request.args.get('password'))
    ] 
    if None in prams:
        return "Missing Parameters"

    if db.getUser(prams):
        return "User Exists"

    return "No Such User"

@api.route('/api/availableCars',methods=['GET'])
def getAvailableCars():
    results = db.availableVehicles()

    for x in results:
        temp = x.get("latitude")
        x["latitude"] = str(temp)

        temp = x.get("longitude")
        x["longitude"] = str(temp)

    return str(results)


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
        encrypt(request.args.get('password')),
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
        1,
        -37.804815, 
        144.955400
    ] 
    car2 = [
        "Toyota",
        "Pickup Truck",
        "Black",
        5,
        40,
        1,
        -37.808189, 
        144.956076
    ] 
    car3 = [
        "Ford",
        "SUV",
        "White",
        7,
        80,
        1,
        -37.807485, 
        144.948019
    ] 

    db.addVehicle(car1)
    db.addVehicle(car2)
    db.addVehicle(car3)
    
    return "Done Populating"



