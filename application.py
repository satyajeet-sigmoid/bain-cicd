import uuid

import flask
from flask import Flask, render_template_string, request, session, redirect, url_for, sessions
from flask_session import Session
import cpp_config
import os
application = app = Flask(__name__)
application.secret_key = os.environ.get('SECRET_KEY', 'dev')

application.config.from_object(cpp_config)
# session.init_app(application)
Session(application)

from functools import wraps
from flask import g, request, redirect, url_for


# def get_session_prefixed(djsession_id):
#     pass

#
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         djsession_id = request.cookies.get("sessionid")
#         if djsession_id is None:
#             return redirect("/")
#
#         key = get_session_prefixed(djsession_id)
#         session_store = SessionStore(redis_conn, key)
#         auth = session_store.load()
#
#         if not auth:
#             return redirect("/")
#
#         g.user_id = str(auth.get("_auth_user_id"))
#
#         return f(*args, **kwargs)
#     return decorated_function


@app.route('/')
def test_environ():
    return "testing session with developer"

@app.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'POST':
        # Save the form data to the session object

        session['email'] = request.form['email_address']
        return redirect(url_for('get_email'))

    return """
        <form method="post">
            <label for="email">Enter your email address:</label>
            <input type="email" id="email" name="email_address" required />
            <button type="submit">Submit</button
        </form>
        """



@app.route('/get_email')
def get_email():
    session_id = flask.session['uid'] = uuid.uuid4()
    if session_id is None:
            return redirect("/")

    return render_template_string("""
            {% if session['email'] %}
                <h1>Welcome {{ session['email'] }}!</h1>
            {% else %}
                <h1>Welcome! Please enter your email <a href="{{ url_for('set_email') }}">here.</a></h1>
            {% endif %}
        """)


@app.route('/delete_email')
def delete_email():
    # Clear the email stored in the session object
    session.pop('email', default=None)
    return '<h1>Session deleted!</h1>'


if __name__ == '__main__':
    app.run(host="localhost", port=5005, debug=True)
