# -*- coding: utf-8 -*-
import re
from my_aip import StringToMp3
from tulingrobot import TulingRobot
from photoGraph import get_photo, upimag
import werobot

robot = werobot.WeRoBot(token='你的token')
robot.config["APP_ID"] = "你的微信公众号APP_ID"
robot.config["APP_SECRET"] = "你的微信公众号APP_SECRET"
robot.config['ENCODING_AES_KEY'] =  "你的微信公众号ENCODING_AES_KEY"

# 这是我的菜单外链
menu_image_url = "http://image.3001.net/images/20180805/15334664151975.png"

# 发送给 新关注用户 的消息
@robot.subscribe
def subscribe(message):
    content = '欢迎来到人工智障总部!\n'+ menu_image_url
    return content

# 文字信息处理
@robot.text
def handler(message): 
    if re.findall(r"暗影菜单", str(message.content)):
        return menu_image_url
    elif re.findall(r"暗影偷拍", message.content):
        return upimag(get_photo())
    elif re.findall(r".*?查询(.*)?天气.*?", message.content):
        weather_info = TulingRobot().talk2string(message.content)
        StringToMp3(weather_info, "./weather_info.mp3").playMp3()
        return weather_info
    else:
        return TulingRobot().talk2string(message.content)

# 图片处理信息处理
@robot.image
def img(message):
    return TulingRobot().talk2image(message.img)

# 错误页面处理
@robot.error_page
def make_error_page(url):
    return "<h1>喵喵喵 %s 不是给麻瓜访问的快走开</h1>" % url

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()