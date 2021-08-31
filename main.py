import requests
from datetime import datetime

PIXELA_ENDPOINT="https://pixe.la/v1/users"
USERNAME=Your_Name
TOKEN=Your_Own_Token

users_paramas={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
######_____CREATING USER ACCOUNT____#####

# response=requests.post(url=PIXELA_ENDPOINT,json=users_paramas)
# print(response.text)

GRAPH_ENDPOINT=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID="graph1"
graph_config={
    "id":GRAPH_ID,
    "name":"Hours Of Coding",
    "unit":"hr",
    "type":"float",
    "color":"ajisai",   
}

header={
    "X-USER-TOKEN":TOKEN
}
######_____CREATING GRAPH FOR TRACKING ____#####

# graph_response=requests.post(url=GRAPH_ENDPOINT,json=graph_config,headers=header)
# print(graph_response.text)

PIXELA_CREATION_ENDPOINT=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
TODAY=datetime.now()


pixel_config={
    "date":TODAY.strftime("%Y%m%d"),
    "quantity":input("How many hours have you studied today ?: ")
}

response=requests.post(url=PIXELA_CREATION_ENDPOINT,json=pixel_config,headers=header)
print(response.text)

