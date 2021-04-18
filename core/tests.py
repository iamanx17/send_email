import json
import requests
import os

url='https://credsapi.herokuapp.com/credsapi/?search=emailservice'

#headers={ "Authorization" : os.environ.get('apikey') }

headers={ "Authorization" : "Token 700468c84e4e14acbc47a1a277b66cc653f430bb" }

r=requests.get(url=url,headers=headers)

json_data=r.json()


for json_data in json_data:
    secret_key=json_data['secret_key']
    database_host=json_data['database_host']
    database_user=json_data['database_user']
    database_password=json_data['database_password']
    database_name=json_data['database_name']
