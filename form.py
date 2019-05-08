from wtforms import Form, validators, StringField


class PlayerForm(Form):
    player = StringField(validators=[validators.required()])
