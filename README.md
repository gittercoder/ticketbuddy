
![dy](https://github.com/gittercoder/ticketbuddy/assets/133194085/5cc026b4-d86a-4d5d-9566-7376088376ef)


A closed platform for college students to share their thoughts, ideas, and projects. It includes features such as User Authentication, Real-time chats, posts and a Admin Dashboard for managing posts and channels. 

## APP DEMO



https://github.com/gittercoder/ticketbuddy/assets/133194085/5a7b5499-1b43-4312-a3c5-1519a6de6469






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
