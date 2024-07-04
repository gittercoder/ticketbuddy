from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy
import time
from datetime import datetime, timedelta
from flask_cors import CORS
from sqlalchemy import event
from sqlalchemy import asc
from flask_mail import Mail,Message
import random
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
app.config['SECRET_KEY']='secretkey'
db = SQLAlchemy(app)
CORS(app)
bcrypt=Bcrypt(app)

class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True)
    verification = db.Column(db.Integer, default=0)
    email = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.String(100), unique=True, nullable=False)
    # name = db.Column(db.String(100), default=None)
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

@app.route('/user', methods=['GET'])
def get_user_id():
    username = request.args.get('username')
    if not username:
        return jsonify({'error': 'Username not provided'}), 400

    user = User.query.filter_by(user_name=username).first()
    if user:
        return jsonify({'u_id': user.u_id}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
    
with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return 'Hey!'

# @app.route('/signup', methods=['POST'])
# def signup():
#     username = request.json['username']
#     password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')

#     # Check if the username already exists
#     if User.query.filter_by(user_name=username).first():
#         return jsonify({'error': 'Username already exists'}), 400

#     # Create a new user
#     new_user = User.create_user(username, password)
#     formatted_user = format_user(new_user)
#     return jsonify({'message': 'User created successfully', 'user': formatted_user}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user_name = data.get('user_name')
    password = data.get('password')

    # Query the database to find the user with the provided username
    user = User.query.filter_by(user_name=user_name).first()

    if user and bcrypt.check_password_hash(user.password,password):
        # Username and password are correct
        return jsonify({"message": "Login successful", "user": format_user(user)}), 200
    else:
        # Username or password is incorrect
        return jsonify({"message": "Invalid username or password"}), 401


# creating Venue table


class Venue(db.Model):
    v_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    r_capacity = db.Column(db.Integer)
    p_capacity = db.Column(db.Integer)
    location = db.Column(db.String(255))

    def __repr__(self):
        return f"Venue(v_id={self.v_id}, r_capacity={self.r_capacity}, p_capacity={self.p_capacity}, location='{self.location}')"

    def __init__(self, r_capacity, p_capacity, location):
        self.r_capacity = r_capacity
        self.p_capacity = p_capacity
        self.location = location



# Route to get sample values
@app.route('/cvenues', methods=['GET'])
def create_sample_venues():
    # Insert sample values into the Venue table
    sample_venues = [
        Venue(r_capacity=100, p_capacity=50, location='Sample Location 1'),
        Venue(r_capacity=150, p_capacity=70, location='Sample Location 2'),
        Venue(r_capacity=120, p_capacity=60, location='Sample Location 3'),
        Venue(r_capacity=80, p_capacity=40, location='Sample Location 4'),
        Venue(r_capacity=200, p_capacity=100, location='Sample Location 5'),
        Venue(r_capacity=90, p_capacity=45, location='Sample Location 6')
    ]
    db.session.add_all(sample_venues)
    db.session.commit()

    return "Sample venues inserted successfully!"




# creating Event table
        

class Event(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    v_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    date = db.Column(db.Date)
    datetime = db.Column(db.DateTime)  # Added datetime column
    r_price = db.Column(db.Float)
    p_price = db.Column(db.Float)
    image_link = db.Column(db.String(255))  # New column for image link
    status = db.Column(db.String(50),default='notcompleted')  # New column for status

    def __repr__(self):
        return f"Event(e_id={self.e_id}, v_id={self.v_id}, name='{self.name}', genre='{self.genre}', date='{self.date}', datetime='{self.datetime}', r_price={self.r_price}, p_price={self.p_price}, image_link='{self.image_link}', status='{self.status}')"

    def __init__(self, v_id, name, genre, date, datetime, r_price, p_price, image_link):  # Modify __init__ to include datetime and image_link
        self.v_id = v_id
        self.name = name
        self.genre = genre
        self.date = date
        self.datetime = datetime  # Added datetime attribute
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


        

class Ticket(db.Model):
    t_id = db.Column(db.Integer, primary_key=True)
    e_id = db.Column(db.Integer)
    price = db.Column(db.Float)
    bid_price = db.Column(db.Float)
    owner = db.Column(db.Integer)
    f_owner = db.Column(db.Integer)
    category = db.Column(db.String(50))
    refund=db.Column(db.Float, default=0) 

    def __repr__(self):
        return f"Ticket(t_id={self.t_id}, e_id={self.e_id}, price={self.price}, bid_price={self.bid_price}, owner='{self.owner}', f_owner='{self.f_owner}', category='{self.category}')"
    
class Bid(db.Model):
    b_id=db.Column(db.Integer, primary_key=True)
    bid_amount=db.Column(db.Float)
    e_id=db.Column(db.Integer)
    u_id=db.Column(db.Integer)

    def __init__(self,bid_amount,e_id,u_id):
        self.bid_amount=bid_amount
        self.e_id=e_id
        self.u_id=u_id        

# initializing tables
    

with app.app_context():
    db.create_all()




@app.route('/cevent', methods=['GET'])
def create_sample_events():
    # Insert sample values into the Event table
    sample_events = [
        Event(
            v_id=2,
            name='Sonu Nigam',
            genre='Example Genre 1',
            date=datetime(2024, 5, 19).date(),  # Assuming you want the date part of the datetime
            datetime=datetime(2024, 5, 19, 10, 0, 0),  # Assign the datetime value
            r_price=20.0,
            p_price=30.0,
            image_link="https://blackhattalent.com/wp-content/uploads/2023/07/sonu-nigam-ready-to-belt-out-new-ghazal-titled-yaad-01.jpg"
        ),
        Event(
            v_id=3,
            name='Erykah Badu',
            genre='Example Genre 2',
            date=datetime(2024, 5, 20).date(),
            datetime=datetime(2024, 5, 20, 10, 0, 0),
            r_price=25.0,
            p_price=35.0,
            image_link="https://www.rollingstone.com/wp-content/uploads/2024/02/stray-kids-topline.jpg?w=1024"
        ),
        Event(
            v_id=2,
            name='Stray Kids',
            genre='Example Genre 1',
            date=datetime(2024, 5, 19).date(),  # Assuming you want the date part of the datetime
            datetime=datetime(2024, 6, 19, 10, 0, 0),  # Assign the datetime value
            r_price=20.0,
            p_price=30.0,
            image_link="https://www.rollingstone.com/wp-content/uploads/2024/02/Erykah-Badu-25-stylish.jpg?w=1024"
        ),
        Event(
            v_id=3,
            name='Lil Uzi Vert',
            genre='Example Genre 2',
            date=datetime(2024, 5, 26).date(),
            datetime=datetime(2024, 5, 20, 10, 0, 0),
            r_price=25.0,
            p_price=35.0,
            image_link="https://www.rollingstone.com/wp-content/uploads/2024/02/lil-uzi-25-stylish.jpg?w=1024"
        ),
        Event(
            v_id=2,
            name='Troye Sivan',
            genre='Example Genre 1',
            date=datetime(2024, 5, 29).date(),  # Assuming you want the date part of the datetime
            datetime=datetime(2024, 5, 19, 10, 0, 0),  # Assign the datetime value
            r_price=20.0,
            p_price=30.0,
            image_link="https://www.rollingstone.com/wp-content/uploads/2024/02/troy-sivan-25-stylish.jpg?w=1024"
        ),
        Event(
            v_id=3,
            name='070 Shake',
            genre='Example Genre 2',
            date=datetime(2024, 5, 25).date(),
            datetime=datetime(2024, 5, 20, 10, 0, 0),
            r_price=25.0,
            p_price=35.0,
            image_link="https://www.rollingstone.com/wp-content/uploads/2024/02/070-25-stylish.jpg?w=1024"
        )
        # Add more events here...
    ]
    db.session.add_all(sample_events)
    db.session.commit()

    return "Sample events inserted successfully!"


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
        # Perform search based on the search query and filter by status
        events = Event.query.filter(Event.name.ilike(f'%{search_query}%'), Event.status != 'completed').all()
    else:
        # If no search query is provided, return all events excluding completed ones
        events = Event.query.filter(Event.status != 'completed').all()

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


# search event details
@app.route('/ee', methods=['GET'])
def get_event_details():
    e_id = request.args.get('e_id') 
    event = Event.query.filter_by(e_id=e_id).first()
    if event:
        event_details = {
            'e_id': event.e_id,
            'v_id': event.v_id,
            'name': event.name,
            'genre': event.genre,
            'date': event.date.strftime('%Y-%m-%d'),  # Convert date to string
            'datetime': event.datetime.strftime('%Y-%m-%d %H:%M:%S'),  # Convert datetime to string
            'r_price': event.r_price,
            'p_price': event.p_price,
            'image_link': event.image_link,
            'status': event.status
        }    
        return jsonify(event_details)
    else:
        return jsonify({'error': 'Event not found'}), 404

# search event details and ticket details
     
@app.route('/gte', methods=['GET'])
def gte():
    user_id = request.args.get('u_id')
    if user_id is None:
        return jsonify({'error': 'User ID not provided'}), 400
    
    # Perform a join operation to fetch ticket details along with event name and date
    ticket_details = db.session.query(Ticket, Event.name, Event.date).join(Event, Ticket.e_id == Event.e_id).filter(Ticket.owner == user_id).all()

    # Construct the response
    tickets_info = []
    for ticket, event_name, event_date in ticket_details:
        ticket_info = {
            't_id': ticket.t_id,
            'event_name': event_name,
            'event_date': str(event_date),  # Convert date object to string
            'price': ticket.price,
            'bid_price': ticket.bid_price,
            'owner': ticket.owner,
            'f_owner': ticket.f_owner,
            'category': ticket.category,
            'refund': ticket.refund
        }
        tickets_info.append(ticket_info)

    return jsonify(tickets_info)

# search event details and ticket details for compensation
     
@app.route('/gtec', methods=['GET'])
def gtec():
    user_id = request.args.get('u_id')
    if user_id is None:
        return jsonify({'error': 'User ID not provided'}), 400
    
    # Perform a join operation to fetch ticket details along with event name and date
    ticket_details = db.session.query(Ticket, Event.name, Event.date).join(Event, Ticket.e_id == Event.e_id).filter(Ticket.f_owner == user_id, Ticket.owner.isnot(None), Ticket.owner != Ticket.f_owner).all()

    # Construct the response
    tickets_info = []
    for ticket, event_name, event_date in ticket_details:
        ticket_info = {
            't_id': ticket.t_id,
            'event_name': event_name,
            'event_date': str(event_date),  # Convert date object to string
            'price': ticket.price,
            'bid_price': ticket.bid_price,
            'owner': ticket.owner,
            'f_owner': ticket.f_owner,
            'category': ticket.category,
            'refund': ticket.refund
        }
        tickets_info.append(ticket_info)

    return jsonify(tickets_info)

# Create an endpoint to fetch ticket details based on the user ID
@app.route('/gt', methods=['GET'])
def gt():
    u_id = request.args.get('u_id') 
    if u_id is None:
        return jsonify({'error': 'User ID not provided'}), 400
    
    tickets = Ticket.query.filter_by(owner=u_id).all()
    if tickets:
        ticket_details = [{
            't_id': ticket.t_id,
            'e_id': ticket.e_id,
            'price': ticket.price,
            'bid_price': ticket.bid_price,
            'owner': ticket.owner,
            'f_owner': ticket.f_owner,
            'category': ticket.category
        } for ticket in tickets]
        return jsonify(ticket_details)
    else:
        return jsonify({'error': 'No tickets found for the user'}), 404

# Create an endpoint to handle canceling a ticket
@app.route('/cancel_ticket', methods=['POST'])
def cancel_ticket():
    data = request.json
    ticket_id = data.get('t_id')
    print(ticket_id)
    if ticket_id is None:
        return jsonify({'error': 'Ticket ID not provided'}), 400
    
    # Update the owner of the ticket to null
    ticket = Ticket.query.get(ticket_id)
    if ticket:
        ticket.owner = None
        db.session.commit()
        return jsonify({'message': 'Ticket canceled successfully'}), 200
    else:
        return jsonify({'error': 'Ticket not found'}), 404



@app.route('/no_auction',methods=['POST'])
def no_auction():
    data = request.json
    t_id=data.get('t_id')
    e_id=data.get('e_id')
    u_id=data.get('u_id')
    bid=Bid.query.filter_by(u_id=u_id).count()
    if bid+len(t_id)<=10:
        for i in t_id:
            ticket = Ticket.query.filter_by(t_id=i).first()
            ticket.bid_price=ticket.price
            ticket.f_owner=u_id
            bid=Bid(bid_amount=ticket.price,e_id=e_id,u_id=u_id,)
            db.session.add(bid)
        db.session.commit()
    return jsonify({"message":"Ticket selected"})

@app.route('/auction',methods=['POST'])
def auction():
    data=request.json
    bid_amt=data.get('bid_amt')
    e_id=data.get('e_id')
    u_id=data.get('u_id')
    bid=Bid.query.filter_by(e_id=e_id,u_id=u_id).order_by(asc(Bid.bid_amount)).first()
    if bid:
        if bid_amt>bid.bid_amount:
            bid.bid_amount=bid_amt
        else:
            return jsonify({"message":"Bid amount less than previous bid"})
    else:
        bid=Bid(bid_amount=bid_amt,e_id=e_id,u_id=u_id)
        db.session.add(bid)
    db.session.commit()
    return jsonify({"message": "Bid placed successfully"}), 200

@app.route('/auction_result',methods=['POST'])
def get_auction_result():
    e_id=request.json['e_id']
    bids = Bid.query.filter_by(e_id=e_id).order_by(Bid.bid_amount.desc()).all()
    data=list()
    for bid in bids:
        bid_for={"b_id":bid.b_id,"bid_amount":bid.bid_amount,"e_id":bid.e_id,"u_id":bid.u_id}
        data.append(bid_for)
    return jsonify(data)

def check_auction_end():
    event=Event.query.all()
    for i in event:
        if datetime.now()>=i.datetime-timedelta(days=1) and i.status=="notcompleted":
            i.status="completed"
            bid = Bid.query.filter_by(e_id=i.e_id).order_by(Bid.bid_amount.desc()).all()
            ticket=Ticket.query.filter_by(e_id=i.e_id).order_by(Ticket.t_id.desc()).all()
            bl=len(bid)
            tl=len(ticket)
            if bl>tl:
                for j in range(tl):
                    ticket[j].owner=bid[j].u_id
                    ticket[j].bid_price=bid[j].bid_amount
                db.session.commit()
                bsum=0
                asum=0
                ticket2=Ticket.query.filter_by(e_id=i.e_id).all()
                for j in ticket2:
                    bsum+=j.price
                    asum+=j.bid_price
                diff=asum-bsum
                cp=0.2*diff
                refund=cp/tl
                for j in ticket2:
                    j.refund=j.price+refund
                db.session.commit()
            else:   
                ticket2=Ticket.query.filter_by(e_id=i.e_id).all()
                for j in ticket2:
                    j.owner=j.f_owner
                db.session.commit()


@app.route('/auction_end')
def auction_end():
    while True:
        print("Running")
        check_auction_end()
        time.sleep(60)


from flask_mail import Mail,Message
import random

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']='ticketbuddyinfo@gmail.com'
app.config['MAIL_PASSWORD']='ofnrqpfdxyzfeoxv'
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False

mail=Mail(app)

# Generate otp
def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

# Notification service
class NotificationService:
    def __init__(self,mail):
        self.mail=mail

    def send_mail(self,recipients,subject,body):
        msg=Message(subject,sender='ticketbuddyinfo@gmail.com',recipients=recipients)
        msg.body=body
        self.mail.send(msg)
        return True

    def send_verification_mail(self,recipients,otp):
        subject=f'{otp} is your verification code.'
        body=f'Thank you for signing up in TicketBuddy!Please find below the confirmation code to complete your sign-up:\n{otp}\n\n\nDo not reply to this message.'
        msg=Message(subject,sender='ticketbuddyinfo@gmail.com',recipients=recipients)
        msg.body=body
        self.mail.send(msg)
        return True

    def send_welcome_mail(self,recipients):
        subject='Welcome to TicketBuddy'
        body='Welcome to TicketBuddy, your VIP pass to event bliss. Never miss your favorite show again.\n\n\nDo not reply to this message.'
        msg=Message(subject,sender='ticketbuddyinfo@gmail.com',recipients=recipients)
        msg.body=body
        self.mail.send(msg)
        return True

    def send_x_mail(self,recipients):
        subject=''
        body=''
        msg=Message(subject,sender='ticketbuddyinfo@gmail.com',recipients=recipients)
        msg.body=body
        self.mail.send(msg)
        return True





@app.route('/signup', methods=['POST'])
def signup():
    
    data = request.json
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    phno = data.get('phone')
    email = data.get('email')
    dob = data.get('age')
    gender = data.get('gender')
    otp_user=data.get('otp')
    
    if username and password:
        # User registration
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        if User.query.filter_by(user_name=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        new_user = User.create_user(username, password_hash)
        formatted_user = format_user(new_user)

        return jsonify({'message': 'User created successfully', 'user': formatted_user}), 201
    
    elif name and email:
        otp=generate_otp()
        user = User.query.filter_by(user_name=username).first()
        #user.name = name
        user.phno = phno
        user.email = email
        user.dob = dob
        user.gender = gender
        user.verification=otp
        db.session.commit()
        send_email = NotificationService(mail)
        send_email.send_verification_mail(recipients=[email], otp=otp)
        return jsonify({"message":"user update data received"})
    
    elif otp_user:
        user = User.query.filter_by(user_name=username).first()
        if user.verification==int(otp_user):
            send_email = NotificationService(mail)
            send_email.send_welcome_mail(recipients=[email])
            return jsonify({"message":"user verified and updated"})
        else:
            user = User.query.filter_by(user_name=username).first()
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message":"error"})
        
    return jsonify({"message":"error"})



if __name__ == '__main__':
    app.run()
