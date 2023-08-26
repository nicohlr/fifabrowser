import os
import sys
import pandas as pd

from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    flash,
    request,
    session,
    jsonify,
)

from utils.form import PlayerForm
from utils.utils import (
    get_player_list,
    get_player_pattern,
    get_player_attributes,
    clean_playername,
)

# Check if the website is launched using an executable file
if getattr(sys, "frozen", False):
    template_folder = os.path.join(sys._MEIPASS, "templates")
    static_folder = os.path.join(sys._MEIPASS, "static")
    app = Flask(
        __name__, template_folder=template_folder, static_folder=static_folder
    )
else:
    app = Flask(__name__)

app.secret_key = os.urandom(32)
df = pd.read_parquet("data/data.pq")
players_list = get_player_list(df)
players_pattern = get_player_pattern(df)


@app.route("/", methods=["GET", "POST"])
def home():
    """Homepage function: get playername inputed by user."""
    player_form = PlayerForm(request.form)

    if request.method == "POST":
        if player_form.validate():
            name = clean_playername(request.form["player"])
            attributes = get_player_attributes(df=df, playername=name)

            # Store attributes in the session
            session["attributes"] = attributes

            return redirect(url_for("player", name=name))

    else:
        flash("All the form fields are required. ")

    return render_template(
        "home.html",
        form=player_form,
    )


@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    query = request.args.get("query").lower()
    matches = [player for player in players_list if query in player[0].lower()]
    # Return only the first 20 matches for performance
    return jsonify(matches[:20])


@app.route("/<name>")
def player(name):
    """Playerpage function: forward player attributes to HTML frontend."""
    attributes = session.get("attributes")
    print(attributes)
    return render_template("player.html", attributes=attributes)


@app.context_processor
def override_url_for():
    """Function to fix pages not changing when code is modified locally."""
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == "static":
        filename = values.get("filename", None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values["q"] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5300))
    app.run(host="0.0.0.0", port=port)
