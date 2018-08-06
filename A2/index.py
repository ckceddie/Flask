from flask import Flask, render_template , request , redirect
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/result",methods=["POST"])
def result():
    print "=======================1========================"
    get_name=request.form['name']
    get_location=request.form['location']   
    get_language=request.form['mylanguage']
    get_comment=request.form['mycomment']
    print "======================="+ get_name +"========================"
    return render_template("result.html",name=get_name,location=get_location,mylanguage=get_language,mycomment=get_comment)
    # return render_template("result.html",name=get_name)

app.run(debug=True)