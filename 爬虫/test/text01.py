# -*- coding:utf-8 -*-
import requests
import os
import csv
csv_data = csv.reader(open('D:\\python程序\\爬虫\\yello_net\\yello_url.csv','r'))
csv_data = list(csv_data)
csv_data = csv_data[::2]
NETWORK_STATUS = True
headers = {
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
for data in csv_data:
    name = data[0]
    url = data[1]
    # print(name, url)
    path = 'D:\\python程序\\爬虫\\text\\ye'
    try:
        req = requests.get(url, timeout=10)
        print('下载开始')
        os.system('you-get -o {0} -O {1} {2}'.format(path, name, url))
        print('下载结束')
    except:
        global NETWORK_STATUS
        NETWORK_STATUS = False  # 请求超时改变状态

        if NETWORK_STATUS == False:
            '''请求超时'''
            for i in range(1, 10):
                print
                '请求超时，第%s次重复请求' % i
                response = requests.post(url, headers=headers, data=data, timeout=5)
                if response.status_code == 200:
                    break
