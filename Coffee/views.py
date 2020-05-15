from Coffee import app, db
from flask import render_template, request, redirect
from Coffee.models import Coffee


@app.route('/')
def index():
	return render_template('base.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'POST':
		name = request.form['name']
		price = request.form['price']
		structure = request.form['structure']

		coffee = Coffee(name=name, price=price, structure=structure)

		try:
			db.session.add(coffee)
			db.session.commit()
			return redirect('/')
		except:
			return redirect('/add')
	else:
		return render_template('add.html')


@app.route('/see')
def see():
	items = Coffee.query.all()
	return render_template('see.html', items=items)


@app.route('/delete')
def delete():
	items = Coffee.query.all()
	return render_template('delete.html', items=items)


@app.route('/delete/<name>')
def delete_by_name(name):
	item = Coffee.query.filter_by(name=name).first()
	db.session.delete(item)
	db.session.commit()
	return redirect('/delete')


