from flask import Flask, request,render_template
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bookmyshow'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)



class Customer(db.Model):
    custId = db.Column('cust_id',db.Integer(), primary_key=True )
    custFname = db.Column('cust_fname',db.String(50))
    custLname = db.Column('cust_lname',db.String(50))
    custContact = db.Column('cust_contact',db.BigInteger())
    custEmail = db.Column('cust_email',db.String(50))
    active = db.Column('cust_active',db.String(50),default='Y')
    authref = db.relationship('Login',backref='custref',lazy=True,uselist=False)

    @staticmethod
    def cust_instance():
        return Customer(custId='',custFname='',custLname='',custContact='',custEmail='')

class Login(db.Model):
    loginId = db.Column('login_id',db.Integer(),primary_key=True)
    username = db.Column('user_name',db.String(50),unique=True)
    password = db.Column('pass_word',db.String(50))
    cid = db.Column('cust_id',db.ForeignKey('customer.cust_id'),unique=True,nullable=False)

    @staticmethod
    def dummy_login():
        return Login(loginId='',username='',password='')





if __name__ == '__main__':
    db.drop_all()
    db.create_all()
