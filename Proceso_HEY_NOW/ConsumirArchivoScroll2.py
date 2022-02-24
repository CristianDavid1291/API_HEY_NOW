
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

url2 = "https://web.heynow.com.uy:8310/api/report/session?begin="+dayCurrently+" 00:00:00&end="+dayCurrently+" 23:59:00&pageSize=500"

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


data_id = []
hey = []
chat_id  = []
ability = []
billing = []
idAgent = []
idMessageHey = []
contactId = []
date = []
endSession = []
incoming = []
lastUpdate = []
message = []
metaData_channelStatus_deliveredStatus = []
metaData_channelStatus_deliveredStatusCode = []
metaData_channelStatus_sentStatus = []
metaData_channelStatus_sentStatusCode = []
metaData_status = []
sequence = []

#cycle to search by each element in data  
for elemento in totalData:
  
  #cycle to search by each element in chat in data  
 for chat in elemento['_source']['chat']:
    data_id.append(elemento['_id'])

    if 'trigger' in chat['__Hey__']:
      hey.append(chat['__Hey__']['trigger'])
    else:
      hey.append('')
    
    if '_id' in chat: 
      chat_id.append(chat['_id'])
    else:
      chat_id.append('')

    if 'ability' in chat:
      ability.append(chat['ability'])
    else:
      ability.append('')
    
    if 'billing' in chat:
      billing.append(chat['billing'])
    else:
       billing.append('')

    if 'idAgent' in chat:
      idAgent.append(chat['idAgent'])
    else:
       idAgent.append('')
    
    if 'idMessageHey' in chat:
      idMessageHey.append(chat['idMessageHey'])
    else:
       idMessageHey.append('')
    
    if 'contactId' in chat:
      contactId.append(chat['contactId'])
    else:
       contactId.append('')
    
    if 'date' in chat:
      date.append(chat['date'])
    else:
       date.append('')
    
    if 'endSession' in chat:
      endSession.append(chat['endSession'])
    else:
       endSession.append('')

    if 'incoming' in chat:
      incoming.append(chat['incoming'])
    else:
       incoming.append('')

    if 'lastUpdate' in chat:
      lastUpdate.append(chat['lastUpdate'])
    else:
       lastUpdate.append('')
   
    if 'message' in chat:
      message.append(chat['message'])
    else:
       message.append('')
    
    if 'metaData' in chat:
      if 'channelStatus' in chat['metaData']:
        if 'deliveredStatus' in chat['metaData']['channelStatus']:
          metaData_channelStatus_deliveredStatus.append(chat['metaData']['channelStatus']['deliveredStatus'])
        else:
          metaData_channelStatus_deliveredStatus.append('')
      else:
        metaData_channelStatus_deliveredStatus.append('')    
    else:
     metaData_channelStatus_deliveredStatus.append('')

    if 'metaData' in chat:
      if 'channelStatus' in chat['metaData']:
        if 'deliveredStatusCode' in chat['metaData']['channelStatus']:
          metaData_channelStatus_deliveredStatusCode.append(chat['metaData']['channelStatus']['deliveredStatusCode'])
        else:
          metaData_channelStatus_deliveredStatusCode.append('')
      else:
        metaData_channelStatus_deliveredStatusCode.append('')    
    else:
      metaData_channelStatus_deliveredStatusCode.append('')
    

    if 'metaData' in chat:
      if 'channelStatus' in chat['metaData']:
        if 'sentStatus' in chat['metaData']['channelStatus']:
          metaData_channelStatus_sentStatus.append(chat['metaData']['channelStatus']['sentStatus'])
        else:
          metaData_channelStatus_sentStatus.append('')
      else:
        metaData_channelStatus_sentStatus.append('')    
    else:
     metaData_channelStatus_sentStatus.append('')

    if 'metaData' in chat:
      if 'channelStatus' in chat['metaData']:
        if 'sentStatusCode' in chat['metaData']['channelStatus']:
          metaData_channelStatus_sentStatusCode.append(chat['metaData']['channelStatus']['sentStatusCode'])
        else:
           metaData_channelStatus_sentStatusCode.append('')
      else:
         metaData_channelStatus_sentStatusCode.append('')     
    else:
     metaData_channelStatus_sentStatusCode.append('')


    if 'metaData' in chat:
      if 'status' in chat['metaData']:
          metaData_status.append(chat['metaData']['status'])
      else:
         metaData_status.append('')
    else:
        metaData_status.append('')
  

    if 'sequence' in chat:
      sequence.append(chat['sequence'])
    else:
       sequence.append('')

archivo = {

'data_id' : data_id,
'hey' : hey,
'chat_id'  : chat_id,
'ability' : ability,
'billing' : billing,
'idAgent' : idAgent,
'idMessageHey' : idMessageHey,
'contactId' : contactId,
'date' : date,
'endSession' : endSession,
'incoming' : incoming,
'lastUpdate' : lastUpdate,
'message' : message,
'metaData_channelStatus_deliveredStatus' : metaData_channelStatus_deliveredStatus,
'metaData_channelStatus_deliveredStatusCode' : metaData_channelStatus_deliveredStatusCode,
'metaData_channelStatus_sentStatus' : metaData_channelStatus_sentStatus,
'metaData_channelStatus_sentStatusCode' : metaData_channelStatus_sentStatusCode,
'metaData_status' : metaData_status,
'sequence' : sequence

}

# print(len(data_id))
# print(len(hey))
# print(len(chat_id))
# print(len(ability))
# print(len(billing))
# print(len(idAgent))
# print(len(idMessageHey))
# print(len(contactId))
# print(len(date))
# print(len(endSession))
# print(len(incoming))
# print(len(lastUpdate))
# print(len(message))
# print(len(metaData_channelStatus_deliveredStatus))
# print(len(metaData_channelStatus_deliveredStatusCode))
# print(len(metaData_channelStatus_sentStatus))
# print(len(metaData_channelStatus_sentStatusCode))
# print(len(metaData_status))
# print(len(sequence))


data_frame = pd.DataFrame(data=archivo)
data_frame.to_csv('C:\\API_HEY_NOW\\Descargas_Online\\datosArchivo2.csv',encoding="ascii", errors='ignore',sep = ';')


#data['data'][0]['_source']['chat'][0]['__Hey__']['trigger']
#data['data'][0]['_source']['contact']['channels'][0]['clientId']

#pd.json_normalize(json.loads(response.text)).to_csv("file_name.csv")



