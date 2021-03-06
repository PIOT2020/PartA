from flask import Flask,Blueprint
import requests

site = Blueprint("site", __name__)
url = "http://220.244.177.218:5000/"


@site.route('/register')
def siteregister():
    response = requests.post((url+"api/register"), params={
        'type' : "customer",
        'username' : "seth", 
        'password' : "testing", 
        'fistname' : "angelo", 
        'lastname' : "parlade", 
        'email' : "angelo.parlade@gmail.com"
    })

    return response.text

@site.route('/login')
def sitelogin():
    param = {
        'username' : "seth", 
        'password' : "testing"
    }
    response = requests.get((url+"api/login"), params=param)

    return response.text

@site.route('/populate')
def populate():
    response = requests.get((url+"api/populateCars"))

    return response.text

@site.route('/getAvailableCars')
def availableCars():
    response = requests.get((url+"api/availableCars"), params={
        'username' : "seth", 
        'password' : "testing", 
    })
    return response.text

@site.route('/book')
def booking():
    response = requests.post((url+"api/book"), params={
        'username' : "seth", 
        'password' : "testing", 
        'carid' : "1", 
    })
    return response.text

@site.route('/history')
def history():
    response = requests.get((url+"api/bookingHistory"), params={
        'username' : "seth", 
        'password' : "testing", 
    })
    return response.text

@site.route('/cancel')
def cancel():
    response = requests.put((url+"api/cancelBooking"), params={
        'username' : "seth", 
        'password' : "testing", 
        'bookingid' : "11"
    })
    return response.text
