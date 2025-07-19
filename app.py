import os
# 1. We import 'request' to access user input.
# 2. We now import 'Markup' from 'markupsafe', its new correct location.
from flask import Flask, render_template, abort, request
from markupsafe import Markup

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=os.path.join(basedir, 'templates'))

# This is a simple dictionary acting as our "database" of users.
USER_PROFILES = {
    1: {"name": "Alice", "role": "User"},
    2: {"name": "Bob", "role": "User"},
    3: {"name": "Charlie", "role": "User"},
    7: {"name": "Admin", "role": "Administrator", "flag": "THM{URLS_C4N_B3_M4N1PUL4T3D}"}
}

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/challenge1')
def challenge_one():
    return render_template('challenge1.html')

@app.route('/challenge2')
def challenge_two():
    return render_template('challenge2.html')

@app.route('/challenge3')
def challenge_three():
    return render_template('challenge3.html')

@app.route('/users/<int:user_id>')
def view_user(user_id):
    user = USER_PROFILES.get(user_id)
    if not user:
        abort(404)
    return render_template('profile.html', user=user)

# This is the route for our fourth challenge.
@app.route('/challenge4')
def challenge_four():
    # We get the user's search term from the URL's query parameter.
    search_query = request.args.get('query', '')

    # CRITICAL VULNERABILITY: We are not cleaning or "sanitizing" the input.
    # We use Markup() to tell the template that this string is safe to render as-is.
    # In a real app, you would use a proper sanitization library here.
    return render_template('challenge4.html', search_query=Markup(search_query))


if __name__ == '__main__':
    app.run(debug=True)