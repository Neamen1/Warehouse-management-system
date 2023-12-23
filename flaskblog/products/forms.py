from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('Product name', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    price = FloatField('Price per unit', validators=[DataRequired()])
    quantityInStock = IntegerField('Quantity in stock', validators=[DataRequired()])
    unitOfMeasure = StringField('Unit of Measure (pcs, litres...)', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add product')
