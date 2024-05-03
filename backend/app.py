from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:super@localhost/ticketbuddy'
db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    verification = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer)
    dob = db.Column(db.Date)
    phno = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User(u_id={self.u_id}, user_name='{self.user_name}', email='{self.email}')"
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    @staticmethod
    def create_user(user_name, password):
        new_user = User(user_name=user_name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

def format_user(user):
    return {
        "u_id": user.u_id,
        "verification": user.verification,
        "email": user.email,
        "user_name": user.user_name,
        "age": user.age,
        "dob": user.dob.strftime("%Y-%m-%d") if user.dob else None,
        "phno": user.phno,
        "gender": user.gender,
    }

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return 'Hey!'

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the username already exists
    if User.query.filter_by(user_name=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    # Create a new user
    new_user = User.create_user(username, password)
    formatted_user = format_user(new_user)
    return jsonify({'message': 'User created successfully', 'user': formatted_user}), 201


@app.route("/tk", methods = ['POST'])
def create_tk():
    user_name = request.json['user_name']
    password = request.json['password']
    user = User(user_name, password)
    db.session.add(user)
    db.session.commit()
    return format_user(user)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user_name = data.get('user_name')
    password = data.get('password')

    # Query the database to find the user with the provided username
    user = User.query.filter_by(user_name=user_name).first()

    if user and user.password == password:
        # Username and password are correct
        return jsonify({"message": "Login successful", "user": format_user(user)}), 200
    else:
        # Username or password is incorrect
        return jsonify({"message": "Invalid username or password"}), 401



class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    owner1 = db.Column(db.String(100))

@app.route('/items/<int:item_id>/own', methods=['POST'])
def own_item(item_id):
    data = request.get_json()
    owner_name = data.get('owner_name')  # Retrieve the owner name from the request

    # Find the item by its ID
    item = Item.query.get_or_404(item_id)

    # Update the owner1 column
    item.owner1 = owner_name
    db.session.commit()

    return jsonify({'message': f'Item {item_id} is now owned by {owner_name}'}), 200

if __name__ == '__main__':
    app.run()