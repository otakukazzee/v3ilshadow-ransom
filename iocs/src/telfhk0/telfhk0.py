"""
Module TelFHk v 2.1.1 ! Modern Bot For hackers or Programer :)
update 3
Import Modules
"""
from os import system as screen
try:
	from requests import post as REQ
	from requests import get as REQ2
except:
    screen("pip install requests")
"Started Set Api Telegram for Methods"
class Telegram:
    def __init__(self, chat, token):
        self.chat = chat
        self.token = token
     
    def SendMessage(self,text,mode=None):
        data = {
            "UrlBox": f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat}&text={text}&parse_mode={mode}",
            "AgentBox": "Google Chrome",
            "VersionsList": "HTTP/1.1",
            "MethodList": "GET"
        }
        REQ("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=data)

    def MultiMessage(self, chats_id,text,mode=None):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        for i in chats_id:
            response = REQ(url, json={"chat_id": i, "text": text,'parse_mode':mode})
        
    def DownloadIR(self,link,mode=None):
        data = {
            "UrlBox": f"https://api.telegram.org/bot{self.token}/sendDocument?chat_id={self.chat}&document={link}&parse_mode={mode}",
            "AgentBox": "Google Chrome",
            "VersionsList": "HTTP/1.1",
            "MethodList": "GET"
        }
        REQ("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx", data=data)         

          
    def SendPhoto(self,address,caption=None,mode=None):
        url = f"https://api.telegram.org/bot{self.token}/sendPhoto?chat_id={self.chat}&caption={caption}"
        files = {'photo': open(address, 'rb')}     
        data = {'parse_mode':mode}      
        r = REQ(url,files=files,data=data)

    def SendFile(self,address,caption=None,mode=None):
        url = f"https://api.telegram.org/bot{self.token}/sendDocument?chat_id={self.chat}&caption={caption}"
        files = {'document': open(address, 'rb')}           
        r = REQ(url,files=files,data={'parse_mode':mode})
    def SendVideo(self,address,caption=None,mode=None):
        url = f"https://api.telegram.org/bot{self.token}/sendVideo?chat_id={self.chat}&caption={caption}"
        files = {'video': open(address, 'rb')}           
        r = REQ(url,files=files,data={'parse_mode':mode}) 

    def SendSticker(self,sticker,mode=None):
        url = f"https://api.telegram.org/bot{self.token}/sendSticker?chat_id={self.chat}"
        files = {'sticker': open(sticker, 'rb')}           
        r = REQ(url,files=files,data={'parse_mode':mode})

    def EditMessage(self,id,text,mode=None):
        url = f"https://api.telegram.org/bot{self.token}/editMessageText?chat_id={self.chat}"
        data = {'message_id': id,'text':text,'parse_mode':mode}           
        r = REQ(url,data=data)

    def InfoBot(self):
        url = f'https://api.telegram.org/bot{self.token}/getMe'
        r = REQ2(url).text
        data = r.json()
        if r.status_code == 200:
            print(f"ID: {data['result']['id']}\nNAME : {data['result']['first_name']}")
                
    def Forward(self,target,id,mode=None):
        url = f"https://api.telegram.org/bot{self.token}/forwardMessage?chat_id={self.chat}&from_chat_id={target}&message_id={id}&parse_mode={mode}"
        data = {
            "UrlBox": url,
            "AgentBox": "Google Chrome",
            "VersionsList": "HTTP/1.1",
            "MethodList": "GET"
        }
        r = REQ("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=data)
        
    def GetProfile(self,user,limit,name):
        url = f"https://api.telegram.org/bot{self.token}/getUserProfilePhotos"
        params = {
        'user_id': user,
        'limit': limit
    }
        r = REQ(url,params=params)
        if r.status_code == 200:
            data = r.json()
            if data['result']['total_count'] > 0:
                file_id = data['result']['photos'][0][0]['file_id']        
                get_file_url = f"https://api.telegram.org/bot{self.token}/getFile"
                params = {'file_id': file_id}
                response = REQ2(get_file_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    file_path = data['result']['file_path']
                    file_url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"
                    response = REQ2(file_url)
                    if response.status_code == 200:
                        ur = f"https://api.telegram.org/bot{self.token}/sendPhoto?chat_id={self.chat}"
                        with open(name, 'wb') as file:
                            file.write(response.content)
                            files = {'photo': open(name, 'rb')}
                            r = REQ(ur,files=files)
                
    def DeletWebhok(self):
        url = f"https://api.telegram.org/{self.token}/deleteWebhook"       
        r = REQ(url)
            
    def SetWebhok(self,url):
        url = f"https://api.telegram.org/bot{self.token}/setWebhook?url={url}"       
        r = REQ(url)
        
    def get_last_message(self,number):
        url = f'https://api.telegram.org/bot{self.token}/getUpdates' 

        response = REQ2(url)
        data = response.json()
  
        if 'result' in data and data['result']:
       
            last_message = data['result'][number]
            return last_message

        return None

    def Reply(self,text,mode=None):
        response = REQ2(f'https://api.telegram.org/bot{self.token}/getUpdates')
        data = response.json()
        if data['result']:
        	last_message = data['result'][-1]['message']['text']
        	REQ2(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat}&text={text}&reply_to_message_id={data["result"][-1]["message"]["message_id"]}',data={'parse_mode':mode})

    def GetMessage(self,offset=None,timeout=None):
        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        response = REQ2(url,params={'offset': offset, 'timeout': timeout})
        if response.status_code == 200:
            messages = response.json()['result']
            last_message = None
            for message in messages:
                if 'message' in message and 'chat' in message['message'] and message['message']['chat']['id'] == self.chat:
                    last_message = message['message']['text']
            if last_message:
                print(last_message)
            else:
                print('No messages found')
        else:
            print('Failed to fetch messages')
    def MessageID(self):        
        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        response = REQ2(url)
        data = response.json()
        latest_message_id = data["result"][-1]["message"]["message_id"]
        print(latest_message_id)
                                                     
    def SendVoice(self,address, caption=None,mode=None):
        url = f"https://api.telegram.org/bot{self.token}/sendVoice?chat_id={self.chat}"
        data = {"caption": caption,'parse_mode':mode}
        files = {"voice": open(address, "rb"),'caption':caption}
        response = REQ(url, data=data, files=files) 
        
    def get_last_message_id(self,number):
        url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        response = REQ2(url)
    
        if response.status_code == 200:
            data = response.json()
            if data["ok"] and data["result"]:
                last_message_id = data["result"][-number]["message"]["message_id"]
                return last_message_id

        return None                 
                                   
    def DeleteMessage(self):
        response = REQ2(f'https://api.telegram.org/bot{self.token}/getUpdates')
        last_message_id = response.json()['result'][-1]['message']['message_id']
        REQ2(f'https://api.telegram.org/bot{self.token}/deleteMessage?chat_id={self.chat}&message_id={last_message_id}')

    def CreatePoll(self,ques,opt,anon,all):

        url = f'https://api.telegram.org/bot{self.token}/sendPoll'
        data = {
            'chat_id': self.chat,
            'question': ques,
            'options': opt,
            'is_anonymous':anon,
            'allows_multiple_answers':all
        }
        response = REQ(url, data=data)

    def infoChGr(self,id):
        r = REQ2(f"https://api.telegram.org/bot{self.token}/getChat?chat_id={id}")
        try:
            r2 = REQ2(f"https://api.telegram.org/bot{self.token}/grtChatMembersCount?chat_id={id}")
            data2 = r2.json()['result']
        except:
            data2 = None
        data = r.json()
        data = data['result']
        try:
            print (f"ID : {data['id']}\nNAME : {data['title']}\nTYPE : {data['type']}PINNED : {data['pinned_message']['text']}\nMEMBER : {data2}")
        except:
            print (f"ID : {data['id']}\nNAME : {data['title']}\nTYPE : {data['type']}PINNED : None\nMEMBER : {data2}")

    def Permission(self,id):
        r = REQ2(f"https://api.telegram.org/bot{self.token}/getChat?chat_id={id}")
        data = r.json()
        data = data['result']['permissions']
        for i in data:
            print (f'{i} : {data[i]}')

