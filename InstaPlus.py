import base64
import json
import random
import threading
import uuid
from  curl_cffi import requests
import os
from Utils import encrypt_payload,decrypt_payload,Gen_UserAgent,Device_Data
from NamasteAes import NamasteAes


class InstaPlus:

    def __init__(self,UserName,UserID):

        self.Client=requests.Session()
        self.Client.timeout=100
        self.Client.impersonate=random.choice(['chrome99','chrome100','chrome101','chrome104','chrome107','chrome110'  ,'chrome99_android','edge99','edge101','safari15_3' ,'safari15_5'])


        self.usi=UserID
        self.unm=UserName

        self.os_api,self.android=Gen_UserAgent()

        self.brand,self.model=Device_Data()

        self.uud=str(uuid.uuid4())

        self.ufli=random.randint(111,999)
        self.uflw=str(random.randint(1111,9999))


        self.crcf = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(32))


    def appStatus(self):
        key='2WQT5YT5#4LFOJK02QQ@ffdE20%%KMKLDDLIREND$@@IRjllk5sdfEE'
        self.neo=str(os.urandom(2).hex())+'-'+str(os.urandom(2).hex())+'-'+str(os.urandom(1).hex())


        self.apsk=NamasteAes.enc_ecb(f'10:8B:B7:C6:6A:63:EF:D9:65:B3:70:F3:BF:8D:AA:55:43:97:C5:97,{self.usi}',"ksd%lsld@@ls86ms@lmsf4f8",16)




        Payload=' {"cpn":"ir.neolook.followerpluss","dvv":"neo_'+self.neo+'","usi":"'+self.usi+'","apsk":"'+self.apsk+'","lang":"en","ven":"1092","mrt":"Cafebazaar"}'



        url = 'http://neolok.ir/v1/appStatus/check/1092/ir.neolook.followerpluss'


        headers =  {
    # 'accept-encoding': 'gzip',
    'connection': 'Close',
    'content-transfer-encoding': 'binary',
    'content-type': 'binary/octet-stream',
    'host': 'neolok.ir',
    "user-agent": f"Dalvik/2.1.0 (Linux; U; Android {self.android}; {self.model} Build/PI)537.36",
    'x-neolook-auth':  base64.b64encode(f'neo_{self.neo}:'.encode('utf-8'))
}



        response = self.Client.post(url, headers=headers, data=encrypt_payload(Payload,key))

        print('1',decrypt_payload(response.content,key))

    def SignUp(self):

        key='mo1yDn01E3yVWM8lIKdMfpo92FN79uwq99p5Mm1I3CCcvx0FSKXu84YPJGlMwkKr'


        Payload='{"cpn":"ir.neolook.followerpluss","unm":"'+self.unm+'","dvv":"neo_'+self.neo+'","cde":"'+self.os_api+'","ufli":"'+str(self.ufli)+'","usi":"'+self.usi+'","uflw":"'+self.uflw+'","apsk":"'+self.apsk+'","id":"0","lang":"en","pn":"'+self.brand+' '+self.model+'","mrt":"Cafebazaar"}'


        headers ={
            # 'accept-encoding': 'gzip',
            'connection': 'Close',
            'content-transfer-encoding': 'binary',
            'content-type': 'binary/octet-stream',
            'host': 'app.neolook.ir',
            "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android {self.android}; {self.model} Build/PI)537.36",
            'x-neolook-auth': base64.b64encode(f'neo_{self.neo}:'.encode('utf-8'))
        }



        response = self.Client.post('https://app.neolook.ir/insfl.10/user/singUp/1092/ir.neolook.followerpluss',
                                 headers=headers, data=encrypt_payload(Payload, key))



        print('2',decrypt_payload(response.content, key))
        self.token=json.loads(decrypt_payload(response.content, key))['utn']

    def GetFollowList(self):
        while True:
            try:
                key='mo1yDn01E3yVWM8lIKdMfpo92FN79uwq99p5Mm1I3CCcvx0FSKXu84YPJGlMwkKr'


                Payload='{"cpn":"ir.neolook.followerpluss","uud":"'+self.uud+'","cnt":"0","usi":"'+self.usi+'","cfrc":"'+self.crcf+'","apsk":"'+self.apsk+'","lang":"en","mrt":"Cafebazaar"}'

                headers = {
                    # 'accept-encoding': 'gzip',
                    'connection': 'Close',
                    'content-transfer-encoding': 'binary',
                    'content-type': 'binary/octet-stream',
                    'host': 'app.neolook.ir',
                    "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android {self.android}; {self.model} Build/PI)537.36",
                    'x-neolook-auth': base64.b64encode(f'neo_{self.neo}:{self.token}'.encode('utf-8')), #neo_18ec-4e74-4b:c13wnecYgBapttQwNjFxQwaS2aGYYx
                }


                response = self.Client.post(
                    'https://app.neolook.ir/insfl.10/follower/getFollowList/1092/ir.neolook.followerpluss',
                    headers=headers,
                    data=encrypt_payload(Payload, key))
                data=decrypt_payload(response.content, key)
                if "unm" in json.dumps(data):
                    for items in json.loads(data)['dolt']:
                        self.OrderFollow(items)
                else:print(data)
            except Exception as E:
                print(E)

    def OrderFollow(self,items):
        try:
            key='mo1yDn01E3yVWM8lIKdMfpo92FN79uwq99p5Mm1I3CCcvx0FSKXu84YPJGlMwkKr'
            Payload='{"cpn":"ir.neolook.followerpluss","scnt":"'+str(self.ufli)+'","usi":"'+self.usi+'","is":"1","apsk":"'+self.apsk+'","id":"'+items['id']+'","extid":"'+items['usi']+'","lang":"en","pht":"'+items['pht']+'","mrt":"Cafebazaar"}'
            self.ufli+=1

            headers = {
                # 'accept-encoding': 'gzip',
                'connection': 'Close',
                'content-transfer-encoding': 'binary',
                'content-type': 'binary/octet-stream',
                'host': 'app.neolook.ir',
                "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android {self.android}; {self.model} Build/PI)537.36",
                'x-neolook-auth': base64.b64encode(f'neo_{self.neo}:{self.token}'.encode('utf-8')), #neo_18ec-4e74-4b:c13wnecYgBapttQwNjFxQwaS2aGYYx
            }


            response = self.Client.post(
                'https://app.neolook.ir/insfl.10/follower/setFollow/1092/ir.neolook.followerpluss',
                headers=headers,
                data=encrypt_payload(Payload, key))


            print(decrypt_payload(response.content, key))
            # self.coins=json.loads(decrypt_payload(response.content, key))['dour']['ucfl']
            # if int(self.coins)>=1200:
            #     self.CoinsTransfer()
            # else:pass

        except Exception as E:
            print(E)

    # def CoinsTransfer(self):
    #
    #     key = 'mo1yDn01E3yVWM8lIKdMfpo92FN79uwq99p5Mm1I3CCcvx0FSKXu84YPJGlMwkKr'
    #
    #     Payload='{"prc":"0","cpn":"ir.neolook.followerpluss","cnt":"'+str(self.coins)+'","usi":"'+self.usi+'","apsk":"'+self.apsk+'","id":"49078425082","lang":"en","mrt":"Cafebazaar"}'
    #
    #
    #     headers = {
    #             # 'accept-encoding': 'gzip',
    #             'connection': 'Close',
    #             'content-transfer-encoding': 'binary',
    #             'content-type': 'binary/octet-stream',
    #             'host': 'app.neolook.ir',
    #             "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android {self.android}; {self.model} Build/PI)537.36",
    #             'x-neolook-auth': base64.b64encode(f'neo_{self.neo}:{self.token}'.encode('utf-8')), #neo_18ec-4e74-4b:c13wnecYgBapttQwNjFxQwaS2aGYYx
    #         }
    #
    #
    #     response = self.Client.post(
    #         'https://app.neolook.ir/insfl.10/follower/transferCoins/1092/ir.neolook.followerpluss',
    #         headers=headers,
    #         data=encrypt_payload(Payload, key),
    #     )
    #
    #     print(decrypt_payload(response.content, key))


# if __name__ == '__main__':
#     def run():
#         # print(len('vlAhbWFM9rkpSznOCBMfVxadtNaLkLbh'))
#         cl=InstaPlus()
#         cl.appStatus()
#         cl.SignUp()
#         cl.GetFollowList()
#
#
#     for i in range(1):
#         ml=threading.Thread(target=run)
#         ml.start()

