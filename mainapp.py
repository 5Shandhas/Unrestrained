from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config.update(DEBUG=True)
app.config['SECRET_KEY'] = '15615156dhiuahdkbafiuwahfw'

posts = [
	{
		'author': 'yangjingbo',
		'title': 'Blog Post1'
	}
]

@app.route("/")
@app.route("/home")
def mainapp():
	return render_template('main.html', posts=posts, title='About')

@app.route("/about")
def about():
	return "<h2>About Pages<h2>"

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
	app.run(debug=True)