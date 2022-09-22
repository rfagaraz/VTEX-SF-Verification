#!python3
# -*- coding: utf-8 -*-
from sf.salesforce_access import session
from vtex.vtexRequestsSetup import vtexRequestsSetup
from sf.soqlQuery import queryString
import pandas as pd


#Request recent orders json
ordersList = vtexRequestsSetup()

#Create DataFrame with all recent orders
print(ordersList)
orders = pd.DataFrame(ordersList)
print (orders)                                                                                                                                                                                    
orders = orders[orders.paymentNames != "Débito em conta"]
orders = orders[["orderId"]]
orders = orders.reset_index(drop=True)

#Login to Salesforce
client = session()

#Query all recent orders on Salesforce coming from VTEX
report = client.sobjects.query(queryString())
stagingsWithOrders = pd.DataFrame(report)

#Cleanup the DataFrame
stagingsWithOrders = stagingsWithOrders.rename(columns={"For_Future_Use_1__c":"orderId"})
stagingsWithOrders = stagingsWithOrders.drop(columns='attributes', errors='ignore')
stagingsWithOrders = stagingsWithOrders.reset_index(drop=True)


#Check for each line of the DataFrame, which orders have not entered Salesforce as stagings
missingOrders = orders[~orders.apply(tuple,1).isin(stagingsWithOrders.apply(tuple,1))]

#Export DataFrames  
orders.to_excel('orders.xlsx')
stagingsWithOrders.to_excel('stagingsWithOrders.xlsx')
missingOrders.to_excel('missingOrders.xlsx')
