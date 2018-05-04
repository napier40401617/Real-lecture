from flask import Flask, render_template,jsonify,request, flash
import sqlite3, json

app = Flask(__name__)

@app.route('/')
def indexPage():
	return render_template("student1.html")

@app.route('/save', methods=['GET','POST'])
def saveStudent():
	print("saving student" + request.method)
	error=''
	if request.method == 'POST':
		try:
			print (request.form)
			name = request.form['Name']
			phy = int(request.form['Physics'])
			che = int(request.form['Chemistry'])
			math = int(request.form['Mathematics'])
		except ValueError:
			error = "data input error"
			return render_template("student1.html",error=error)
		try:
			with sqlite3.connect("sqlite3.db") as con:
				cur = con.cursor()
				cur.execute("insert into student(name,Physics,Chemistry,Maths) values(?,?,?,?)",(name,phy,che,math))
				con.commit()
				msg = "saving"
			#return redirect(url_for("flashMessage.html",msg = msg))
		except:
			con.rollback()
		finally:
			#con.close()
			return render_template("student1.html",error=error)
	return render_template("student1.html",error=error)

@app.route('/allStudents')
def studentInformation():
	con = sqlite3.connect("sqlite3.db")
	cur = con.cursor()
	cur.execute("select * from student")
	rows = cur.fetchall()
	print(rows)
	return json.dumps(rows)

#@app.route('/save', methods)
if __name__=="__main__":
	app.run(debug=True)