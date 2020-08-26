from flask import Flask, request,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/theatre'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

theatresmovies = db.Table('theatres_movies',
                          db.Column('tid',db.ForeignKey('theatre.thet_id'),primary_key=True),
                          db.Column('mid', db.ForeignKey('movie.mov_id'),primary_key=True)
                          )
theatreaddress = db.Table('theatre_address',
                          db.Column('tid',db.ForeignKey('theatre.thet_id'),primary_key=True),
                          db.Column('aid',db.ForeignKey('address.adr_id'),primary_key=True))


class Theatre(db.Model):
    thetId = db.Column('thet_id',db.Integer(),primary_key=True)
    thetName = db.Column('thet_name',db.String(50))
    thetGrade = db.Column('thet_grade',db.String(30))
    active = db.Column('thet_active',db.String(50),default="Y")
    movies = db.relationship('Movie',secondary= theatresmovies, backref=db.backref('theatres', lazy=True))
    adrrefs = db.relationship('Address',secondary= theatreaddress,backref=db.backref('theaters', lazy=True))

    @staticmethod
    def dummy_theatre():
        return Theatre(thetId='',thetName='',thetGrade='')

    @staticmethod
    def get_theater(th):
        th_json = th.__dict__
        if th_json.__contains__('_sa_instance_state'):
            th_json.pop('_sa_instance_state')
        return th_json


class Movie(db.Model):
    movId = db.Column('mov_id',db.Integer(),primary_key=True)
    movName = db.Column('mov_name',db.String(50))
    movFare = db.Column('mov_fare',db.Float())
    movRating = db.Column('mov_rating', db.String(50))
    active = db.Column('mov_active',db.String(30),default='Y')

    @staticmethod
    def dummy_movie():
        return Movie(movId='',movName='',movFare='',movRating='')


    @staticmethod
    def get_movie(mov):
        mov_json = mov.__dict__
        if mov_json.__contains__('_sa_instance_state'):
            mov_json.pop('_sa_instance_state')
        return mov_json



class Address(db.Model):
    adrId = db.Column('adr_id',db.Integer(),primary_key=True)
    adrCity = db.Column('adr_city',db.String(50))
    adrPin = db.Column('adr_pin',db.Integer())
    active = db.Column('adr_active',db.String(30),default='Y')

    @staticmethod
    def dummy_address():
        return Address(adrId='',adrCity='',adrPin='')

    @staticmethod
    def get_city(cit):
        cit_json = cit.__dict__
        if cit_json.__contains__('_sa_instance_state'):
            cit_json.pop('_sa_instance_state')
        return cit_json








if __name__ == '__main__':
    db.create_all()