# wechatClub
> python 3

## 如何使用
> 小白看这个可能会有点困难

### 安装mplayer
```shell
sudo apt-get update
sudo apt-get install mplayer2
```

### 安装ngrok
```
注册 https://ngrok.com/

注册完会跳转到 get-started 界面
照着做就可以了~

1- Download ngrok
2- Unzip to install
3- Connect your account
4- Fire it up
```

### 设置相机
```
sudo raspi-config
选择 5  Interfacing Options
选择 P1 Camera
接下来机会问你是否同意使能Pi camera，选择是；然后重启

# 测试一下
aspistill -t 1000 -o tmp_image.jpg &

# 如果解决不了，可以看这个http://www.cnblogs.com/uestc-mm/p/7587783.html
```

### 设置一下树莓派的语言字符
> 后面有坑，最好设置一下
```shell
1.进入到系统的语言配置页面
    sudo raspi-config
 
2.在像 BIOS 界面的界面中依次进行操作
    空格操作勾选/取消勾选，tab 跳转到[确定，取消]选择区域

3.选择 Localisation Options
    选择 Change Locale
    取消勾选 en_GB.UTF-8 UTF-8，勾选 en_US.UTF-8, zh_CN.UTF-8 UTF-8, zh_CN.GBK GBK
```


### 安装一些python库
```
sudo pip3 install baidu-aip,werobot,requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 下载运行
```
git clone https://github.com/hyhm2n/RaspberryPiApps

cd RaspberryPiApps/wechatClub/

# 将代码中需要替换的地方替换一下(一些密钥等，需要替换成自己的)

sudo python3 index.py &
ngrok http 80

之后就如视频一样操作就好了 
在 01：14 处~
https://www.bilibili.com/video/av28630618
```
