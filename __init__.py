from flask import Flask, render_template, url_for, redirect, flash, request, session
import os
import sys
import webbrowser
from form import PlayerForm
from utils import get_player_list, get_player_pattern, get_player_attributes, resource_path

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

app.secret_key = open(resource_path('secret_key.txt')).readline()[:-1]


@app.route('/', methods=['GET', 'POST'])
def home():
    player_form = PlayerForm(request.form)
    players_list = get_player_list()
    players_pattern = get_player_pattern()

    if request.method == 'POST':

        if player_form.validate():
            session['playername'] = request.form['player']
            return redirect(url_for('player', name=request.form["player"].replace('. ', '_').replace(' ', '_')))

    else:
        flash('All the form fields are required. ')

    return render_template('home.html', form=player_form, players_list=players_list, players_pattern=players_pattern)


@app.route('/player_<name>')
def player(name):
    playername = session.get('playername', None).strip()
    attributes = get_player_attributes(playername=playername)
    return render_template('player.html', attributes=attributes)


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
    # webbrowser.open('http://localhost:5000')
    app.run(debug=True)
