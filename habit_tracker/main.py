import requests
from datetime import datetime

USERNAME="kbhaskar"
TOKEN="bhaskar@011220"
ID="graph0"

user_parameter={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
pixela_endpoint="https://pixe.la/v1/users"

# response=requests.post(url=pixela_endpoint,json=user_parameter)
# print(response.text)

graph_config={
    "id":ID,
    "name":"Running Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"   
}
#Authentication
header={
    "X-USER-TOKEN":TOKEN
}

graph_endpoint=F"{pixela_endpoint}/{USERNAME}/graphs"


# graph_response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(graph_response.text)

today=datetime.now()
post_parameter={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How much you cycled today?"),
    
}
posting_endpoint=f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}"

posting_respose=requests.post(url=posting_endpoint,json=post_parameter,headers=header)
print(posting_respose.text)
# update_parameter={
#     "quantity":"8.0"
# }
# update_graph=f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"
# update_response=requests.put(url=update_graph,json=update_parameter,headers=header)
# print(update_response.text)

# delete_endpoint=f"https://pixe.la/v1/users/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"
# delete_response=requests.delete(url=delete_endpoint,headers=header)
# print(delete_response.text)