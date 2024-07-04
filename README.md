


https://github.com/gittercoder/ticketbuddy/assets/133194085/5fb95095-3b52-4e93-bb1b-565b7aa0bb90


TicketBuddy provides a dynamic platform for entities to sell tickets to their events, with a compensation mechanism that allows individuals to potentially profit from its auctioning system. It facilitates event ticket allocation, bidding, and returns, offering real-time bid processing, efficient ticket return management, and a seamless user experience.


## APP DEMO



https://github.com/gittercoder/ticketbuddy/assets/133194085/c5a9ce7d-05ca-44d7-9439-c88a763a6240




## Installation Guide

### Requirements
- [Node.js](https://nodejs.org/) (make sure npm is also installed)
- [Python](https://www.python.org/) (for Flask)
- [PostgreSQL](https://www.postgresql.org/) (database server)


### Installation
Fork this repo : https://github.com/gittercoder/ticketbuddy

```shell
git clone https://github.com/gittercoder/ticketbuddy
cd ticketbuddy
```
#### FRONTEND
Navigate to frontend
```shell
cd frontend
npm start
```

#### BACKEND
Navigate to backend in another console:
```shell
cd backend
```
- Connecting to database:<br/><br/>
First, make sure PostgreSQL is running on your system.<br/><br/>
Then, in line 14 of `app.py`, change the username, password, and database name(dbname) to your own PostgreSQL credentials.<br/>
```shell
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
```  
- Install dependencies and start the backend:
```shell
pip install -r requirements.txt
flask run
```

open http://localhost:3000  in your browser to access the website.
<br/>

#### Inserting Dummy Events

Create dummy venues to the database after starting the backend, using get request through postman or browser to the below url:<br>
http://127.0.0.1:5000/cvenues<br><br>
To display events you can insert dummy events to the database, using get request through postman or browser to the below url:<br>
http://127.0.0.1:5000/cevent1



## Contributions

Contributions are welcome! Feel free to create and work on issues to develop this project.

Happy coding and thank you for contributing! 
