# -*- coding:utf-8 -*-
# !/usr/bin/python3

from os import geteuid
from scapy.all import *
from IPy import IP
import json
import requests
from sys import exit

def ip_conf(cidr):
    return [str(i) for i in IP(cidr)]

def mac_info(mac_addr):
    url = 'https://www.sunif.cn/m.php?mac={}'
    res = requests.get(url.format(mac_addr)).text
    return json.loads(res)['vendor']

'''
def scapy_arp_request(ip_address , ifname = 'wlp2s0',queue = None):
    result_raw = srp(Ether(dst = 'FF:FF:FF:FF:FF:FF')#srp  二层帧
        /ARP(op = 1,hwdst = '00:00:00:00:00:00',pdst = ip_address),#ARP询问操作，op置1
        timeout = 1,#等待1s
        iface = ifname,#二层一定要填写接口
        verbose = False)#关闭发送数据提示信息
#result_raw接收到的数据如：(<Results: TCP:0 UDP:0 ICMP:0 Other:1>, <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>)
#[0]为相应的数据，[1]为未相应的数据(等待1s，所以有可能会产生未响应的数据)
    try:
        result_list = result_raw[0].res #把响应的数据包对，产生为清单
#result_list数据为展开的信息，如：[(<Ether  dst=FF:FF:FF:FF:FF:FF type=0x806 |<ARP  op=who-has hwdst=00:00:00:00:00:00 pdst=172.17.174.73 |>>, <Ether  dst=e0:3f:49:a1:99:6c src=58:69:6c:5e:70:ec type=0x806 |<ARP  hwtype=0x1 ptype=0x800 hwlen=6 plen=4 op=is-at hwsrc=58:69:6c:5e:70:ec psrc=172.17.174.73 hwdst=e0:3f:49:a1:99:6c pdst=172.17.171.178 |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>)]

#可以看到，result_list中只有一组数据，下标为0。在这一组里，[1]代表接收到的包，[0]代表发送的数据包
#[2]ARP头部字段的['hwsrc']字段，作为返回值返回

        if queue == None:
            #return result_list[0][1][1].fields['hwsrc']
            return result_list[0][1].getlayer(ARP).fields['hwsrc']

        else:
            queue.put((ip_address,result_list[0][1].getlayer(ARP).fields['hwsrc']))

    except:
        return
'''

if __name__ == "__main__":
    if geteuid():
        exit('[-] please run as root')
    cidr = '192.168.2.0/24'    #网段
    ifname='wlp2s0'    #网卡
    ip_link_mac = []
    iplist = ip_conf(cidr)
    for ip in iplist:
        data = {}
        data['ip'] = ip
        tmp = getmacbyip(ip)
        data['mac'] = tmp
        data['vendor'] = mac_info(tmp)
        print(data)
        if tmp != None:
            ip_link_mac.append(data)
    with open('sniffer.json', 'a') as f:
        json.dump(ip_link_mac,f)

        
