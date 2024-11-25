from flask import Flask, request
from iebank_api import db, app
from iebank_api.models import Account
from iebank_api.models import User

from iebank_api import default_username, default_password

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/skull', methods=['GET'])
def skull():
    text = 'Hi! This is the BACKEND SKULL! 💀 '
    
    text = text +'<br/>Database URL:' + db.engine.url.database
    if db.engine.url.host:
        text = text +'<br/>Database host:' + db.engine.url.host
    if db.engine.url.port:
        text = text +'<br/>Database port:' + db.engine.url.port
    if db.engine.url.username:
        text = text +'<br/>Database user:' + db.engine.url.username
    if db.engine.url.password:
        text = text +'<br/>Database password:' + db.engine.url.password
    return text


@app.route('/accounts', methods=['POST'])
def create_account():
    name = request.json['name']
    currency = request.json['currency']
    account = Account(name, currency)
    db.session.add(account)
    db.session.commit()
    return format_account(account)

@app.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = Account.query.all()
    return {'accounts': [format_account(account) for account in accounts]}

@app.route('/accounts/<int:id>', methods=['GET'])
def get_account(id):
    account = Account.query.get(id)
    return format_account(account)

@app.route('/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    account = Account.query.get(id)
    account.name = request.json['name']
    db.session.commit()
    return format_account(account)

@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    account = Account.query.get(id)
    db.session.delete(account)
    db.session.commit()
    return format_account(account)

def format_account(account):
    return {
        'id': account.id,
        'name': account.name,
        'account_number': account.account_number,
        'balance': account.balance,
        'currency': account.currency,
        'status': account.status,
        'created_at': account.created_at
    }

@app.route('/sign-in', methods=['POST'])
def sign_in():
    username = request.json['username']
    password = request.json['password']

    print("ADMIN TRIED LOGGING IN", username, password)
    valid = verify_admin(username, password)
    print("VALID:", valid)
    return {'result': valid}

def verify_admin(username, password):
    print("Given:", username, password, "     real:", default_username, default_password, "     result:", username == default_username and password == default_password)
    return username == default_username and password == default_password




@app.route('/users', methods=['POST'])
def create_user():
    print(request.json)
    username = request.json['name']
    password = request.json['password']
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
    return format_user(user)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return {'users': [format_user(user) for user in users]}

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return format_user(user)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    user.username = request.json['username']
    db.session.commit()
    return format_user(user)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return format_user(user)

def format_user(user):
    return {
        'id': user.id,
        'username': user.username,
    }