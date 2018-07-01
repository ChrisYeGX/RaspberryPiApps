# raspberry
---
## 简单的语音天气闹钟⏰:
[SimpleClock](./SimpleClock):
- 简单描述
> 利用天气API与百度语音API生成MP3文件 os.system执行,使用contrab调用执行播放mp3文件就好了
- 项目细节
我还在树莓派实验室上投稿了此[项目](http://shumeipai.nxez.com/2017/10/27/crontab-and-raspberry-pi-voice-alarm-clock.html),具体的过程去看看吧。(因为写的比较久远了，有很多的问题，最近想更新一下)
- ️️️️⚠️警告
我后来更新了这个代码,所以上面👆的投稿的内容不是很准确。等段时间整理md！！
- 更新之后的使用方法 - - - - - 如下:
> 注意：使用之前先要去注册[百度语音合成](http://ai.baidu.com/tech/speech/tts)和[阿凡达云数据](http://www.avatardata.cn/)

### 安装mplayer
```shell
sudo apt-get update
sudo apt-get install mplayer2
```
### 安装python3
> 网上很多
### 安装依赖库
```python
pip3 install requests
pip3 install baidu-aip
# 如果安装不成功建议去看投稿上有写
```
### 最后设置定时运行
> 首先看时区（中国的是CST）、时间对不对
```shell
date
# 时区不对：
sudo dpkg-reconfigure tzdata
# 选择亚洲-上海就可以了

# 时间不对：
sudo ntpd -s -d
```
### clone 此项目
```shell
cd ~
git clone https://github.com/hyhmnn/raspberry
```

### 写入crontab
> 都要使用绝对路径,具体crontab用法去百度

```shell
crontab -e

# 内容
45 7 * * * /usr/bin/python3 /home/pi/raspberry/SimpleClock/main.py > /home/pi/SimpleClock.log 2>&1
```
---
