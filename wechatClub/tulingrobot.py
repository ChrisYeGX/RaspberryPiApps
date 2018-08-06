# -*- coding: utf-8 -*-
import requests
import json

class TulingRobot(object):
    def __init__(self):
        self.api = "http://openapi.tuling123.com/openapi/api/v2"
        self.apiKey = "你的图灵机器人api的apiKey"

    def request_api(self, send_json):
        data = json.dumps(send_json).encode('utf8')
        response = requests.post(url=self.api, data=data, headers={'content-type': 'application/json'})
        result = ''
        for tmp in response.json()["results"]:
            # print(tmp)
            # print(tmp["values"].keys())
            for key in tmp["values"].keys():
                result += tmp["values"][key]
        return result

    def talk2string(self, text, userid="hyhm2n"):
        send_json = {
            "reqType":0,
            "perception": {
                "inputText": {
                    "text": text
                }
            },
            "userInfo": {
                "apiKey": self.apiKey,
                "userId": "hyhm2n"
            }
        }
        return self.request_api(send_json)
    
    def talk2image(self, image_url, userid="hyhm2n"):
        send_json = {
            "reqType":0,
            "perception": {
                "inputImage": {
                    "url": image_url
                },
            },
            "userInfo": {
                "apiKey": self.apiKey,
                "userId": userid
            }
        }
        return self.request_api(send_json)

    def talk2media(self, media_url, userid="hyhm2n"):
        send_json = {
            "reqType":0,
            "perception": {
                "inputMedia": {
                    "url": media_url
                },
            },
            "userInfo": {
                "apiKey": self.apiKey,
                "userId": userid
            }
        }
        return self.request_api(send_json)


if __name__ == "__main__":
    print(TulingRobot().talk2string("查询无锡天气"))