import requests
url = 'http://www.littlebigplay.com/submitAir.php'
payload = {'score': '2147483647', 'nickname': 'BALANCE66','gameMode':'2','gameid':'145'}
page = requests.post(url, data=payload)
print page
