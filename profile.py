import random

from flask import Flask, request, render_template, jsonify

# from profile.js import submitProfile(evt)

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    return render_template("index.html")



@app.route('/api/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.form['name']
    occupation = request.form['occupation']
    age = request.form['age']
    # TODO: get the values from the rest of the form
    # Add them to jsonify

    return jsonify({'fullname': fullname,
                    'occupation': occupation,
                    'age': age})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
