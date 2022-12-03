import requests
import json

headers = {
    'Authorization' : 'Bearer TOKEN' ,
    'Content-Type' : 'application/json',

}

params ={
    'collector' : 'c_lb6fda0o2n1mfjktr6',
    'queue_next' : 1 ,
} 


json_data= [
    {
        'url' : 'https://www.amazon.com/s?k=mounting+and+fastening&rh=n%3A228013&dc&crid=9W9ZLKPYDBEM&qid=1643643231&rnid=2941120011&sprefix=mounting+and+fastening%2Caps%2C155&ref=sr_nr_n_1',
        'country' : 'US' ,
        'domain' : 'https://www.amazon.com',
        'department' : '',
        'max_pages' : '2' ,
    }

]

response = requests.post('https://api.brightdata.com/dca/trigger',params=params, headers=headers, json=json_data)
data = json.loads(response.content.decode("utf-8"))
print(data)