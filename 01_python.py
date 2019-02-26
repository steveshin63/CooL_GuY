print('hello')

import webbrowser
import time

base_url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='

idols = ['방탄소년단','아이유','ITZY']
for name in idols:
    webbrowser.open(base_url+name)
    time.sleep(5)