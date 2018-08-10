from flask import Flask , request, redirect , render_template , session , Response
# get current datetime ----------------------
import time


import random
app=Flask(__name__)
app.secret_key = "ThisIsSecret"



@app.route("/")
def index():
    if not 'gold' in session :
        session['gold']=0
    return render_template('places.html')



@app.route("/process_money" , methods=['post'])
def process():
    
    # set variable ================================
    if not 'gold' in session :
        session['gold']=0
    win=0
    lost=1+1
    gamble=random.randrange(win,lost)

    # import time
    # https://docs.python.org/3/library/time.html#time.strftime
    cur_time = str(time.strftime("%Y/%m/%d  %I:%M%p"))
    #=============================================================


    if not "act_message" in session :
        session["act_message"]=[]
    if request.form['place']=='farm':
          
        min_amount=10
        max_amount=20+1
        amount=random.randrange(min_amount, max_amount)
        session['gold']=session['gold']+amount
     
        session["act_message"].append({"place":"Farm","gold":amount,"gamble":win,"date":str(cur_time)})
    
    elif request.form['place']=='cave':
        min_amount=5
        max_amount=10+1
        amount=random.randrange(min_amount, max_amount)
        session['gold']=session['gold']+amount

        session["act_message"].append({"place":"Cave","gold":amount,"gamble":win,"date":str(cur_time)})
    
    elif request.form['place']=='house':
        min_amount=2
        max_amount=5+1
        amount=random.randrange(min_amount, max_amount)
        session['gold']=session['gold']+amount
        session["act_message"].append({"place":"House","gold":amount,"gamble":win,"date":str(cur_time)})
    
    elif request.form['place']=='casino':
        min_amount=0
        max_amount=50+1
        amount=random.randrange(min_amount, max_amount)
        if gamble==win:
            session['gold']=session['gold']+amount
        else:
            session['gold']=session['gold']-amount
        
        session["act_message"].append({"place":"Casino","gold":amount,"gamble":gamble,"date":str(cur_time)})
    
    return render_template('places.html')


@app.route("/clear")
def clear():
    session.pop('gold')
    session.pop('act_message')
    session.clear() 
    if not 'gold' in session :
        session['gold']=0
    return render_template('places.html')

app.run(debug=True)