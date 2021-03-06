import asyncio
import re
import sys
import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0'}
    async with session.get(url, headers=headers,ssl=False) as resp:
        return await resp.text()

async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title')+' ---- '+url)


def main():
    url_s = []
    with open('domain_bjtu.edu.cn.txt','r') as f:
        urls = f.readlines()
    for i in urls:
        i = i.strip()
        i = 'http://'+i+'/'
        url_s.append(i)
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in url_s]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    sys.exit()

if __name__ == '__main__':
    main()
