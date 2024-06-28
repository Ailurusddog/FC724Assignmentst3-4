from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class QuestionnaireForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    course = StringField('Programme of Study', validators=[DataRequired()])
    grades = StringField('Grades Obtained', validators=[DataRequired()])
    short_term_goal = StringField('Short Term Goal', validators=[DataRequired()])
    long_term_goal = TextAreaField('Long Term Goal', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[
        ('very_satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('dissatisfied', 'Dissatisfied'),
        ('very_dissatisfied', 'Very Dissatisfied')
    ], validators=[DataRequired()])
    improvement = RadioField('Suggestions for Improvement', choices=[
        ('more_practice', 'More Practice'),
        ('better_materials', 'Better Materials'),
        ('more_support', 'More Support')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        with open('data.txt', 'a') as f:
            f.write(f"{form.name.data}, {form.student_number.data}, {form.email.data}, {form.course.data}, {form.grades.data}, {form.short_term_goal.data}, {form.long_term_goal.data}, {form.satisfaction.data}, {form.improvement.data}\n")
        return 'Form submitted!'
    return render_template('data.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
