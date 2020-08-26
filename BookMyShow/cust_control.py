from Ticket_Booking_app.BookMyShow.cust_model import *




@app.route('/cust/save/', methods=['GET','POST'])
def cust_save_edit():
    msg = ''
    if request.method == 'POST':
        formdata = request.form
        cust = Customer.query.filter(Customer.custId==formdata['cid'],Customer.active=='Y').first()
        if cust:
            cust.custFname=formdata['cfnm']
            cust.custLname=formdata['clnm']
            cust.custContact=formdata['cmob']
            cust.custEmail=formdata['cemail']
            db.session.commit()
            msg = 'Customer Updated Successfully...!'
        else:
            cust = Customer(custId=formdata['cid'],
                     custFname=formdata['cfnm'],
                     custLname=formdata['clnm'],
                     custContact=formdata['cmob'],
                     custEmail=formdata['cemail'])
            log = Login(username=formdata['username'],password=formdata['password'])
            log.cid=cust.custId
            db.session.add(cust)
            db.session.add(log)
            db.session.commit()
            msg = 'Customer Register Successfully...!'

        return render_template('bookMyShowDashboard.html',log=Login.dummy_login(),cust=Customer.cust_instance(),all_cust=Customer.query.filter(Customer.active=='Y').all(),
                               resp = msg)
    return render_template('cust.html', cust=Customer.cust_instance(), log=Login.dummy_login(),
                           all_cust=Customer.query.filter(Customer.active == 'Y').all(),
                           resp=msg)



@app.route('/cust/edit/', methods=['GET'])
def cust_edit(cid):
    return render_template('cust.html',cust=Customer.query.filter(Customer.custId==cid,Customer.active=='Y').first(),
                           all_cust=Customer.query.filter(Customer.active=='Y').all())

