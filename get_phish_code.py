#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:schur
'''
Get phish_url in phishtank,and brute to get source code
'''
import aiohttp
import asyncio
import urllib.parse

success_dir = []
success_file = []

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
}

def split_and_combine(url):
    dir_list  = []
    file_list = []
    remote_file = []
    ext_list = [".zip",".tar.gz",".rar",".txt",".7z",".bak",".gz",".tgz",".bz2"]
    url = url.split("/")
    main_url = url[0]+"//"+url[2]+'/'
    dir = url[3:]
    for i in dir:
        main_url = main_url+i+'/'
        dir_list.append(main_url)
    if len(dir_list)>=1:
        del dir_list[-1]
    for i in dir:
        for j in ext_list:
            file = i+j
            file_list.append(file)
    for i in dir_list:
        for j in file_list:
            remote_file.append(i+j)
    return dir_list,remote_file

async def judge(url):
    global success_dir
    global success_file
    print('[+]handing :'+url.strip())
    dir_list,remote_file = split_and_combine(url.strip())
    async with aiohttp.ClientSession() as sess:
        for i in remote_file:
            try:
                #print("file:"+i)
                async with sess.get(i,headers=headers,timeout=3) as res:
                    if res.status == 200:
                        success_file.append(i+'\n')
            except Exception as e:
                print(str(e))
        for i in dir_list:
            try:
                #print('dir'+i)
                async with sess.get(i,headers=headers,timeout=3) as res:
                    html = await res.text()
                    if "Index" in html:
                        success_dir.append(i+'\n')
            except Exception as e:
                print(str(e))           

def main():
    with open('2.csv','r') as f:
        data = f.readlines()
    loop = asyncio.get_event_loop()
    tasks =  [judge(url) for url in data]
    results = loop.run_until_complete(asyncio.wait(tasks))
    with open("result.txt",'a') as f:
        f.writelines(success_dir)
        f.writelines(success_file)

if __name__ == "__main__":
    main()