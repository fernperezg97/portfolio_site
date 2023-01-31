import os
from flask import Flask, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def index():
    """return homepage"""

    return render_template("homepage.html")














if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)