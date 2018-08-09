from flask import Flask , redirect, render_template , Response, session,request
import random
app=Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def index():
    min=1
    session['min']=min
    max=100
    session['max']=max
    session['random_num']=random.randrange(1, 3) # random number between 0-100
    return render_template("game.html",min=min , max=max , result='Take a guess!',bgcolor='white' )

@app.route('/submit' , methods=['post'])
def submit():
    min=session['min']
    max=session['max']
    reset = 0
    input_num=request.form['input_num']
    if request.form['input_num'] == "":
        return render_template("game.html",min=min , max=max ,result='Input field is out of range, Please take a guess again !')

    if (int(input_num)==session['random_num']):  
        
        return render_template("game.html",display=input_num+" was the number",reset=1,min=min , max=max ,bgcolor='green' ,result='Bingo ! The number I am thinking is :'+ input_num)
    elif (int(input_num)>session['random_num']):
        max=int(input_num)
        session['max']=max
        return render_template("game.html",display="Too high",min=min , max=input_num ,bgcolor='red',result='[Sorry you are wrong , your number is too large. Please try it again .]')
    elif (int(input_num)<session['random_num']):

        min=int(input_num) 
        session['min']=min
        return render_template("game.html",display="Too low",min=input_num , max=max ,bgcolor='red' ,result='[Sorry you are wrong , your number is too small. Please try it again .]')
    else:
        return render_template("game.html",min=min , max=max ,result='[Sorry Something Error! Please try it again.]')

@app.route('/reset',methods=['post'])
def reset():
        return redirect('/')
app.run(debug=True)