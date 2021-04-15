import json
import requests
import os

url='https://apihouse.herokuapp.com/credsapi/?search=send_email'

#headers={ "Authorization" : os.environ.get('apikey') }

headers={ "Authorization" : "Token a1c6d310cfe6ef987e66394bc86c63066dd22160" }

r=requests.get(url=url,headers=headers)

json_data=r.json()


for json_data in json_data:
    secret_key=json_data['secret_key']
    database_host=json_data['database_host']
    database_user=json_data['database_user']
    database_password=json_data['database_password']
    database_name=json_data['database_name']
