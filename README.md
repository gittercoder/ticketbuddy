
![tklogo](https://github.com/gittercoder/ticketbuddy/assets/133194085/089f2fbd-d018-4d01-a48e-40b867b9ec05)



A closed platform for college students to share their thoughts, ideas, and projects. It includes features such as User Authentication, Real-time chats, posts and a Admin Dashboard for managing posts and channels. 

## APP DEMO





https://github.com/gittercoder/ticketbuddy/assets/133194085/c5a9ce7d-05ca-44d7-9439-c88a763a6240







## Installation Guide

### Requirements
- [Node.js](https://nodejs.org/) (make sure npm is also installed)
- [Python](https://www.python.org/) (for Flask)
- [PostgreSQL](https://www.postgresql.org/) database server

Both should be installed and make sure mongodb is running.
### Installation
Fork this repo : https://github.com/gittercoder/ticketbuddy

```shell
git clone https://github.com/gittercoder/ticketbuddy
cd Unigram
```
#### FRONTEND
Navigate to frontend
```shell
cd frontend
npm start
```

#### BACKEND
Navigate to backend in another console
```shell
cd backend
```
- Connecting to database<br/>
In line 14 of app.py, change username, password and dbname of postgresql to your own.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'

- Install dependencies and run
```shell
pip install -r requirements.txt
flask run
```

open http://localhost:3000  in your browser to access the website.
<br/>




## Contributions

Contributions are welcome! Feel free to create and work on issues to develop this project.

Happy coding and thank you for contributing! 
