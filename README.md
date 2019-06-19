# Fifafinder

User interface on top of [kaggle FIFA 19 complete player dataset](https://www.kaggle.com/karangadiya/fifa19). This website was made using [Flask](http://flask.pocoo.org/docs/1.0/).

## Export as .exe
-----

**Step 1**

In the file __ init __.py, uncomment the before last line of the file (which launch the webbrowser on execution) and set the "debug" argument of the run method to "False" in the last line of the file. 

**Step 2** 

In a terminal, activate a venv on which is installed pyinstaller :

    activate *YOUR_VIRTUAL_ENVIRONMENT*
    
Or directly install pyinstaller in the python default environment :

    pip install pyinstaller

Then, set the project directory as current working directory in a terminal and execute the following line:

    pyinstaller -F --add-data "templates;templates" --add-data "static;static" --add-data "datasets;datasets" --add-data "secret_key.txt;." app.py
    
The process may last few minutes. When it's finished, the .exe file is located in the "dist" directory at the root of the project. You can double click on it from any computer (even if Python is not installed on this computer), it'll launch locally the website on the following address: "http://localhost:5000/".

## Screenshots
-----

![](static/img/screenshots/homepage.png)

![](static/img/screenshots/playerpage.png)