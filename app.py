from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for CSRF protection

# Define the questionnaire form class using WTForms
class QuestionnaireForm(FlaskForm):
    # Define form fields with labels and validators
    name = StringField('Name', validators=[DataRequired()])  # Name field
    student_number = StringField('Student Number', validators=[DataRequired()])  # Student number field
    email = StringField('Email', validators=[DataRequired()])  # Email field
    course = StringField('Programme of Study', validators=[DataRequired()])  # Course field
    grades = StringField('Grades Obtained', validators=[DataRequired()])  # Grades field
    short_term_goal = StringField('Short Term Goal', validators=[DataRequired()])  # Short term goal field
    long_term_goal = TextAreaField('Long Term Goal', validators=[DataRequired()])  # Long term goal field
    satisfaction = SelectField('Overall Satisfaction', choices=[  # Satisfaction select field
        ('very_satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('dissatisfied', 'Dissatisfied'),
        ('very_dissatisfied', 'Very Dissatisfied')
    ], validators=[DataRequired()])
    improvement = RadioField('Suggestions for Improvement', choices=[  # Improvement suggestions radio field
        ('more_practice', 'More Practice'),
        ('better_materials', 'Better Materials'),
        ('more_support', 'More Support')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')  # Submit button

# Define route for the home page
@app.route('/')
def home():
    return render_template('home.html')  # Render the home.html template

# Define route for the information page
@app.route('/information')
def information():
    return render_template('information.html')  # Render the information.html template

# Define route for the data collection page
@app.route('/data', methods=['GET', 'POST'])
def data():
    form = QuestionnaireForm()  # Create an instance of the questionnaire form
    if form.validate_on_submit():  # Check if form submission is valid
        # Open the data.txt file in append mode and write form data to it
        with open('data.txt', 'a') as f:
            f.write(f"{form.name.data}, {form.student_number.data}, {form.email.data}, {form.course.data}, {form.grades.data}, {form.short_term_goal.data}, {form.long_term_goal.data}, {form.satisfaction.data}, {form.improvement.data}\n")
        return 'Form submitted!'  # Display a confirmation message
    return render_template('data.html', form=form)  # Render the data.html template and pass the form instance

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
