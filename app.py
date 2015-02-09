from flask import *
import dataset
import subprocess, sys, os

app = Flask(__name__)

# Connnect to database
db = dataset.connect('sqlite:///file.db')

# create your guests table
table = db['users']

'''
if not find_com("admin","admin"):
    table.insert( dict(username='admin', password='admin', company="AAPL US Equity") )
'''
'''
return redirect(url_for('show', id=rec.id))
'''
#debugging call
#ret = testCommand("AAPL US Equity")

# when someone sends a GET to / render index.html
@app.route('/', methods = ['GET'] )
def root():
    return render_template('index.html')

# when someone sends  POST to /submit, take the name and message from the body
@app.route('/data', methods=['POST'])
def getData():
    signatures = table.find()
    uname = request.form['name']
    pword = request.form['password']
    #company = find_com(uname,pword)
    company = find_com('admin','admin')
    #print "company is" + str(company)
    #print "COMPANY IS " + str(company)
    price = testCompany("AAPL US Equity")
    #print str(price)
    #print "SHIT IS NOW: " + str(price)
    #price = request("http-api.openbloomberg.com")
    return render_template('data.html', prices=True)

@app.route('/logform', methods=['GET'])
def logform():
    return render_template('logform.html')

@app.route('/login', methods=['POST'])
def logger():
    signatures = table.find()
    uname = request.form['name']
    pword = request.form['password']
    return render_template('logform.html',prices=True)


def find_com(uname,pword):
    signatures = table.find()
    for signature in signatures:
        if signature['username'] == uname :
            if signature['password'] == pword :
                return signature['company']
    return False


def testCompany(company):
    cmd = ["sudo", "node", "bloom.js", str(company) ]
    print "RUNNING COMMAND FOR " + str(company)
    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE)
    stdout = proc.communicate()[0]
    myList = [ ]
    print stdout
    for line in stdout.splitlines():
        print line.strip()
        myList.append(float(line.strip().replace(" ", "")))
    return myList

@app.errorhandler(error)
def new_page(error):
	return render_template('error.html', error=error)

'''
@app.errorhandler(500)
def page_not_found(error): # will send me an email with hopefully some relevant information using sendgrid
	sg = sendgrid.SendGridClient('YOUR_SENDGRID_USERNAME', 'YOUR_SENDGRID_PASSWORD')
	message = sendgrid.Mail()
	message.add_to('David Awad <davidawad64@gmail.com>')
	message.set_subject('500 Error on Spaceshare')
	message.set_html('Body')
	message.set_text('Hey dave, there was another error on spaceshare I apologize! Spaceshare currently has '+str(visitors)+' visitors.')
	message.set_from('Space Admin <Admin@spaceshare.me>')
	#status, msg = sg.send(message)
	return render_template('error.html', error=500)
'''
app.run(debug=True)
