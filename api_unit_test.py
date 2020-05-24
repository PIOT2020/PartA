import unittest
import requests

url = "http://220.244.177.218:5000/"

class TestStringMethods(unittest.TestCase):

    def test_register(self):
        response = requests.post((url+"api/register"), params={
            'type' : "customer",
            'username' : "seth", 
            'password' : "testing", 
            'fistname' : "angelo", 
            'lastname' : "parlade", 
            'email' : "angelo.parlade@gmail.com"
        })
        self.assertEqual(response.text, "Sucessful Register")

    def test_login(self):
        param = {
            'username' : "seth", 
            'password' : "testing"
        }
        response = requests.get((url+"api/login"), params=param)

        self.assertEqual(response.text, "User Exists")

    def test_listAvailableCars(self):
        response = requests.get((url+"api/availableCars"), params={
            'username' : "seth", 
            'password' : "testing", 
        })

        self.assertTrue(response.text != "()")

    def test_booking(self):
        response = requests.post((url+"api/book"), params={
            'username' : "seth", 
            'password' : "testing", 
            'carid' : "1", 
        })

        self.assertEqual(response.text, True)

    def test_bookingHistory(self):
        response = requests.get((url+"api/bookingHistory"), params={
            'username' : "seth", 
            'password' : "testing", 
        })
        self.assertTrue(response.text != "()")

    def test_cancelBooking(self):
        response = requests.put((url+"api/cancelBooking"), params={
            'username' : "seth", 
            'password' : "testing", 
            'bookingid' : "11"
        })

        self.assertEqual(response.text, True)

if __name__ == '__main__':
    unittest.main()