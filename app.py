from flask import Flask, render_template, request, redirect, url_for
# to import the Flask class and then added the required functions needed as I went along
from wtforms import Form, StringField, TextAreaField, validators
# Used wtforms to create the input field as it makes the code alot simpler and cleaner. Also easier to understand
from wtforms.validators import InputRequired
# This was used to import the function needed for validating input.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FlaskApp'
# I have added the secret key which could also be a randomzied string as I understand that this is good practice however I am not sure how this works


class NameEntry(Form):  # this is to generate a class for the name field
    name = StringField(validators=[InputRequired()])
    # StringField calls on the function imported at the start and
    # I have called this 'name' which is used below in the logic part of the script
    # Validators is used to ensure an input is given


@app.route('/', methods=['GET', 'POST'])
# GET and POST are methods used to handle data. i.e GET may be used to retrieve informaiton from a database
def home():
    form = NameEntry(request.form)
    if request.method == 'POST':
        name = request.form['name']
        # this links to the page you will be redirected to after submitting
        return render_template('name.html', name=name)
    # this is template used to markup the html displayed on the home page
    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run()
