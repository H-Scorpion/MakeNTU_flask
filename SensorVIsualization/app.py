#debug
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)

Blue = 29
Pink = 31

debug
GPIO.setmode(GPIO.BOARD)
# set up pin 11 as an output
GPIO.setup(Blue, GPIO.OUT)
GPIO.setup(Pink, GPIO.OUT)

# @app.route('/', methods=["GET", "POST"])
# def main():
#     print('state3')
#     return render_template('index.html')


# @app.route('/data', methods=["GET", "POST"])
# def data():
#     # Data Format [ Time, Velocity, SOC]
#     Velocity = random()*150  
#     SOC = random()*100
#     # rfid num: id
#     rfid_dic={       
#         385426309652 : 0
#     }
    
#     tmp1=input("id")
#     tmp2=input("status")
#     tmp3=input("tmp3")

#     # id mapping 
#     # 0:wallet
#     # 1:phone
    

#     #data = [time() * 1000, Velocity, SOC]
#     data = [tmp1,tmp2,tmp3]
#     #define variable rfid_recv

#     # rfid_recv = [ id , status , 0]

#     #response = make_response(json.dumps(rfid_recv))
#     response = make_response(json.dumps(data))
#     response.content_type = 'application/json'

#     return response


# if __name__ == "__main__":
#     print(__name__)
#     app.run(debug=True, port=8888)

@app.route('/data', methods=["GET", "POST"])
def data():
    print('state1')
    
    reader = SimpleMFRC522()
    GPIO.output(Blue,False)
    GPIO.output(Pink,True)
    id, text = reader.read()
    
    # rfid num: id
    rfid_dic={
            385426309652 : 3,
            896299244541 : 4
            }
    
    # Data Format [ Time, Velocity, SOC]
    
    if text != ' ':
        GPIO.output(Pink,False)
        GPIO.output(Blue,True)
        print(id)
        print(text)
        data = [rfid_dic[id], text, time.time()]
        time.sleep(1)
        
    print('state2')
    response = make_response(json.dumps(data))
        
    response.content_type = 'application/json'
        
    return response


if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        GPIO.cleanup()
    
