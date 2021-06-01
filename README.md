# Fifabrowser

User interface on top of [kaggle FIFA 19 complete player dataset](https://www.kaggle.com/karangadiya/fifa19). This webapp was made using [Flask](http://flask.pocoo.org/docs/1.0/) and [Chart.js](https://www.chartjs.org/). 

[**You can try the app by clicking here**](https://fifabrowser.herokuapp.com/)

## Run locally

Docker makes it easy to run the app locally:

    docker build -t fifabrowser:1.0 .
    docker run -p 5000:5000 -d fifabrowser:1.0

You can now open your browser at http://localhost:5000/ to use the app.

## Deployment (Docker & Heroku)

Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

Sign in to Heroku and to the Container Registry:

    heroku login -i
    heroku container:login

Push the Docker image to the registry (it will build the docker image using the [Dockerfile](Dockerfile)):

    heroku container:push web --app <YOUR_HEROKU_APP_NAME>

Deploy the app:

    heroku container:release web --app <YOUR_HEROKU_APP_NAME>

## Export as executable

Install pyinstaller:

    pip install pyinstaller
 
Run:

    pyinstaller -F --add-data "templates:templates" \
                   --add-data "static:static" \
                   --add-data "data:data" \
                   app.py
    
The executable file will be **located in the newly created `dist` directory**, at the root of the project. You can launch it from any computer (even if Python is not installed), the application will be accessible at: http://localhost:5000/.

## Screenshots

<img src="./static/img/screenshots/homepage.PNG">

<img src="./static/img/screenshots/playerpage.PNG">