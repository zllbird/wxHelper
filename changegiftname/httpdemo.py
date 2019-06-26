import requests
import json

class http(object):

    @staticmethod
    def postTuling(msg=None):
        if msg is not None:
            data = {
                "reqType": 0,
                "perception": {
                    "inputText": {
                        "text": msg.text
                    },
                    "inputImage": {
                        "url": "imageUrl"
                    },
                    "selfInfo": {
                        "location": {
                            "city": "北京",
                            "province": "北京",
                            "street": "信息路"
                        }
                    }
                },
                "userInfo": {
                    "apiKey": "fab3ef8bfc4a4289a2c5b51ea5e3d1b9",
                    "userId": "zhu"
                }
            }

            r = requests.post('http://openapi.tuling123.com/openapi/api/v2', json=data)
            if r.status_code == 200:
                data = json.loads(r.text)
                print(data)
                results = data['results']
                text = results[0]['values']['text']
                return text
            else:
                return '出现错误！'

