from flask import Flask
import os

app = Flask(__name__)
app.debug = True

secret = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils/secret.txt'))
app.secret_key = secret.readline()[:-1]


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
