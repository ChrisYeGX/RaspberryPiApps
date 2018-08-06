# -*- coding: utf-8 -*-
import os
import time
import requests

def get_photo():
    # photoGraph_shell = "raspistill -o tmp_image.jpg -rot 0 -w 1024 -h 768 –t 2"
    photoGraph_shell = "raspistill -t 1000 -o tmp_image.jpg &"
    os.system(photoGraph_shell)
    time.sleep(1.4)
    return "tmp_image.jpg"

# 图片上传, 获取外链
def upimag(filepath):
    try:
        with open(filepath, 'rb') as file:
            url = 'https://group.jd.com/ueditor/jsp/imageUp.jsp?action=uploadimage&encode=utf-8'
            headers = {
                'Host': 'group.jd.com',
                'Origin': 'https://group.jd.com',
                'Referer': 'https://group.jd.com/ueditor/dialogs/imag',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',   
            }
            response = requests.post(url, headers=headers,files={'upfile':file})
            return 'http://img30.360buyimg.com/club_community/'+response.json()['url']
    except Exception as e:
        return "获取图片失败.错误信息:{0}".format(e)

if __name__ == "__main__":
    print(upimag(get_photo()))