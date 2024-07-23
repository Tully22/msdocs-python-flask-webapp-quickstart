import os
#import flask

#from flask import (Flask, redirect, render_template, request,
                   #send_from_directory, url_for)

#app = Flask(__name__)
#####################################
#from flask import Flask, render_template, request, flash
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_bootstrap import Bootstrap
#from forms import ContactForm
#from flask_mail import Message, Mail
#import cred

#mail = Mail()
app = Flask(__name__)
# Flask-Bootstrap requires this line
Bootstrap(app)

#contact me
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  return render_template('contact.html')
 
  #if request.method == 'POST':
    #if form.validate() == False:
      #flash('All fields are required.')
      #return render_template('contact.html', form=form)
    #else:
      #msg = Message(form.subject.data, sender='contact@example.com', recipients=['harrytull1@gmail.com'])
      #msg.body = """
      #From: %s <%s>
      #%s
      #""" % (form.name.data, form.email.data, form.message.data)
      #mail.send(msg)
 
      #return render_template("thankyou.html", success=True)
 
  #elif request.method == 'GET':
    #return render_template('contact.html', form=form)

#successful contact me post
@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

#add new pages here and make sure they point to the html files I have built
#these pages fucking work
#homepage
@app.route("/base")
def base():
    return render_template("base.html")

#homepage
@app.route("/")
def home():
    return render_template("index.html")

#page2
@app.route("/page2")
def page2():
    return render_template("index2.html")

#about page
@app.route("/about")
def about():
    return render_template("about.html")

#latest post
@app.route("/post")
def post():
    return render_template("new_project_template.html")

#contact details page - replaced with contact3
#@app.route("/contact")
#def contact():
    #return render_template("contact.html")

#redditbot article
@app.route("/post1")
def post1():
    return render_template("redditbot.html")

#redditbot article
@app.route("/post2")
def post2():
    return render_template("redditbot2.html")

#homeserver article
@app.route("/post3")
def post3():
    return render_template("homeserver.html")

#homeserver article
@app.route("/post4")
def post4():
    return render_template("datamodels.html")

#-------link to posts on main page
#post1
#@app.route("/post1")
#def post1():
    #return render_template("post1.html")

if __name__ == "__main__":
    app.run(debug=True)

#####################################
#@app.route('/')
#def index():
   #print('Request for index page received')
   #return render_template('index.html')

#@app.route('/favicon.ico')
#def favicon():
    #return send_from_directory(os.path.join(app.root_path, 'static'),
                               #'favicon.ico', mimetype='image/vnd.microsoft.icon')

#@app.route('/hello', methods=['POST'])
#def hello():
   #name = request.form.get('name')

   #if name:
       #print('Request for hello page received with name=%s' % name)
       #return render_template('hello.html', name = name)
   #else:
       #print('Request for hello page received with no name or blank name -- redirecting')
       #return redirect(url_for('index'))


#if __name__ == '__main__':
   #app.run()
