#!python3
# -*- coding: utf-8 -*-
import base64
import requests
import datetime as date
import json

#How many days back from today the script will request
days = -3






today = date.datetime.today().strftime("%Y-%m-%dT%H:%M:%S.000Z")
datePast = date.datetime.today() + date.timedelta(days=days)
past = datePast.strftime("%Y-%m-%dT%H:%M:%S.000Z")


def vtexRequestsSetup():
    url = "https://greenpeace.myvtex.com/api/oms/pvt/orders/"
    ordersList = []
    
    newResults = True
    headers = {
    "content-type": "application/json",
    "accept": "application/json",
    "X-VTEX-API-AppKey": "",
    "X-VTEX-API-AppToken": ""
}
    params = {
    "f_creationDate":f"creationDate:[{past} TO {today}]",
    'per_page':'30',
    'f_status':'ready-for-handling'
}   
    page = 1
    while newResults:
        call = requests.get(url+f"?page={page}",headers = headers, params = params).json()
        newResults = call.get("list", [])
        ordersList.extend(newResults)
        page += 1      
    
    return ordersList