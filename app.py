from flask import Flask, render_template, url_for, request, redirect
import pickle

app = Flask(__name__)

model = pickle.load(open("linear_regression.pkl","rb"))
@app.route("/",methods =['POST','Get'])
def home():
	if request.method == "POST":
		petrol , deisel , manual, indiv = 0,0,0,0
		p_price = float(request.form['Present_Price'])
		km =  int(request.form['kms'])
		age = 2021 - int(request.form['age'])
		no_of_owners = int(request.form['Owners'])
		
		fuel = request.form['fuel']
		if fuel == 'petrol':
			petrol = 1
		elif fuel == 'deisel':
			deisel = 1		

		transmission = request.form['transmission']
		if transmission == 'manual':
			manual = 1

		seller = request.form['seller']
		if transmission == 'indiv':
			indiv = 1

		values = [p_price,km,no_of_owners,age,deisel,petrol,indiv,manual]
		predictions = model.predict([values])[0]

		return render_template("home.html",context="Predicted Selling Price is Rs. {}.".format(predictions))
	else:

		return render_template("home.html",context='')

if __name__ == '__main__':
	app.run(debug=True)