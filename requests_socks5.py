import requests
url = ''
socks5_proxy = "socks5h://127.0.0.1:1081"
sess = requests.Session()
sess.proxies = {"https":socks5_proxy,"http":socks5_proxy}
sess.get(url)