from Ticket_Booking_app.Theatre.model import *




@app.route('/movie/save/', methods=['GET','POST'])
def movie_save_edit():
    msg = ''
    if request.method=='POST':
        reqform=request.form
        mov = Movie.query.filter(Movie.movId==reqform['mid'],Movie.active=='Y').first()
        if mov:
            mov.movName=reqform['mnm']
            mov.movFare=reqform['mfare']
            mov.movRating=reqform['mrating']
            db.session.commit()
            msg='Movie Updated Successfully...!'
        else:
            mov = Movie(movId=reqform['mid'],movName=reqform['mnm'],movFare=reqform['mfare'],movRating=reqform['mrating'])
            db.session.add(mov)
            db.session.commit()
            msg = 'Movie Added Successfully...!'
        return render_template('movie.html', movs=Movie.query.filter(Movie.active=='Y').all(),
                               resp=msg, mov=Movie.dummy_movie())

    return render_template('movie.html', movs=Movie.query.filter(Movie.active == 'Y').all(),
                           resp=msg, mov=Movie.dummy_movie())

@app.route('/movie/edit/<int:mid>')
def movie_edit(mid):
    return render_template('movie.html',mov=Movie.query.filter(Movie.movId==mid,Movie.active=='Y').first(),
                           movs=Movie.query.filter(Movie.active == 'Y').all() )

@app.route('/movie/delete/<int:mid>')
def movie_delete(mid):
    mov = Movie.query.filter(Movie.movId==mid,Movie.active=='Y').first()
    mov.active='N'
    db.session.commit()
    msg = 'Movie Deleted Successfully'
    return render_template('movie.html',mov=Movie.dummy_movie(),resp=msg,
                           movs=Movie.query.filter(Movie.active == 'Y').all() )



if __name__ == '__main__':
    app.run(debug=True)