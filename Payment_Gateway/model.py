from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:root@localhost/paymentgate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


class Customer(db.Model):
    custAccNo = db.Column('cust_accno',db.Integer(), primary_key=True )
    custFname = db.Column('cust_fname',db.String(50))
    custLname = db.Column('cust_lname',db.String(50))
    custContact = db.Column('cust_contact',db.BigInteger())
    custEmail = db.Column('cust_email',db.String(50))
    custAccType = db.Column('cust_acctype',db.String(50))
    custAccBal = db.Column('cust_accbal',db.Float())
    active = db.Column('cust_active',db.String(50),default='Y')
    bid = db.Column('bank_id', db.ForeignKey('bank.bank_id'),unique=False)

    @staticmethod
    def dummy_cust():
        return Customer(custAccNo='',custFname='',custLname='',custContact='',custEmail='',custAccType='',custAccBal='')

class Bank(db.Model):
    bankId = db.Column('bank_id',db.Integer(),primary_key=True)
    bankName = db.Column('bank_name',db.String(50))
    active = db.Column('bank_active',db.String(30),default='Y')
    custs = db.relationship(Customer,backref='bankref',lazy=True,uselist=True)

    @staticmethod
    def dummy_bank():
        return Bank(bankId='',bankName='')


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    b1 = Bank(bankId=111,bankName='State Bank Of India')
    b2 = Bank(bankId=112,bankName='Bank of Maharashtra')
    b3 = Bank(bankId=113,bankName='Union Bank Of India')
    b4 = Bank(bankId=114,bankName='Punjab National Bank')
    b5 = Bank(bankId=115,bankName='ICICI Bank')
    b6 = Bank(bankId=116,bankName='HDFC Bank')
    b7 = Bank(bankId=117,bankName='Central Bank Of India')
    b8 = Bank(bankId=118,bankName='Bank Of India')
    b9 = Bank(bankId=119,bankName='United Bank Of India')
    b10 = Bank(bankId=110,bankName='Corporation Bank Of India')
    db.session.add_all([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10])
    db.session.commit()