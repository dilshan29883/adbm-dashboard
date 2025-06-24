from flask import Flask, render_template, request, redirect, url_for
from forms.booking_form import BookingForm
from db.connection import get_db_connection
from datetime import datetime
from dashboard.analytics import generate_dashboard_data

app = Flask(__name__)
app.secret_key = 'df2c098c3391ff52c4d9d25fb3c7ba1a6cca024c7683c7c3b261d9f39319b7b8'  # Replace with a secure key

@app.route('/', methods=['GET', 'POST'])
def booking():
    form = BookingForm(request.form)
    if request.method == 'POST' and form.validate():
        connection = get_db_connection()
        cursor = connection.cursor()
        # Insert customer
        cursor.execute(
            "INSERT INTO Customer (Customer_name, Email, Phone, Membership_status) VALUES (%s, %s, %s, %s)",
            (form.customer_name.data, form.email.data, form.phone.data, 'Regular')
        )
        customer_id = cursor.lastrowid
        # Insert booking (Showtime_ID and Total_Amount are placeholders)
        cursor.execute(
            "INSERT INTO Booking (Customer_ID, Showtime_ID, Booking_Time, Total_Amount) VALUES (%s, %s, %s, %s)",
            (customer_id, 2, datetime.combine(form.booking_date.data, datetime.now().time()), 0.0)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('success'))
    return render_template('booking.html', form=form)

@app.route('/success')
def success():
    return "Booking successful!"

@app.route('/dashboard')
def dashboard():
    data = generate_dashboard_data()
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


#cd python-booking-app\src"