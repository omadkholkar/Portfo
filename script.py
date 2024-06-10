
from flask import Flask, render_template, request,redirect
from datetime import date
import csv
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('HTML.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    dt=open('data.text','a')
    email=data['email']
    sub=data['subject']
    desc=data['Describe']
    todays_date=date.today()
    dt.write(f'\n{todays_date} {email},{sub},{desc}')
    dt.close()

def write_to_file_csv(data):
    with open('data.csv',mode='a') as dt:
        header=['email','Subject','Describe']
        email=data['email']
        sub=data['subject']
        desc=data['Describe']
        todays_date=date.today()
        df=csv.writer(dt, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        df.writerow([todays_date,email,sub,desc])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form(data=None):
    if request.method=="POST":
        data=request.form.to_dict()
        print(data)
        write_to_file_csv(data)
        return render_template('/thanky_form.html',data_o=data)
    

'''@app.route("/html")
def next():
    return render_template('HTML.html')'''


if __name__ == '__main__':
   app.run(debug = True)