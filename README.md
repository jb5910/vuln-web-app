# Vulnerable Web Application #

## Welcome! ##

<p> Here is my implementation of a vulnerable web application. It uses Flask and a SQL database. To create the database, please execeute the following SQL statements into a running instance of SQL (I used the instance from WAMP)</p>
``` CREATE DATABASE vuln_app; ```
``` CREATE TABLE vuln_app.users(username varchar(12), password varchar(12)); ```

<p> In order for the app to run correctly, Flask and pymysql must be installed.</p>

```pip install flask --user```
```pip install pymysql --user```

<p>In order for the app to run correctly, the SQL server needs to be set up to run on port 3306 with the user 'root' and no password </p>
<p>The app runs on localhost on port 2520</p>
<p>This app has a user log in, and then displays that user's credentials. If the login is invalid, the app responds with an error message.</p>
<p>The app also allows the user to register, and asks for a user name and a password</p>
<p>This app is vulnerable to both weak authentication (passwords are stored in plaintext and have no constraints as to what they can be)</p>
<p>This app is also vulnerable to SQLi</p>

<p>This app also allows the user to just input any string without logging in, and will then display that text back to the user</p>
<p>This part of the app is vulnerable to Template Programming injection (see https://nvisium.com/blog/2015/12/07/injecting-flask.html for reference)</p>