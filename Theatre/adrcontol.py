from Ticket_Booking_app.Theatre.model import *



@app.route('/address/save/', methods=['GET','POST'])
def address_save_edit():
    msg = ''
    if request.method=='POST':
        reqform = request.form
        adr = Address.query.filter(Address.adrId==reqform['aid'],Address.active=='Y').first()
        if adr:
            adr.adrCity=reqform['city']
            adr.adrPin=reqform['pin']
            db.session.commit()
            msg = 'Address Updated Successfully...!'
        else:
            adr = Address(adrId=reqform['aid'], adrCity=reqform['city'],adrPin=reqform['pin'])
            db.session.add(adr)
            db.session.commit()
            msg = 'Address Added Successfully...!'
        return render_template('address.html', resp=msg,adr = Address.dummy_address(),
                               adrs= Address.query.filter(Address.active=='Y').all())

    return render_template('address.html', resp=msg, adr=Address.dummy_address(),
                           adrs=Address.query.filter(Address.active == 'Y').all())





@app.route('/address/edit/<int:aid>', methods=['GET','POST'])
def address_edit(aid):
    return render_template('address.html',adr=Address.query.filter(Address.adrId==aid,Address.active=='Y').first(),
                           adrs=Address.query.filter(Address.active == 'Y').all())

@app.route('/address/delete/<int:aid>', methods=['GET','POST'])
def address_delete(aid):
    adr =Address.query.filter(Address.adrId==aid,Address.active=='Y').first()
    adr.active='N'
    db.session.commit()
    msg='Address Deleted Successfully...!'
    return render_template('address.html', resp= msg, adr=Address.dummy_address(),
                           adrs=Address.query.filter(Address.active == 'Y').all())


if __name__ == '__main__':
    app.run(debug=True)