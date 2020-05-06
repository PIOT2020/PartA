# PartA

<h1>Environment Setup</h1>

<h3>Google Cloud SDK</h3>

* Follow Week 7 Tutorial PDF
* Not sure but may need to add Raspberry Pi's global ip address to the Google Cloud Project's authorized list
* Run "curl icanhazip.com"
* Add IP address output to Google Cloud Project > SQL > Connections > Public IP

<h3> Create and Access Virtual Environment</h3>
 
* *Week 8 Tutorial PDF
* pip3 install virtualenv
* *clone Part A Repo then cd /PartA
* source venv/bin/activate
* *Install any necessary dependencies
* pip3 install flask 
* pip3 install requests
* export FLASK_APP=main.py
* flask run --host 192.168.0.1 #Change IP address to your Pi's IP address
