from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	opposite_day = False
	fav_foods = ['Hamburger', 'Steak', 'Panakook']
	worse_foods = ['Tomatoes', 'Chocolate', 'Hummus']
	return render_template("index.html", 
		opposite_day = opposite_day, fav_foods = fav_foods, worse_foods = worse_foods)

if __name__ == '__main__':
   app.run(debug = True)