# Biosecurity
COMP639 Studio Project – Semester 1 2024 Individual Assignment 
**Table of contents**

**Table of contents**

- [Project Focus](#project-focus)
- [Principles](#principles)
- [Requirements](#requirements)
- [Getting started](#getting-started)

## Project Focus

This is a Flask Python Web App functioning as a biosecurity guide, providing information on animal
pests present in New Zealand.

## View my Web and Use introduction: Important!!!

First, please log into my PythonAnywhere account for me. The account username is: Clarazheng111, and the password is also: Clarazheng111.


After logging in, click on "Web", then click "Reload: Clarazheng111.pythonanywhere.com". Next, open "Configuration for: Clarazheng111.pythonanywhere.com". 

Just wait a moment, and you will be able to access the webpage I created on the topic of Biosecurity. 

And then, on the Home page, there are many pest images connected to the database. Lightly tapping on these images will display their ID, and there’s an arrow below indicating that you can click to view the description inside.

Then, by pressing the ‘LogInOut’ button, you can register as a user and select a role. After registering, you can log in with your username and password into different role panels.

Afterward, once logged in, your login information will be displayed in the Profile section.

As well,You can hover your mouse over the images on the homepage. By clicking "more", you can see information about the pictures. 


## Principles

- **Flask**: Flask provides configuration and conventions, with sensible defaults, to get started. This section of the documentation explains the different parts of the Flask framework and how they can be used, customized, and extended. Beyond Flask itself, look for community-maintained extensions to add even more functionality.

- **MySQL**: MySQL is a popular open-source relational database management system known for its reliability, performance, and ease of use, making it a top choice for web applications.

- **Bootstrap**: Bootstrap is a free and open-source front-end framework for designing websites and web applications. It offers responsive grid systems, pre-designed components, and powerful JavaScript plugins, enabling rapid and efficient development of aesthetically pleasing and mobile-first designs.

## Requirements

1.Initialize Python environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2.Initialize MySQL

```bash
sudo service start mysql start
mysql -h localhost -u root -p
CREATE DATABASE pest;
CREATE USER 'pest_admin'@'%' IDENTIFIED BY 'qwer1234';
GRANT ALL PRIVILEGES ON pest.* TO 'pest_admin'@'%';
FLUSH PRIVILEGES;
```

## Registered usernames and passwords

- Admin :
    - Username: clara
    - password: 012

- Staff :
    - Username: monica
    - password: 123  

    - Username: joey
    - password: 234

    - Username: cynthia
    - password: 345

    - Username: Charles
    - password: 456

- PestController :
    - Username: david
    - password: 567

    - Username: judy
    - password: 678

    - Username: joy
    - password: 789

    - Username: lucy
    - password: 890

    - Username: sandy
    - password: 0123

    - Username: sarah
    - password: 1234


## References:

All the pictures from: https://www.mpi.govt.nz/biosecurity/pests-and-diseases-not-in-new-zealand/priority-list-of-potentially-invasive-pests-and-diseases/

https://www.mpi.govt.nz/biosecurity/exotic-pests-and-diseases-in-new-zealand/long-
<!-- ## Getting started

1. run flask

```bash
python3 app.py
```

<!-- 2. Invoke an initialization routing function, only once

```bash
Navigate to localhost:5000/initdb in your web browser to initialize the data.
``` -->

<!-- 3.Register user

```bash
Navigate to localhost:5000/register in your web browser.
```

4.Visit Home

```bash
Navigate to localhost:5000/page/index or localhost:5000/
``` --> 
