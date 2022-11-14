from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import RequestPing
from pythonping import ping
import os
import re

NA= '104.160.131.102' #works
LAN= 'google.com.mx' #works
EUW= 'www1.sedoparking.com' #works
EUNE= 'google.co.uk' 
BR= 'google.com.br' 
OCE= 'LoL.garena.com' #works
RU= 'google.com.ru'

serversDict= {
    1: NA,
    2: LAN,
    3: EUW,
    4: EUNE,
    5: BR,
    6: OCE,
    7: RU
}
def retreivePing(index):
    server= serversDict[index]
    count=0
    responseList=[]
    while(count < 6):
        ping = os.popen("ping " +  server )
        result = ping.readlines()
        msLine = result[-1].strip()
        msLine= msLine[-9: -1]
        msLine= re.sub(r'[^0-9.]', '', msLine)
        responseList.append(msLine)
        count = count +1
    newList=[
         (1,responseList[0]),
         (2,responseList[1]),
         (3,responseList[2]),
         (4,responseList[3]),
         (5,responseList[4])
         ]
    print (newList)
    return newList

@app.route('/', methods = ['GET', 'POST'])
def index():
    labels = []
    values = []
    server = ''
    i = 0
    form = RequestPing()
    if form.validate_on_submit():
        region = form.rigions.data
        print(region)
        for k in serversDict.keys():
            if k == int(region):
                i = k
                server = serversDict[k]
                print(i)
        data = retreivePing(i)
        labels = [row[0] for row in data]
        values = [row[1] for row in data]   
        print(server)   
    return render_template('base.html', form = form, labels = labels, values = values)