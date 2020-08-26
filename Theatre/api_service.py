import requests,json
from Ticket_Booking_app.Theatre.model import *

BASE_URI="/theater/api/"


@app.route('/service/movies/',methods=['GET'])
def get_all_movies():
    movies = Movie.query.all()
    list_of_Movies = []
    for movie in movies:
        if movie.__dict__.get('_sa_instance_state'):
            movie.__dict__.pop('_sa_instance_state')
            list_of_Movies.append(movie.__dict__)
    return json.dumps(list_of_Movies)


@app.route(BASE_URI+"city/",methods=['GET'])
def fetch_all_cities():
    cites = Address.query.filter(Address.active == 'Y').all()
    all_cities = []
    for city in cites:
        all_cities.append(city.adrCity)
    return json.dumps(all_cities)

@app.route(BASE_URI+"tcity/",methods=['GET','POST'])
def fetch_all_theaters():
    try:
        cityjson = request.get_json()
        print(cityjson)
        adr = Address.query.filter(Address.adrCity == cityjson['tcity']).first()
        if adr:
            theaters = adr.theaters
            all_theaters = []
            for theater in theaters:
                all_theaters.append(theater.thetName)
            return json.dumps(all_theaters)
        else:
            print('No ')

    except:
        pass


@app.route(BASE_URI+"tmov/",methods=['GET','POST'])
def fetch_all_movies():
    try:
        thjson = request.get_json()
        print(thjson)
        th = Theatre.query.filter(Theatre.thetName==thjson['tth']).first()
        if th:
            movies = th.movies
            mydict = dict()
            for mov in movies:

                m1 = Movie.query.filter_by(movId=mov.movId).first()
                mname = str(m1.movName)
                mfare = float(m1.movFare)
                mydict[mname] = mfare
            return json.dumps(mydict)

        else:
            print('No ')

    except:
        pass

import time
if __name__ == '__main__':
    app.run(debug=True, port=5051)



