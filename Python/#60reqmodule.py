#Requests module in python
import requests

r = requests.get('https://www.financialmodelingprep.com/api/company/price/AAPL')
print(r.text) #This will give me the content of the above url
print(r.status_code) #This will tell you the status code

#This is a post request:
# url = 'www.something.com'
# data = {
#     'p1':4,
#     'p2':8
# }
# r2 = requests.post(url=url, data=data)
