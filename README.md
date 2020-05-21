# PartA

<h1>Environment Setup</h1>

<h3>Google Cloud SDK</h3>

* Follow Week 7 Tutorial PDF
* Not sure but may need to add Raspberry Pi's global ip address to the Google Cloud Project's authorized list
* Run "curl icanhazip.com"
* Add IP address output to Google Cloud Project > SQL > Connections > Public IP

<h3> Create and Access Virtual Environment</h3>
 
* pip3 install virtualenv
* *clone Part A Repo then cd /PartA
* python3 -m venv venv
* source venv/bin/activate
* pip3 install flask 
* pip3 install requests
* pip3 install mysqlclient
* pip3 install mariadb
* export FLASK_APP=main.py
* flask run --host 192.168.0.1 #Change IP address to your Pi's IP address
