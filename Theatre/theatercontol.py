from Ticket_Booking_app.Theatre.model import *



@app.route('/theater/save/', methods=['GET','POST'])
def theater_save_edit():
    msg = ''
    if request.method=='POST':
        rqform = request.form
        th = Theatre.query.filter(Theatre.thetId==rqform['tid'],Theatre.active=='Y').first()
        if th:
            th.thetName=rqform['tnm']
            th.thetGrade=rqform['tgd']
            th.movies.clear()
            th.adrrefs.clear()
            db.session.commit()
            movids = [int(mid) for mid in rqform.getlist('tmovs')]
            print(movids)
            for mid in movids:
                mov = Movie.query.filter_by(movId=mid).first()
                th.movies.append(mov)
                db.session.commit()
            adrids = [int(aid) for aid in rqform.getlist('tadrs')]
            for aid in adrids:
                adr = Address.query.filter_by(adrId=aid).first()
                th.adrrefs.append(adr)
                db.session.commit()
            msg = 'Theater Upadated Successfully...!'
        else:
            th = Theatre(thetId=rqform['tid'],thetName=rqform['tnm'],thetGrade=rqform['tgd'])
            db.session.add(th)
            db.session.commit()

            movids = [int(mid) for mid in rqform.getlist('tmovs')]
            print(movids)
            for mid in movids:
                mov = Movie.query.filter_by(movId=mid).first()
                th.movies.append(mov)
                db.session.commit()
            adrids = [int(aid) for aid in rqform.getlist('tadrs')]
            for aid in adrids:
                adr = Address.query.filter_by(adrId=aid).first()
                th.adrrefs.append(adr)
                db.session.commit()
            msg = 'Theater Added Successfully...!'

        return render_template('theatre.html',th=Theatre.dummy_theatre(), resp = msg,
                               thtrs=Theatre.query.filter(Theatre.active=='Y').all(),
                               movs = Movie.query.filter(Movie.active=='Y').all(),
                               adrs=Address.query.filter(Address.active=='Y').all())
    return render_template('theatre.html',thtrs=Theatre.query.filter(Theatre.active == 'Y').all(),
                           th=Theatre.dummy_theatre(), resp=msg, movs=Movie.query.filter(Movie.active == 'Y').all(),
                           adrs=Address.query.filter(Address.active == 'Y').all())


@app.route('/theater/edit/<int:tid>', methods=['GET','POST'])
def theater_edit(tid):
    return render_template('theatre.html', th=Theatre.query.filter(Theatre.thetId==tid,Theatre.active=='Y').first(),
                           thtrs=Theatre.query.filter(Theatre.active == 'Y').all(),
                           movs=Movie.query.filter(Movie.active == 'Y').all(),
                           adrs=Address.query.filter(Address.active == 'Y').all())


@app.route('/theater/delete/<int:tid>', methods=['GET','POST'])
def theater_delete(tid):
    th = Theatre.query.filter(Theatre.thetId==tid, Theatre.active=='Y').first()
    th.active = 'N'
    db.session.commit()
    msg = 'Theater Deleted Successfully...!'
    return render_template('theatre.html', th=Theatre.dummy_theatre(), resp=msg,
                           thtrs=Theatre.query.filter(Theatre.active == 'Y').all(),
                           movs=Movie.query.filter(Movie.active == 'Y').all(),
                           adrs=Address.query.filter(Address.active == 'Y').all())


if __name__ == '__main__':
    app.run(debug=True)