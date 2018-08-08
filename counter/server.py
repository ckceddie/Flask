from flask import Flask , redirect, render_template , Response, session 
app=Flask(__name__)
app.secret_key="ThisIsSecret "

# inital page to counter ===================
@app.route("/")
def default():
    return redirect("/counter")


# counter page + set counter times ============== 
@app.route("/counter")
def counter():
    if 'times' in session:
        curr=session['times']
        curr=curr+2
        session['times']=curr
    else :
        session['times'] =1
    return render_template("counter.html")


# clear session =========================
@app.route('/clear')
def clear():
    session.clear()
    return "clear done!"

# reset session['times'] ====================
@app.route("/reset")
def reset():   
    session['times']=-1
    return redirect("/counter")

app.run(debug=True)