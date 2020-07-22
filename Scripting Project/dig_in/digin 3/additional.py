@app.route('/adminHome1',methods=['GET','POST'])
def userhome1():
	amail=session['amail']
	Diginadmin  = Diginadmin.query.filter(Diginadmin.amail == amail).first()

	return render_template('adminHome.html',cusname=Diginadmin.aname,restadmin = Restadmin.query.all())


@app.route('/adminLoginNext',methods=['GET','POST'])
def adminLoginNext():

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


@app.route('/adminLogin')
def adminLogin():
	return render_template('adminlogin.html')            
