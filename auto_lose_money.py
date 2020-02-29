# -*- coding:utf-8 -*-
import requests
import json
import time

def swing():
    data = json.loads(requests.get('https://api.huobi.pro/market/history/kline?period=1day&size=1&symbol=mxusdt').text)
    start1day = data['data'][0]['open']
    end = data['data'][0]['close']
    amplitude = (end-start1day)/start1day
    return float(amplitude)*100

class Notice(object):
    def __init__(self,amplitude):
        self.amplitude = amplitude
    def buy_notice(self):
        for i in range(8):
            requests.get('https://api.day.app/FuvhVQxYYyDqkSjQppGEMT/buy/跌幅{}'.format(self.amplitude))
    def sell_notice(self):
        for i in range(8):
            requests.get('https://api.day.app/FuvhVQxYYyDqkSjQppGEMT/sell/增幅{}'.format(self.amplitude))

def main():
    while True:
        amplitude = swing()
        a = Notice(amplitude)
        if amplitude <= -10.0:
            a.buy_notice()
        elif amplitude >= 10.0:
            a.sell_notice()
        del a
        time.sleep(60)
if __name__ == "__main__":
    main()