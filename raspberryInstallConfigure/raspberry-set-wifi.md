# 最简单的办法
```shell
sudo raspi-config
```
设置wifi

# scp简单使用
scp pi@192.168.1.12:/home/pi/image.jpg ./

# 树莓派配置wifi

- wifi启动设置：
```shell
sudo vim /etc/network/interfaces

auto wlan0
allow-hotplug wlan0
iface wlan0 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

- wifi密码的设置：
```shell
vim /etc/wpa_supplicant/wpa_supplicant.conf
# 所有的WiFi连接配置都在这里了：
# 最常用的配置。WPA-PSK 加密方式。

network={
  ssid="*******"
  psk="********"
  key_mgmt=WPA-PSK
  priority=5
}
# *priority 是指连接优先级，数字越大优先级越高（不可以是负数）。
```
- 设置静态ip
```shell
vim /etc/dhcpcd.conf
# 添加无线网络的固定IP，则添加如下内容：
# **注意ip需要更改

interface wlan0
static ip_address=192.168.1.110/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1 114.114.114.114
```

- 重启wifi
```shell
sudo ifdown wlan0
sudo ifup wlan0
```

- 查看网卡信息
```shell
ifconfig -a
```
