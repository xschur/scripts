#!/usr/bin/python3
import os
import random


def main():
    def random_mac():
        new_mac = []
        for i in range(6):
            x = "".join(random.sample('0123456789abcdef', 2))
            new_mac.append(x)
        new_mac = ":".join(new_mac)
        return new_mac

    mac = random_mac()
    input('Change your Mac addr temporarily to {}, press Enter to continue:\n'.format(mac))
    os.system('sudo ifconfig wlp2s0 down')
    os.system('sudo ifconfig wlp2s0 hw ether {}'.format(mac))
    os.system('sudo ifconfig wlp2s0 up')

if __name__ == '__main__':
    try:
        main()
    except:
        print('Mac address has not changed')