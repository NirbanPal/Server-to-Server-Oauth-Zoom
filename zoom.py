import requests
import json

# replace with your client ID
client_id = ""

# replace with your account ID
account_id = ""

# replace with your client secret
client_secret = ""

auth_token_url = "https://zoom.us/oauth/token"
api_base_url = "https://api.zoom.us/v2"



class Zoommeeting:
    def __init__(self,client_id,account_id,client_secret):
        self.client_id=client_id
        self.account_id=account_id
        self.client_secret=client_secret

        data = {
            "grant_type": "account_credentials",
            "account_id": self.account_id,
            "client_secret": self.client_secret
        }

        resp=requests.post(auth_token_url,auth=(self.client_id, self.client_secret),data=data)
        self.response=resp.json()['access_token']



    
    def CreateMeeting(self,topic, duration, start_date, start_time,password):

        access_token = self.response

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "topic": topic,
            "duration": duration,
            'start_time': f'{start_date}T10:{start_time}',
            "type": 2,
            "password":password,
            'settings':{
                'join_before_host': True,
                # 'timezone': 'Asia/Calcutta' 
            }
        }

        resp = requests.post(f"{api_base_url}/users/me/meetings",headers=headers,json=payload)

        if resp.status_code != 201:
            print("Unable to generate meeting link")

        print(json.loads(resp.text))
        return json.loads(resp.text)
    
    def DeleteMeeting(self,meeting_id):
        access_token=self.response
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.delete(f"{api_base_url}/meetings/{meeting_id}", headers=headers)
        if response.status_code == 204:
            print("deleted")
            return response
        else:
            raise Exception("Failed to delete meeting")
        

    def GetMeetingInfo(self, meeting_id):
        # Retrieve details of a Zoom meeting by its ID
        access_token=self.response
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(f"{api_base_url}/meetings/{meeting_id}", headers=headers)
        if response.status_code == 200:
            # return response.json()
            print(json.loads(response.text))
            return json.loads(response.text)
        else:
            print(response.json())
            raise Exception("Failed to get meeting details")
        


        
    

        


zoommeeting=Zoommeeting(client_id,account_id,client_secret)
# zoommeeting.CreateMeeting("Test Zoom Meeting","60","2023-09-24","18:24","sitaraman")
# print("Meeting details")
# zoommeeting.GetMeetingInfo('73855538968')
# zoommeeting.DeleteMeeting('73855538968')

