# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:46:04 2020

@author: A691602
"""

import http.client

conn = http.client.HTTPSConnection("circuitsandbox.net")

payload = 'client_id=901ef5597bca4c54b64c899bb859e8c6&client_secret=7de4a58501c5446b9fa423521e8a98eb&grant_type=client_credentials&scope=READ_CONVERSATIONS,READ_USER_PROFILE,WRITE_CONVERSATIONS'

headers = {

  'Content-Type': 'application/x-www-form-urlencoded'

}

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()

data = res.read()

print(data.decode("utf-8"))


#credentials given by MIRA
#Client ID : 75b802ba9888455fb68a08669c88eaff
#Client Secret : 7708158697ba4623aaa2ad8ea2d30e94


#Bot credentials
#client ID:901ef5597bca4c54b64c899bb859e8c6
#client_secret=7de4a58501c5446b9fa423521e8a98eb