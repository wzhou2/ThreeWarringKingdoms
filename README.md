# ThreeWarringKingdoms: Wei Wen Zhou, Matthew Ming, Jack Lu

[![Build Status](https://travis-ci.org/wzhou2/ThreeWarringKingdoms.svg?branch=master)]

## Instructions to Run:
Click this link to go to our website: [Live Link](http://206.189.184.181/)
### To Run Locally:
1. Open a terminal session.
2. Create your own environment by typing (name is a placeholder for the name of the virtual environment of your choosing):
```
$ python3 -m venv name
```
3. Activate the virtual environment.
```
$ . name/bin/activate
```
4. Clone this repository. If you have already cloned this repository, skip this step. To clone this repo, navigate to the directory you want for this repository to located in. Then clone using HTTP.
```
  (venv)$ git clone https://github.com/wzhou2/ThreeWarringKingdoms.git
```
5. Navigate to our project.
```
$ cd ThreeWarringKingdoms/workbuddy/
```
6. Make sure you have all the dependencies installed in your virtual environment.
```
(venv)$ pip install -r requirements.txt
```
7. Run the python file.
```
(venv)$ python __init__.py
```
8. This should appear in the terminal after running the python file.   
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 248-748-502
```
9. Open a web browser and navigate to the link http://127.0.0.1:5000/.
10. Register if you are a new user or login if you are an existing user and enjoy our web application!

### To Run on Apache2:
1. SSH into your droplet:
```
$ ssh <user>@<ip address>
```
2. Update your packages on your droplet:
```
$ sudo apt update
$ sudo apt upgrade
```
3. Move to the www directory:
```
$ cd /var/www
```
4. Clone the repo via https:
```
$ sudo git clone https://github.com/wzhou2/ThreeWarringKingdoms.git workbuddy
```
5. Move into the repo, add write permisssions, and install requirements:
```
$ cd workbuddy
$ sudo chgrp -R www-data workbuddy
$ sudo chmod -R g+w workbuddy
$ sudo pip3 install -r workbuddy/requirements.txt
```
6. Open the conf file and change the server name to your ip address:
```
$ sudo nano workbuddy.conf
```
7. Move the conf file to the sites-available directory:
```
$ sudo mv /var/www/workbuddy/workbuddy.conf /etc/apache2/sites-available/
```
8. Move to the sites-available directory
```
$ cd /etc/apache2/sites-available/
```
9. Enable the site:
```
$ sudo a2ensite workbuddy.conf
```
10. Enable WSGI module
```
$ sudo a2enmod wsgi
```
11. Restart the apache server:
```
$ sudo service apache2 restart
```
11. Go to your ip address on any browser
