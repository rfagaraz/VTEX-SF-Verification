#!python3
# -*- coding: utf-8 -*-
from salesforce_api import Salesforce

def session():
    client = Salesforce(username= "",
                        password= "",
                        security_token= "",
                        is_sandbox=False)
    return client
