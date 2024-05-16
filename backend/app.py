from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from sqlalchemy import event


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


# creating Venue table

class Venue(db.Model):
    v_id = db.Column(db.Integer, primary_key=True)
    r_capacity = db.Column(db.Integer)
    p_capacity = db.Column(db.Integer)
    location = db.Column(db.String(255))

    def __repr__(self):
        return f"Venue(v_id={self.v_id}, r_capacity={self.r_capacity}, p_capacity={self.p_capacity}, location='{self.location}')"

    def __init__(self, r_capacity, p_capacity, location):
        self.r_capacity = r_capacity
        self.p_capacity = p_capacity
        self.location = location


# creating Event table
        

class Event(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    v_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    date = db.Column(db.Date)
    r_price = db.Column(db.Float)
    p_price = db.Column(db.Float)
    image_link = db.Column(db.String(255))  # New column for image link

    def __repr__(self):
        return f"Event(e_id={self.e_id}, v_id={self.v_id}, name='{self.name}', genre='{self.genre}', date='{self.date}', r_price={self.r_price}, p_price={self.p_price}, image_link='{self.image_link}')"

    def __init__(self, v_id, name, genre, date, r_price, p_price, image_link):  # Modify __init__ to include image_link
        self.v_id = v_id
        self.name = name
        self.genre = genre
        self.date = date
        self.r_price = r_price
        self.p_price = p_price
        self.image_link = image_link

    def create_tickets(self):
        venue = Venue.query.get(self.v_id)
        if venue:
            r_tickets_count = min(venue.r_capacity, 250)  
            p_tickets_count = min(venue.p_capacity, 50)  

            tickets = []

            # Create regular tickets
            for _ in range(r_tickets_count):
                ticket = Ticket(e_id=self.e_id, price=self.r_price, category='Regular')
                tickets.append(ticket)

            # Create premium tickets
            for _ in range(p_tickets_count):
                ticket = Ticket(e_id=self.e_id, price=self.p_price, category='Premium')
                tickets.append(ticket)

            # Add all tickets to the session
            db.session.add_all(tickets)


# creating Ticket table
        

class Ticket(db.Model):
    t_id = db.Column(db.Integer, primary_key=True)
    e_id = db.Column(db.Integer)
    price = db.Column(db.Float)
    bid_price = db.Column(db.Float)
    owner = db.Column(db.Integer)
    f_owner = db.Column(db.Integer)
    category = db.Column(db.String(50))  

    def __repr__(self):
        return f"Ticket(t_id={self.t_id}, e_id={self.e_id}, price={self.price}, bid_price={self.bid_price}, owner='{self.owner}', f_owner='{self.f_owner}', category='{self.category}')"
    
class Bid(db.Model):
    b_id=db.Column(db.Integer, primary_key=True)
    bid_amount=db.Column(db.Float)
    e_id=db.Column(db.Integer)
    u_id=db.Column(db.Integer)

    def __init__(self,bid_amount,e_id,u_id,category):
        self.bid_amount=bid_amount
        self.e_id=e_id
        self.u_id=u_id        
        self.category=category

# initializing tables
    

with app.app_context():
    db.create_all()




@app.route('/cevent')
def index():
    image_link = "https://blackhattalent.com/wp-content/uploads/2023/07/sonu-nigam-ready-to-belt-out-new-ghazal-titled-yaad-01.jpg"

    event = Event(
        v_id=1,
        name='Example Event',
        genre='Example Genre',
        date='2024-05-15',
        r_price=20.0,
        p_price=30.0,
        image_link=image_link  # Assign the image link
    )
    db.session.add(event)
    db.session.commit()

    return 'Event created successfully'


@event.listens_for(Event, 'after_insert')
def event_after_insert(mapper, connection, target):
    target.create_tickets()

# for layout 

@app.route('/api/tickets')
def get_tickets():
    e_id = request.args.get('e_id')  # Get e_id from query parameters
    if e_id is None:
        return jsonify({'error': 'e_id parameter is required'}), 400
    
    # Filter tickets based on e_id
    tickets = Ticket.query.filter_by(e_id=e_id).all()
    
    ticket_data = [
        {
            't_id': ticket.t_id,
            'e_id': ticket.e_id,
            'price': ticket.price,
            'bid_price': ticket.bid_price,
            'owner': ticket.owner,
            'f_owner': ticket.f_owner,
            'category': ticket.category
        }
        for ticket in tickets
    ]
    return jsonify(ticket_data)

# Route to fetch events
@app.route('/api/event')
def get_event():
    search_query = request.args.get('search')
    if search_query:
        # Perform search based on the search query
        events = Event.query.filter(Event.name.ilike(f'%{search_query}%')).all()
    else:
        # If no search query is provided, return all events
        events = Event.query.all()

    return jsonify([{
        'e_id': event.e_id,
        'v_id': event.v_id,
        'name': event.name,
        'genre': event.genre,
        'date': event.date.strftime('%Y-%m-%d'),
        'r_price': event.r_price,
        'p_price': event.p_price,
        'image_link': event.image_link
    } for event in events])


@app.route('/auction_result',methods=['POST'])
#@login_required
def get_auction_result():
    e_id=request.json['e_id']
    bids = Bid.query.filter_by(e_id=e_id).order_by(Bid.bid_amount.desc()).all()
    data=list()
    for bid in bids:
        bid_for={"b_id":bid.b_id,"bid_amount":bid.bid_amount,"e_id":bid.e_id,"u_id":bid.u_id}
        data.append(bid_for)
    return jsonify(data)

if __name__ == '__main__':
    app.run()