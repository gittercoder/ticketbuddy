
![2024-07-04 15_26_04-Free Logo Maker - Get Custom Logo Designs in Minutes _ Looka](https://github.com/gittercoder/ticketbuddy/assets/133194085/1712eb76-8c1b-4d73-8db0-2cdc273afa5b)


A closed platform for college students to share their thoughts, ideas, and projects. It includes features such as User Authentication, Real-time chats, posts and a Admin Dashboard for managing posts and channels. 

## APP DEMO





https://github.com/gittercoder/ticketbuddy/assets/133194085/c5a9ce7d-05ca-44d7-9439-c88a763a6240







## Installation Guide

### Requirements
- [Nodejs](https://nodejs.org/en/download)
- [Mongodb](https://www.mongodb.com/docs/manual/administration/install-community/)

Both should be installed and make sure mongodb is running.
### Installation
Fork this repo : https://github.com/Vijaykv5/Unigram
#### First Method
```shell
git clone https://github.com/your-user-name/Unigram
cd Unigram
```
Now Create an env file .env for your Mongodb String
```shell
cd server
export MONGODB_URL="<Your-MongoDb-String>"
cd ..
```

Now install the dependencies
```shell
cd client
npm install
cd ..
cd server
npm install
```
We are almost done, Now just start the development server.

For Frontend.
```shell
cd client
npm start
```
For Backend.

Open another terminal in folder, Also make sure mongodb is running in background.
```shell
cd server
npm start
```
Done! Now open localhost:5173 in your browser.
<br/>
You can see your frontend running sucessfully!

#### Second Method
- This method requires docker and docker-compose to be installed in your system.
- Make sure you are in the root of your project and run the following command.

```shell
docker compose build --no-cache
```
after the build is complete run the containers using the following command
```shell
docker compose up
```
now open localhost:5173 in your browser.


# Contributions are welcome! 

Please create and work over the issues if you would love to contribute to this project.

Happy coding ⭐
