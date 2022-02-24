
import pandas as pd
import requests
import json
from datetime import datetime

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
dayCurrently2 = datetime.today().strftime('%Y%m%d')

url2 = "https://web.heynow.com.uy:8310/api/report/session?begin="+dayCurrently+" 00:00:00&end="+dayCurrently+" 23:59:00&pageSize=500&exclude=chat&include=abandoned&include=beginSession&include=channel&include=channelContext&include=companyId&include=contact&include=elasticQueryData&include=endSession&include=firstIncomingMessage&include=messages&include=platformId&include=queryChannelContext&include=queryData&include=session&include=sessionLength&include=startPannelDate&include=versions&include=contactLastInteractionDate"
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
scroll_total_value = data['scroll']['total']['value']
scroll_total_relation = data['scroll']['total']['relation']

data_index =[] 
data_type = []
data_id = []
data_score = []
data_source_abandoned = []
data_source_beginSession = []
data_source_channel = []
data_source_channelContext = []
data_source_clientId = []
data_source_companyId = []
data_source_contact_id = []
data_source_contact_creationDate = []
data_source_contact_first_name = []
data_source_contact_gender = []
data_source_contact_lastUpdate = []
data_source_contact_last_name = []
data_source_contact_locale = []
data_source_contact_profile_pic = []
data_source_contact_timezone = []
data_source_contactLastInteractionDate = []
data_source_elasticQueryChannelContext = []
data_source_endSession = []
data_source_firstIncomingMessage = []
data_source_messages_incomingMessages = []
data_source_messages_outcomingMessages = []
data_source_messages_totalMessages = []
data_source_platformId = []
data_source_queryChannelContext = []
data_source_queryData_encuestaSolicitada_type = []
data_source_queryData_encuestaSolicitada_value = []
data_source_session = []
data_source_sessionLength = []
data_source_startPannelDate = []
data_source_versions_chat = []
data_source_versions_contact = []
data_source_versions_messages = []
data_source_versions_steps = []

for elemento in data['data']:
  
  data_index.append(elemento['_index'])
  data_type.append(elemento['_type'])
  data_id.append(elemento['_id'])
  data_score.append(elemento['_score'])

# verificar llave abandoned
  if 'abandoned' in elemento['_source']:
    data_source_abandoned.append(elemento['_source']['abandoned'])
  else:
    data_source_abandoned.append("")
 # verificar llave endSession 
  if 'endSession' in elemento['_source']:
    data_source_beginSession.append(elemento['_source']['endSession'])
  else:
    data_source_beginSession.append("")

 # verificar llave channel 
  if 'channel' in elemento['_source']:
    data_source_channel.append(elemento['_source']['channel'])
  else:
    data_source_channel.append("")
  
  # verificar llave channel context
  if 'channelContext' in elemento['_source']:
    data_source_channelContext.append(elemento['_source']['channelContext'])
  else:
    data_source_channelContext.append("")

# verificar llave cient_id

  if 'clientId' in elemento['_source']['contact']['channels'][0]:
    data_source_clientId.append(elemento['_source']['contact']['channels'][0]['clientId'])
  else:
    data_source_clientId.append("")

# verificar llave cient_id
    
  if 'companyId' in elemento['_source']:
    data_source_companyId.append(elemento['_source']['companyId'])
  else:
    data_source_companyId.append("")
  
  # verificar llave contact_id
  if '_id' in elemento['_source']['contact']:
    data_source_contact_id.append(elemento['_source']['contact']['_id'])
  else:
    data_source_contact_id.append("")

# verificar llave creation_date
  if 'creationDate' in elemento['_source']['contact']:
    data_source_contact_creationDate.append(elemento['_source']['contact']['creationDate'])
  else:
    data_source_contact_creationDate.append("")

  
    # verificar llave contact_first_name
  if 'first_name' in elemento['_source']['contact']:
    data_source_contact_first_name.append(elemento['_source']['contact']['first_name'])
  else:
    data_source_contact_first_name.append("")

    # verificar llave contact_first_name
  if 'gender' in elemento['_source']['contact']:
    data_source_contact_gender.append(elemento['_source']['contact']['gender'])
  else:
    data_source_contact_gender.append("")
  
      # verificar llave contact_last_uptdate
  if 'lastUpdate' in elemento['_source']['contact']:
    data_source_contact_lastUpdate.append( elemento['_source']['contact']['lastUpdate'][0]['date'])
  else:
    data_source_contact_lastUpdate.append("")
  
      # verificar llave contact_last_name
  if 'last_name' in elemento['_source']['contact']:
    data_source_contact_last_name.append(elemento['_source']['contact']['last_name'])
  else:
    data_source_contact_last_name.append("")

      # verificar llave contact_locale
  if 'locale' in elemento['_source']['contact']:
    data_source_contact_locale.append(elemento['_source']['contact']['locale'])
  else:
    data_source_contact_locale.append("")
  
  # verificar llave contact_locale
  if 'profile_pic' in elemento['_source']['contact']:
    data_source_contact_profile_pic.append(elemento['_source']['contact']['profile_pic'])
  else:
    data_source_contact_profile_pic.append("")

    # verificar llave time_zone
  if 'timezone' in elemento['_source']['contact']:
    data_source_contact_timezone.append(elemento['_source']['contact']['timezone'])
  else:
    data_source_contact_timezone.append("")

        # verificar llave contactLastInteractionDate
  if 'contactLastInteractionDate' in elemento['_source']:
    data_source_contactLastInteractionDate.append(elemento['_source']['contactLastInteractionDate'])
  else:
    data_source_contactLastInteractionDate.append("")

            # verificar llave contactLastInteractionDate
  if 'queryChannelContext' in elemento['_source']:
    data_source_elasticQueryChannelContext.append(elemento['_source']['queryChannelContext'])
  else:
    data_source_elasticQueryChannelContext.append("")

  # verificar llave contactLastInteractionDate
  if 'endSession' in elemento['_source']:
    data_source_endSession.append(elemento['_source']['endSession'])
  else:
    data_source_endSession.append("")

  # verificar llave firstIncomingMessage
  if 'firstIncomingMessage' in elemento['_source']:
    data_source_firstIncomingMessage.append(elemento['_source']['firstIncomingMessage'])
  else:
    data_source_firstIncomingMessage.append("")

   # verificar llave IncomingMessage
  if 'incomingMessages' in elemento['_source']['messages']:
    data_source_messages_incomingMessages.append( elemento['_source']['messages']['incomingMessages'])
  else:
    data_source_messages_incomingMessages.append("")

   # verificar llave outcomingMessages
  if 'outcomingMessages' in elemento['_source']['messages']:
    data_source_messages_outcomingMessages.append( elemento['_source']['messages']['outcomingMessages'])
  else:
    data_source_messages_outcomingMessages.append("")
  
  # verificar llave totalMessages
  if 'totalMessages' in elemento['_source']['messages']:
    data_source_messages_totalMessages.append( elemento['_source']['messages']['totalMessages'])
  else:
    data_source_messages_totalMessages.append("")

     # verificar llave platformId
  if 'platformId' in elemento['_source']:
    data_source_platformId.append( elemento['_source']['platformId'])
  else:
    data_source_platformId.append("") 

     # verificar llave session
  if 'session' in elemento['_source']:
    data_source_session.append( elemento['_source']['session'])
  else:
    data_source_session.append("") 

     # verificar llave sessionLength
  if 'sessionLength' in elemento['_source']:
    data_source_sessionLength.append( elemento['_source']['sessionLength'])
  else:
    data_source_sessionLength.append("") 

     # verificar llave startPannelDate
  if 'startPannelDate' in elemento['_source']:
    data_source_startPannelDate.append( elemento['_source']['startPannelDate'])
  else:
    data_source_startPannelDate.append("") 

     # verificar llave versions_chat
  if 'chat' in elemento['_source']['versions']:
    data_source_versions_chat.append( elemento['_source']['versions']['chat'])
  else:
    data_source_versions_chat.append("") 

     # verificar llave versions_contact
  if 'contact' in elemento['_source']['versions']:
    data_source_versions_contact.append( elemento['_source']['versions']['contact'])
  else:
    data_source_versions_contact.append("") 

     # verificar llave versions_messages
  if 'messages' in elemento['_source']['versions']:
    data_source_versions_messages.append( elemento['_source']['versions']['messages'])
  else:
    data_source_versions_messages.append("") 

     # verificar llave versions_steps
  if 'steps' in elemento['_source']['versions']:
    data_source_versions_steps.append( elemento['_source']['versions']['steps'])
  else:
    data_source_versions_steps.append("") 



archivo = {
'data_index' : data_index,
'data_type' : data_type,
'data_id' : data_id,
'data_score' : data_score,
'data_source_abandoned' : data_source_abandoned,
'data_source_beginSession' : data_source_beginSession,
'data_source_channel' : data_source_channel,
'data_source_channelContext' : data_source_channelContext,
'data_source_clientId' : data_source_clientId,
'data_source_companyId' : data_source_companyId,
'data_source_contact_id' : data_source_contact_id,
'data_source_contact_creationDate' : data_source_contact_creationDate,
'data_source_contact_first_name' : data_source_contact_first_name,
'data_source_contact_gender' : data_source_contact_gender,
'data_source_contact_lastUpdate' : data_source_contact_lastUpdate,
'data_source_contact_last_name' : data_source_contact_last_name,
'data_source_contact_locale' : data_source_contact_locale,
'data_source_contact_profile_pic' : data_source_contact_profile_pic,
'data_source_contact_timezone' : data_source_contact_timezone,
'data_source_contactLastInteractionDate' : data_source_contactLastInteractionDate,
#'data_source_elasticQueryChannelContext' : data_source_elasticQueryChannelContext,
'data_source_endSession' : data_source_endSession,
'data_source_firstIncomingMessage' : data_source_firstIncomingMessage,
'data_source_messages_incomingMessages' : data_source_messages_incomingMessages,
'data_source_messages_outcomingMessages' : data_source_messages_outcomingMessages,
'data_source_messages_totalMessages' : data_source_messages_totalMessages,
'data_source_platformId' : data_source_platformId,
#'data_source_queryChannelContext' : data_source_queryChannelContext,
#'data_source_queryData_encuestaSolicitada_type' : data_source_queryData_encuestaSolicitada_type,
#'data_source_queryData_encuestaSolicitada_value' : data_source_queryData_encuestaSolicitada_value,
'data_source_session' : data_source_session,
'data_source_sessionLength' : data_source_sessionLength,
'data_source_startPannelDate' : data_source_startPannelDate,
'data_source_versions_chat' : data_source_versions_chat,
'data_source_versions_contact' : data_source_versions_contact,
'data_source_versions_messages' : data_source_versions_messages,
'data_source_versions_steps' : data_source_versions_steps,
}

data_frame = pd.DataFrame(data=archivo)
data_frame.to_csv('C:\\API_HEY_NOW\\Descargas_Online\\datosArchivo1'.csv',encoding = 'ascii', errors = 'ignore')



