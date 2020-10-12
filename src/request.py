import requests


class ResqreApi():
    def resource(self,url_address,key,value):
        content = requests.get(url_address) 
        todo = content.json()
        a=todo['data']
        for i in range(len(a)):
            if a[i][key]==value:
                return {'data':(a[i])},{'ad':todo['ad']}

           