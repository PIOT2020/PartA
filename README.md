# PartA

Environment Setup

Google Cloud SDK
    Follow Week 7 Tutorial PDF
    Not sure but may need to add Raspberry Pi's global ip address to the Google Cloud Project's authorized list

 Create and Access Virtual Environment 
    *Same as Week 8 Tutorial PDF
    pip3 install virtualenv
    *clone Part A Repo then cd /PartA
    source venv/bin/activate
    *Install any necessary dependencies
    pip3 install flask 
    pip3 install requests
    etc.
    export FLASK_APP=main.py
    flask run --host 192.168.0.1 #Change IP address to your Pi's IP address
