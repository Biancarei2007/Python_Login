from markupsafe import escape
from markupsafe import Markup
from flask import Flask, request
import os
from flask import Flask, url_for, request, session, redirect
from flask import Flask, render_template

app = Flask(__name__)

""" @app.route('/')
def index():
    return 'make login' """

#A Minimal Application
""" @app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"  """

#HTML Escaping
""" @app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"   """

#Routing
""" @app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/login')
def login():
    return 'login'  """

#Variables Rules
""" @app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}' 


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}' """  

#Unique URLs
""" @app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page' """

#URL Building
""" @app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))  
 """

#HTTP Methods
""" def do_the_login():
    return 'login'

def show_the_login_form():
    return 'logged'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form() 
 """

#Rendering Templates
""" @app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/hello.html')
def index():
    return render_template('hello.html')
 """

#Accessing Request Data
""" with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST' 
"""

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    # Redireciona para a rota que serve o arquivo index.html
    return redirect(url_for('serve_index'))

@app.route('/index.html')
def serve_index():
    # Renderiza o arquivo index.html que está fora da pasta 'templates'
    return render_template('index.html')

@app.route('/logged')
def logged():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('hello'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()