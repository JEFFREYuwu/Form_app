from flask import Flask, render_template, request, session
# used to implement permenant session/timed session
from datetime import datetime, timedelta


# needed module for mail facilities

from flask_mail import Mail, Message

# needed module to upload files

from werkzeug import secure_filename

#include database functionality sqlalchemy
# from flask_mysqldb import MYSQL

app = Flask(__name__)



#mailing configuration

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jeffuwu@gmail.com'
app.config['MAIL_PASSWORD'] = 'unknown'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

#mail object
mail = Mail(app)


#secret key needed to implement sessions
app.secret_key= "unknown"

# Declaring how long the session is going to persist days, hours, minutes etc
app.permenant_session_lifetime = timedelta(minutes=1)


@app.route("/form", methods=["POST","GET"])
def form():
       
   if request.method == 'POST':
      session["work_kids"]=request.form["work_kids"]
      session["carer"]=request.form['carer']
      session["experience"]=request.form['experience']
      session["teacher"]=request.form["teacher"]
      cover_letter= request.form.get("cover_letter")
      session["manager"]=request.form["manager"]
      session["speak"]=request.form["speak"]
      session["learn"]=request.form["learn"]
      session["prepare"] =request.form["prepare"]
      session["events"]=request.form["events"]
      indentity=request.form.get("indentity")
      

    
      score=0
      if session["manager"]=="YES":
        score+=1
      else:
         pass 
      if session["speak"]=="YES":
         score+=1
      else:
         pass
      if session["teacher"]=="YES":
         score+=1
      else:
         pass
      if session["events"]=="YES":
         score+=1
      else:
         pass
      if session["learn"]=="YES":
         score+=1
      else:
         pass
      if session["prepare"]=="YES":
         score+=1
      else:
         pass
      if session["work_kids"]=="YES":
         score+=1
      else:
         pass
      if session["carer"]=="YES":
         score+=1
      else:
         pass
      if session["experience"]=="YES":
         score+=1
      else:
         pass
      if score==5:
         if request.files:
            f = request.files['file']
            f.save(secure_filename(f.filename)) 
            msg = Message('Hello', sender = 'jeffuwu@gmail.com', recipients = ['jeffuwu@yahoo.com'])
            msg.body = f" {indentity} seems a good candidate. See attached CV and cover letter below.\n\n\n\n {cover_letter} "
            name=str(f.filename)
            f = open(name, "rb")
            msg.attach(name,'application/octect-stream',f.read())
            mail.send(msg)
            return "Sent"
         else:
            return f"Score is {score}, which is less than 5"
         
      
         

      
   else:
      return render_template("form_app.html")


       




if __name__ == "__main__":
   
    app.run(debug=True)