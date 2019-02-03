from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
	app.run(debug=True)