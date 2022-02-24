
import pandas as pd
import requests
import json
from datetime import datetime, timedelta

url = "https://web.heynow.com.uy:8310/api/login"

payload = json.dumps({
  "name": "ReportesDigitex",
  "password": "Desarrollo1"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

y = json.loads(response.text)


dayCurrently = datetime.today().strftime('%Y-%m-%d')
dayBefore = (datetime.today() - timedelta(22)).strftime('%Y-%m-%d')
dayCurrently2 = datetime.today().strftime('%Y%m%d')


url2 = "https://web.heynow.com.uy:8310/api/report/session?begin="+dayCurrently+" 00:00:00&end="+dayCurrently+" 23:59:00&pageSize=500&exclude=chat"
        
j = "Bearer "+ y['token']

payload={}
headers = {
  
  'Authorization': j
  
}

response2 = requests.request("GET", url2, headers=headers, data=payload)
response2.encoding = 'ascii'
data = json.loads(response2.text)

scroll_id = data['scroll']['id']
scroll_length = data['scroll']['length']

##Scroll
totalData = data['data']

while (int(scroll_length) > 0):

 url3 = "https://web.heynow.com.uy:8310/api/report/" + scroll_id

 payload={}
 headers = {
  'Authorization': j
  
   }

 response3 = requests.request("GET", url3, headers=headers, data=payload)
 response3.encoding = 'ascii'
 dataScroll = json.loads(response3.text)
 scroll_id = dataScroll['scroll']['id']
 scroll_length = dataScroll['scroll']['length'] 
 if (int(scroll_length > 0)):
  totalData = totalData + dataScroll['data']

#with open(data, encoding="ascii", errors='ignore') as file:
#data = json.load(file)
  #data = pd.read_json(file, encoding='UTF-8')


data_id = []
date = []
delay = []
index = []
public = []
steps = []
key = []

for elemento in totalData:
  
  for step in elemento['_source']['steps']:
    
    data_id.append(elemento['_id'])

    if 'date' in step:
      date.append(step['date'])
    else:
      date.append('')

    key.append(elemento['_id'] + step['date'])
    
    if 'delay' in step:
      delay.append(step['delay'])
    else:
      date.append('')

    if 'index' in step:
      index.append(step['index'])
    else:
      index.append('')

    if 'public' in step:
      public.append(step['public'])
    else:
      public.append('')

    if 'step' in step:
      steps.append(step['step'])
    else:
      steps.append('')


archivo = {

'data_id' : data_id,
'date' : date,
'delay' : delay,
'index' : index,
'public' : public,
'step' : steps,
'key' : key

}
data_frame = pd.DataFrame(data=archivo)
#data_frame.to_csv('C:\\Users\\User1\\Desktop\\API_AIVO\\datos3.csv')
data_frame.to_csv('C:\\API_HEY_NOW\\Descargas_Online\\datosArchivo3.csv',encoding="ascii", errors='ignore',sep = ';')


#print(data_frame)

#data['data'][0]['_source']['contact']['channels'][0]['clientId']

#pd.json_normalize(json.loads(response.text)).to_csv("file_name.csv")
