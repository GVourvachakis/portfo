from flask import Flask, render_template, request, redirect
import csv #CSV = Comma Separated Values
#from flask import url_for

app = Flask(__name__) #our app is called 'main'
#print(__name__) -> __main__

@app.route('/') 
def my_home():
    #print(url_for('static', filename='book_tech.ico')) -> /static/book_tech.ico
    return render_template('index.html') #searches inside of a directory called 'templates'

''' 
In terminal:
    export FLASK_APP=server.py
    flask run
In Google Chrome: 
    http://127.0.0.1:5000/
    output:
        A simple server including Hello, World!
In order to not always restart your server to view the changes
you can open the 'Debug mode' typing in terminal:
    FLASK_ENV=development
    flask run
So you can just refresh your server in chrome
'''

'''
<p>This is a paragraph of text. 
It can contain multiple sentences or lines, 
and the browser will automatically add spacing between paragraphs.</p>
'''



@app.route("/blog") 
def blog():
    return "<p>These are my thoughts about blogs!</p>"

@app.route("/blog/2020/dogs") 
def blog_dog():
    return "This is my dog!"

@app.route("/<string:page_name>") #dynamically accept URL parameters to seek any html file
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route("/submit_form", methods = ['POST','GET']) #dynamically accept URL parameters to seek any html file
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save in database'
    else:
        return'Something went wrong. Try again.'


