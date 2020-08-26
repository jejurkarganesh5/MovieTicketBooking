from Ticket_Booking_app.BookMyShow.cust_model import *
from Ticket_Booking_app.BookMyShow.api_service import *


@app.route('/BookMyShow/',methods=['GET','POST'])
def BookMyShow():
    if request.method=='POST':
        theat_data = {
            "tcity": request.form['mcity']
        }

        response = requests.post("http://localhost:5051/theater/api/tcity/", json=theat_data)
        return render_template('bookMyShowDashboard.html', theaters=response.json(), cities=fetch_all_cities())

    return render_template('bookMyShowDashboard.html',cities=fetch_all_cities())

@app.route('/thet/mov/',methods=['GET','POST'])
def mov_thet():
    if request.method=='POST':
        mov_data = {
            "tth": request.form['mtheat']
        }
        print(mov_data)
        response = requests.post("http://localhost:5051/theater/api/tmov/", json=mov_data)
        return render_template('bookMyShowDashboard.html', res =response.json(), cities=fetch_all_cities(),
                               banks=get_all_bankinfo(), movies = get_all_movie())
    return render_template('bookMyShowDashboard.html', cities=fetch_all_cities())


@app.route('/book/movie/ticket/', methods = ['GET','POST'])
def book_ticket():
    if request.method == 'POST':
        ticket_data = {
            "amount": float(request.form['movie']),
            "mobile": int(request.form['mobile']),
            "bank": request.form['bank']
        }
        print(ticket_data)
        response = requests.post("http://localhost:5001/bank/service/", json=ticket_data)
        return render_template('bookMyShowDashboard.html', resp=response.json(), cities=fetch_all_cities())
    return render_template('bookMyShowDashboard.html', cities=fetch_all_cities())