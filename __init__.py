from flask import Flask, render_template, url_for
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/request')
def request():
    return render_template('request.html')


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
    print(app.secret_key)
    app.run()
