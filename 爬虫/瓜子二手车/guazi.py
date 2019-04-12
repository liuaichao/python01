# -*- coding:utf-8 -*-
import time
from lxml import etree
from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options
url = 'https://www.guazi.com/weifang/buy'
# headers = {
#     'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
# }
# req = requests.get(url, headers=headers)
# print(req.text)
# driver = webdriver.Chrome()
# driver.get(url)
# print(driver.page_source)
# driver.quit()
def get_data(urls):
    for url in urls:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        html = etree.HTML(driver.page_source)
        car_name = html.xpath('//ul[@class="carlist clearfix js-top"]/li/a/@title')
        buy_data = html.xpath('//ul[@class="carlist clearfix js-top"]/li/a/div[@class="t-i"]//text()')
        buy_time = list(buy_data)[0::5]
        buy_gongli = list(buy_data)[2::5]
        buy_type = list(buy_data)[4::5]
        buy_price = html.xpath('//div[@class="t-price"]/p/text()')
        buy_price = [i+'万' for i in buy_price]
        buy_xinche = []
        for i in range(len(car_name)):
            buy_xin = html.xpath('//ul[@class="carlist clearfix js-top"]/li[{0}]/a/div[@class="t-price"]/em/text()'.format(i+1))
            if buy_xin ==[]:
                buy_xinche.append(None)
            else:
                buy_xinche.append(buy_xin[0])
        data = []
        for name, times, gongli, types, price, xinche in zip(car_name, buy_time, buy_gongli,
                                                             buy_type,buy_price,buy_xinche):
            group = (name, times, gongli, types, price, xinche)
            data.append(group)
        to_csv(data)
        # print(data)
        driver.quit()
        time.sleep(3)

def to_csv(data):
    with open('guazi.csv', 'a',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


if __name__ == '__main__':
    #https://www.guazi.com/weifang/buy/o3/#bread
    #https://www.guazi.com/weifang/buy
    url1 = ['https://www.guazi.com/weifang/buy']
    url2 = ['https://www.guazi.com/weifang/buy/o{0}/#bread'.format(i) for i in range(2,51)]
    urls = url1 + url2
    # print(urls)
    get_data(urls)
