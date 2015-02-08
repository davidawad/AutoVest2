from flask import *
from bloom import *
import dataset

app = Flask(__name__)

# Connnect to database
db = dataset.connect('sqlite:///file.db')

# create your guests table
table = db['users']

if not find_com("admin","admin"):
    table.insert( dict(username='admin', password='admin', company="AAPL US Equity") )

#debugging call
#ret = testCommand("AAPL US Equity")

# when someone sends a GET to / render index.html
@app.route('/', methods = ['GET'] )
def sign_form():
    return render_template('index.html')

# when someone sends  POST to /submit, take the name and message from the body
@app.route('/login', methods=['POST'])
def submit():
    signatures = table.find()
    uname = request.form['name']
    pword = request.form['password']
    company = find_com(uname,pword)
    print "SHIT IS NOT"
    price = testCommand(company)
    print "SHIT IS NOW: " + str (price)
    return render_template('data.html', log=True, prices=price )

def find_com(uname,pword):
    signatures = table.find()
    for signature in signatures:
        if signature['username'] == uname :
            if signature['password'] == pword :
                return signature['company']
    return False

app.run(debug=True)
