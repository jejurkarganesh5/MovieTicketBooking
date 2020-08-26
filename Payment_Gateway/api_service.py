import requests,json
from Ticket_Booking_app.Payment_Gateway.model import *
from Ticket_Booking_app.Payment_Gateway.custbankcontrol import *

@app.route('/service/banks/',methods=['GET'])
def get_all_banks():
    banks = Bank.query.all()
    listOfBanks = []
    for bank in banks:
        if bank.__dict__.get('_sa_instance_state'):
            bank.__dict__.pop('_sa_instance_state')
            listOfBanks.append(bank.__dict__)
    return json.dumps(listOfBanks)


@app.route("/bank/service/",methods=['POST'])
def withdraw_amount():
    reqbody = request.get_json()
    print(reqbody)
    banknm = reqbody['bank']
    mobile = reqbody['mobile']
    amount = reqbody['amount']
    bank = Bank.query.filter(Bank.bankName==banknm).first()
    customer = Customer.query.filter(Customer.custContact == mobile).first()
    if not bank:
        return json.dumps({"Status": "Invalid Bank.....!"})

    elif not customer:
        return json.dumps({"Status": "Mobile is not associated with bank acount...!"})

    elif customer.bankref.bankName==banknm and customer.custContact==mobile:
        customer.custAccBal -= amount
        db.session.commit()
        return json.dumps({"Status": "Ticket Booked Successfull...!"})

    return json.dumps({"Status": "Invalid Details"})


if __name__ == '__main__':
    app.run(debug=True, port=5001)