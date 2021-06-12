# fifabrowser

User interface on top of [kaggle FIFA 19 complete player dataset](https://www.kaggle.com/karangadiya/fifa19). This webapp was made using [Flask](http://flask.pocoo.org/docs/1.0/) and [Chart.js](https://www.chartjs.org/). 

[**You can try the app by clicking here**](https://fifabrowser.herokuapp.com/)

## Run locally

Docker makes it easy to run the app. From a terminal, run:

```sh
$ docker run -p 5000:5000 nicohlr/fifabrowser:1.0
```

You can now open your browser at http://localhost:5000/ to use the app.

You can also clone the repo and build the image locally using the provided [Dockerfile](Dockerfile):

```sh
$ git clone https://github.com/nicohlr/fifabrowser.git
$ docker build -t fifabrowser ./fifabrowser/
$ docker run -p 5000:5000 -d fifabrowser
```

## Deployment (Docker & Heroku)

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Sign in to Heroku and to the Container Registry:

```sh
$ heroku login -i
$ heroku container:login
```

Push the Docker image to the registry and deploy the app:

```sh
$ heroku container:push web --app <YOUR_HEROKU_APP_NAME>
$ heroku container:release web --app <YOUR_HEROKU_APP_NAME>
```

## Export as executable

The python package pyinstaller allows you to easily create an executable:

```sh
$ pip install pyinstaller
$ pyinstaller -F --add-data "templates:templates" \
                 --add-data "static:static" \
                 --add-data "data:data" app.py
```
    
The executable file will be **located in the newly created `dist` directory**, at the root of the project. You can launch it from any computer (even if Python is not installed), the application will be accessible at: http://localhost:5000/.

## Screenshots

<img src="./static/img/screenshots/homepage.PNG">

<img src="./static/img/screenshots/playerpage.PNG">