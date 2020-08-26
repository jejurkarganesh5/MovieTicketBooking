from Ticket_Booking_app.Payment_Gateway.model import *




@app.route('/bank/cust/save/', methods=['GET','POST'])
def cust_bank_save():
    msg = ''
    if request.method=='POST':
        rqform=request.form
        cust = Customer(custAccNo=rqform['acno'],custFname=rqform['fnm'],custLname=rqform['lnm'],
                        custContact=rqform['mob'],custEmail=rqform['email'],custAccType=rqform['actyp'],custAccBal=rqform['bal'])
        cust.bid=rqform['bnk']
        db.session.add(cust)
        db.session.commit()
        msg = 'Account Added Sucessfully'
        return render_template('cust.html', resp = msg, cust=Customer.dummy_cust(),banks= Bank.query.filter(Bank.active=='Y').all(),
                               custs= Customer.query.filter(Customer.active=='Y').all())
    return render_template('cust.html', resp=msg, cust=Customer.dummy_cust(),
                           banks=Bank.query.filter(Bank.active == 'Y').all(),
                           custs=Customer.query.filter(Customer.active == 'Y').all())


if __name__ == '__main__':
    app.run(debug=True)