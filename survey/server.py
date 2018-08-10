# Validation & error message by flash
# (1) import flash 
# (2) check and add flash message for error 
# <!-- (3)return error message  -->


from flask import Flask, render_template , request , redirect , flash
app=Flask(__name__)
app.secret_key="ThisIsKey"

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/result",methods=["POST"])
def result():


    get_name=request.form['name']
    get_location=request.form['location']   
    get_language=request.form['mylanguage']
    get_comment=request.form['mycomment']

    back_page=False

# (2) check and add flash message for error

    if len(get_language)<1:
        flash("Please select your favorite language.")

        back_page=True

    if len(get_location)<1:
        flash("Please select your location.")
        back_page=True
   

    if back_page==True:
        return render_template("main.html")

    if len(get_comment)>120 :    
        flash("Comment cannot be over 120 words!")
        back_page=True
    return render_template("result.html",name=get_name,location=get_location,mylanguage=get_language,mycomment=get_comment)
    # return render_template("result.html",name=get_name)

app.run(debug=True)