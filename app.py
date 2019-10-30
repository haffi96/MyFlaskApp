from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, TextAreaField, validators
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'FlaskApp'


class NameEntry(Form):
    name = StringField('Name:', validators=[InputRequired()])


@app.route('/', methods=['GET', 'POST'])
def home():
    form = NameEntry(request.form)
    if request.method == 'POST':
        name = request.form['name']
        return render_template('name.html', name=name)
    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run()
