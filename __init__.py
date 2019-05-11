from flask import Flask, render_template, url_for, redirect, flash, request
import os
from config import Config
from form import PlayerForm
from utils import get_player_list, get_player_pattern

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def home():
    player_form = PlayerForm(request.form)
    players_list = get_player_list()
    players_pattern = get_player_pattern()

    if request.method == 'POST':

        if player_form.validate():
            return redirect(url_for('player', name=request.form["player"]))
    else:
        flash('All the form fields are required. ')

    return render_template('home.html', form=player_form, players_list=players_list, players_pattern=players_pattern)


@app.route('/player_<name>')
def player(name=None):
    return render_template('player.html', name=name)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':
    app.run()
