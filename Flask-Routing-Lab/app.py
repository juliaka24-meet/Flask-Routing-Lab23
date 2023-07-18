from flask import Flask, redirect, request, render_template, url_for


app = Flask( __name__, template_folder='templates', static_folder='static')

@app.route("/")
def home_page():
	return render_template("home.html")

@app.route("/product")
def product_page():
	return render_template("product.html")

@app.route("/cart")
def cart_page():
	return render_template("cart.html")

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)