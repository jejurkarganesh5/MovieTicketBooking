import requests,json
from Ticket_Booking_app.BookMyShow.cust_model import *
from Ticket_Booking_app.BookMyShow.cust_control import *
from Ticket_Booking_app.BookMyShow.main_Control import *

BASE_URI="http://localhost:5051/theater/api/"


def json_to_cities(mjsons):
    cities = []
    for mjson in mjsons:
        cities.append(mjson)
    return cities

def fetch_all_cities():
    response= requests.get(BASE_URI+"city/")
    return json_to_cities(response.json())

class Movie:
    def __init__(self,mid,mnm,mfr,mgd):
        self.movid = mid
        self.movnm = mnm
        self.movfare = mfr
        self.movgrade = mgd


def get_all_movie():
    respnose = requests.get('http://localhost:5051/service/movies/')
    print(respnose.json())
    movies = []
    for item in respnose.json():
        #movies.append(item)
        movies.append(Movie(item['movId'],item['movName'],item['movFare'],item['movRating']))
    return movies




class Bank:
    def __init__(self,bid,bnm):
        self.bankid = bid
        self.banknm = bnm


def get_all_bankinfo():
    respnose = requests.get('http://localhost:5001/service/banks/')
    print(respnose.json())
    banks = []
    for item in respnose.json():
        banks.append(Bank(item['bankId'],item['bankName']))
    return banks





import time
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    m = get_all_movie()
    print(m)




