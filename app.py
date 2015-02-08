from flask import *
from bloom import *
import dataset
#from flask.ext.login import LoginManager


app = Flask(__name__)

# Connnect to database
db = dataset.connect('sqlite:///file.db')

# create your guests table
table = db['users']
table.insert( dict(username='admin', password='admin', company="AAPL US Equity") )

#debugging call
ret = testCommand("AAPL US Equity")

#login_manager = LoginManager()
#login_manager.init_app(app)

# when someone sends a GET to / render sign_form.html
@app.route('/', methods = ['GET'] )
def sign_form():
    return render_template('index.html')

# when someone sends a GET to their own account
@app.route('/stockview', methods=['GET'])
def stock_view():
    signatures = table.find()
    for signature in signatures:
        break
    return render_template('data.html', signatures=signatures )

# when someone sends  POST to /submit, take the name and message from the body
# of the POST, store it in the database, and redirect them to the guest_book
@app.route('/login', methods=['POST'])
def submit( ):
    signature = dict( username=request.form['name'], password=request.form['password'] )
    signatures = table.find()
    return redirect(url_for('stockview'))

app.run(debug=True)
