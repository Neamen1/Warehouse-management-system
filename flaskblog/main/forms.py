from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class OrderStatusForm(FlaskForm):
    status_choices = [('Pending', 'Pending'), ('Shipping', 'Shipping'), ('Delivered', 'Delivered'), ('Ready to pick up', 'Ready to pick up')]
    status = SelectField('Order Status', choices=status_choices, validators=[DataRequired()])
    submit = SubmitField('Change Status')