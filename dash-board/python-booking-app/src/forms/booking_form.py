from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, validators

class BookingForm(FlaskForm):
    customer_name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    phone = StringField('Phone', [validators.DataRequired()])
    booking_date = DateField('Booking Date', format='%Y-%m-%d', validators=[validators.DataRequired()])
    submit = SubmitField('Book Now')

    def validate(self):
        if not super().validate():
            return False
        # Additional custom validation can be added here
        return True

    def render(self):
        return self._render()  # Assuming _render is defined to return the form HTML

    def process_data(self, form_data):
        # Process the submitted form data
        self.customer_name.data = form_data.get('name')
        self.email.data = form_data.get('email')
        self.phone.data = form_data.get('phone')
        self.booking_date.data = form_data.get('booking_date')