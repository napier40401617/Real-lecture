from flask import Flask,g
import sqlite3

from flask import Flask
app=Flask(__name__)
db_location='student.db'

def get_db():
	db=getattr(g,'db',None)
	if db is None:
		db=sqlite3.connect(db_location)
		g.db=db
	return db

@app.teardown_appcontext
def close_db_connection(exception):
	db=getattr(g,'db',None)
	if db is not None:
		db.close()

def init_db():
	with app.app_context():
		db=get_db()
		with app.open_resource('schema.sql',mode='r')as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.route("/")
def root():
	start=init_db()
	db=get_db()
	db.cursor().execute('insert into albums values("America Beauty","Grateful Dead","CD")')
	db.commit()

	db.cursor().execute('insert into albums values("ck","Guess","CD")')
	db.commit()
	
	page=[]
	page.append('<html><ul>')
	sql="select rowid, * from albums order by artist"
	for row in db.cursor().execute(sql):
		page.append('<li>')
		page.append(str(row))
		page.append('<li>')
	page.append('</ul></html>')
	return ''.join(page)

if __name__ == "__main__":
	app.run(debug=True)

