from flask import render_template
from sqlalchemy import and_
from flask import url_for, redirect, request, make_response,flash
# Importing Session Object to use Sessions
from flask import session
from app.models import Customer, Restadmin, Items, Orders, Diginadmin
from app import app, db



# ohash=0;

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',restadmin = Restadmin.query.all())

@app.route('/indexmenu', methods = ['GET','POST'])
def indexmenu():


	if request.method == "GET":
		restid = request.args.get("restid")
	
	elif request.method == "POST":
		restid = request.form['restid']

	items = Items.query.filter(Items.rid == restid).all()
	restad = Restadmin.query.filter(Restadmin.rid == restid).first()
	return render_template('indexmenu.html',restad=restad, restadmin=items)


# customerregister.html
@app.route('/register')
def register():
	return render_template('userregister.html')

# customerregisterNext.py
@app.route('/registerNext', methods = ['GET','POST'])
def registerNext():

	customer = Customer(cname=request.form["cname"], cmail=request.form["cmail"], cmobile=request.form["cmobile"], caddress=request.form["caddress"], cpassword=request.form['cpassword'])
	
	db.session.add(customer)
	db.session.commit()

	return redirect(url_for('login'))
	
# customerlogin.html
@app.route('/login')
def login():
	return render_template('userlogin.html')

	
# customerloginNext.html
@app.route('/loginNext',methods=['GET','POST'])
def loginNext():

	if request.method == "GET":
		cmail = request.args.get("cmail")
		cpassword = request.args.get("cpassword")
	
	elif request.method == "POST":
		cmail = request.form['cmail']
		cpassword = request.form['cpassword']

		
		customer  = Customer.query.filter(and_(Customer.cmail == cmail, Customer.cpassword == cpassword)).first()


		if customer :
			session['cmail'] = request.form['cmail']
			return redirect(url_for('userhome1'))
			# return render_template('userhome.html',cusname=customer.cname,restadmin = Restadmin.query.all())
			# return render_template('userhome.html',restadmin = Restadmin.query.all())
			
		return "Login failed ...!"


@app.route('/userhome1',methods=['GET','POST'])
def userhome1():
	cmail=session['cmail']
	customer  = Customer.query.filter(Customer.cmail == cmail).first()

	return render_template('userhome.html',cusname=customer.cname,restadmin = Restadmin.query.all())



# customerlogout.html
@app.route('/logout')
def logout():
	session.pop('cmail',None)
	return redirect(url_for('index'))



@app.route('/restmenu', methods = ['GET','POST'])
def restmenu():


	if request.method == "GET":
		restid = request.args.get("restid")
	
	elif request.method == "POST":
		restid = request.form['restid']

	items = Items.query.filter(Items.rid == restid).all()
	restad = Restadmin.query.filter(Restadmin.rid == restid).first()
	return render_template('restmenu.html',restad=restad, restadmin=items, ohash=ohash)


# restadmin login
@app.route('/restlogin')
def restlogin():
	return render_template('restlogin.html')

	
# restadminloginNext.html
@app.route('/restloginNext',methods=['GET','POST'])
def restloginNext():
	# To find out the method of request, use 'request.method'

	if request.method == "GET":
		rmail = request.args.get("rmail")
		rpassword = request.args.get("rpassword")
	
	elif request.method == "POST":
		rmail = request.form['rmail']
		rpassword = request.form['rpassword']

		
		restadmin  = Restadmin.query.filter(and_(Restadmin.rmail == rmail, Restadmin.rpassword == rpassword)).first()


		if restadmin :
			session['rmail'] = request.form['rmail']
			return redirect(url_for('resthome1'))
			# return render_template('resthome.html',rusname=restadmin.rname,restadmin = Restadmin.query.all())
			# return render_template('resthome.html',restadmin = Restadmin.query.all())
			
		return "Login failed ...!"


@app.route('/resthome1',methods=['GET','POST'])
def resthome1():
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()

	return render_template('resthome.html',rusname=restad.rname,restadmin = Restadmin.query.all())



@app.route('/showmyrestmenu',methods=['GET','POST'])
def showmyrestmenu():
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	restid=restad.rid
	items = Items.query.filter(Items.rid == restid).all()


	return render_template('showmymenu.html',restad=restad, restadmin=items)

@app.route('/additem')
def additem():
	return render_template('additem.html')


@app.route('/additemNext',methods = ['GET','POST'])
def additemNext():
	if request.method == "GET":
		# iid = request.args.get("iid")
		iname = request.args.get("iname")
		iprice = request.args.get("iprice")
		# rid = request.args.get("rid")
	
	elif request.method == "POST":
		# iid = request.form['iid']
		iname = request.form['iname']
		iprice = request.form['iprice']
		# rid = request.form['rid']

	
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	restid=restad.rid

	items = Items(iname=request.form["iname"], iprice=request.form["iprice"], rid=restid)
	db.session.add(items)
	db.session.commit()
	
	return redirect(url_for('showmyrestmenu'))



@app.route('/updateitem',methods = ['GET','POST'])
def updateitem():
	return render_template('updateitem.html')


@app.route('/updateitemNext',methods = ['GET','POST'])
def updateitemNext():
	if request.method == "GET":
		iid = request.args.get("iid")
		iname = request.args.get("iname")
		iprice = request.args.get("iprice")
	
	elif request.method == "POST":
		iid = request.form['iid']
		iname = request.form['iname']
		iprice = request.form['iprice']

	
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	restid=restad.rid

	item = Items.query.filter(and_(Items.iid ==iid,Items.rid==restid)).first()
	if item :
		item.iname=iname
		item.iprice=iprice

		db.session.commit()
		return redirect(url_for('showmyrestmenu'))
	else :
		return redirect(url_for('updateitem'))		




@app.route('/deleteitem',methods = ['GET','POST'])
def deleteitem():
	return render_template('removeitem.html')	


@app.route('/deleteitemNext',methods = ['GET','POST'])
def deleteitemNext():
	if request.method == "GET":
		iid = request.args.get("iid")
	
	elif request.method == "POST":
		iid = request.form['iid']
	
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	restid=restad.rid

	item = Items.query.filter(and_(Items.iid ==iid,Items.rid==restid)).first()
	if item :
		
		db.session.delete(item)
		db.session.commit()
		return redirect(url_for('showmyrestmenu'))
	else :
		return redirect(url_for('updateitem'))



@app.route('/restlogout')
def restlogout():
	# Remove the session variable if present
	session.pop('rmail',None)
	return redirect(url_for('index'))

# 33333333333333333333333333333333333333333333333333333
@app.route('/pra', methods = ['GET','POST'])
def pra():
	if request.method == "GET":
		cname = request.args.get("cname")
		items_selected = request.args.get("items")
		# ohash=request.args.get("ohash")
	
	elif request.method == "POST":
		cname=request.form["total"]
		items_selected=request.form["items"]
		# ohash=request.form["ohash"]
	
	return "Login Successful for: %s" % ohash




# 33333333333333333333333333333333333333333333333333
















@app.route('/adminlogin')
def adminlogin():
	return render_template('adminlogin.html')


@app.route('/adminloginNext',methods=['GET','POST'])
def adminloginNext():

	if request.method == "GET":
		amail = request.args.get("amail")
		apassword = request.args.get("apassword")

	elif request.method == "POST":
		amail = request.form['amail']
		apassword = request.form['apassword']


		Diginadmin  = Diginadmin.query.filter(and_(Diginadmin.amail == amail, Diginadmin.apassword == apassword)).first()


		if Diginadmin :
			session['amail'] = request.form['amail']
			return redirect(url_for('adminHome1'))
			# return render_template('userhome.html',cusname=customer.cname,restadmin = Restadmin.query.all())
			# return render_template('userhome.html',restadmin = Restadmin.query.all())

		return "Login failed ...!"



@app.route('/adminHome1',methods=['GET','POST'])
def adminHome1():
	amail=session['amail']
	Diginadmin  = Diginadmin.query.filter(Diginadmin.amail == amail).first()

	return render_template('adminhome.html',cusname=Diginadmin.aname,restadmin = Restadmin.query.all())