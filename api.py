from flask import Flask, render_template, request
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def home_back():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/services.html")
def services():
    return render_template("services.html")

@app.route("/projects.html")
def projects():
    return render_template("projects.html")

@app.route("/godrej.html")
def projectsdetails():
    return render_template("godrej.html")

@app.route("/tata.html")
def projectsdetails1():
    return render_template("tata.html")

@app.route("/flipkart.html")
def projectsdetails2():
    return render_template("flipkart.html")

@app.route("/itc.html")
def projectsdetails3():
    return render_template("itc.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/elements.html")
def elements():
    return render_template("elements.html")

@app.route("/inquiry", methods=['POST','GET'])
def mail():
    email_sender = 'deviranshenterprise@gmail.com'
    email_password = 'zaoqkzvxxvuczlkp'
    email_receiver = ['deviransh@gmail.com']
    subject = 'New query!!'
    body = """
You have a query from:

Name: {}
Email ID: {}
Subject: {}

Message:

{}""".format(request.form['name'], request.form['email'],request.form['subject'],request.form['message'] )
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
    b = 'Query recorded! Our team will get back to you shortly.'
    return render_template("contact.html", b = b, id = 'message')

@app.route("/news", methods=['POST','GET'])
def subs():
    email_sender = 'deviranshenterprise@gmail.com'
    email_password = 'zaoqkzvxxvuczlkp'
    email_receiver = ['deviransh@gmail.com']
    subject = 'New subscription!!'
    body = """
You have subscription from:

Email ID: {} """.format(request.form['email'])
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())
    a = 'Subscription added successfully!'
    return render_template("index.html", a = a)

@app.route("/project-details.html")
def proj():
     return render_template("project-details.html")


if __name__ =='__main__':
    app.run(debug=False)