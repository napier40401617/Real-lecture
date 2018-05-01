from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello():
	return 'Welcome to local host'

@app.route('/hello/<name>')
def hello1(name=None):
	user={'name':name}
	return render_template('hello.html',user=user)

if __name__ == "__main__":
	app.run(debug=True)