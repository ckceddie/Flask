from flask import Flask, render_template , request , redirect ,session
app=Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    session['name']= request.form['name']
    session['email'] = request.form['email']
	 # Here's the line that changed. We're rendering a template from a post route now.
    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html",name=session['name'],email=session['email'])
app.run(debug=True)