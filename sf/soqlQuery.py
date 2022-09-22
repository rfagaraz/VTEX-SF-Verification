#!python3
# -*- coding: utf-8 -*-

def queryString():
    criteria = { 'date':'createdDate = This_Week',
                 "vtex_order":"For_Future_Use_1__c != ''"}
    
    exhibitedFields = ["Id", 
                       "For_Future_Use_1__c"]
    
    objects = ["s360aie__Staging__c"]

    queryString = f"SELECT {exhibitedFields[1]} FROM {objects[0]} WHERE {criteria['date']} AND {criteria['vtex_order']}"
    
    return queryString