import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request
import os


folder= './figures'
# 保存先フォルダ名

os.makedirs(folder, exist_ok=True)
# フォルダ名でディレクトリを作成する

url_list= []
title_list=[]

url_url = "https://www.google.com/search?q=%E3%82%8A%E3%82%93%E3%81%94&sxsrf=ACYBGNQSQombi7OznFdW86BbQTX4qUP2hg:1578292629354&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi1wJicru7mAhUnG6YKHT3XD5gQ_AUoAXoECBIQAw&biw=1690&bih=975#imgrc=_"
url_url = "https://www.google.com/search?q=%E5%9B%BD%E6%97%97&sxsrf=ACYBGNQvT69ycxqTi1bMVg-ZBYPlWn-0Hg:1578299085327&source=lnms&tbm=isch&sa=X&ved=2ahUKEwir29Gixu7mAhUExIsBHfb-CSwQ_AUoAXoECBAQAw&biw=1690&bih=975&dpr=1.1"
# スクレイピングするURL

def get_hp(url_url):
	res = requests.get(url_url)
	res.raise_for_status() #エラーならここで例外を発生させる
	return res.text


def pickup_tag(url_url):
	soup = BeautifulSoup(get_hp(url_url), 'html.parser')
	# get_tag = soup.select("img.thumbnail")
	get_tag = soup.select("img")
	#get_tag = list(dict.fromkeys(get_tag))
	if get_tag is None:
		print("見つかりません")
		quit()
	return get_tag

print("element :", len(pickup_tag(url_url)))


def get_photo_url(url_url):
	for temp in pickup_tag(url_url):
		url_fact = temp.get("src")
		yield url_fact
		url_list.append(url_fact)


def get_title(url_url):
	for i in get_photo_url(url_url):
		pass

	soup = BeautifulSoup(get_hp(url_url), 'html.parser')
	# get_title_tag = soup.select('h2 a')
	get_title_tag = soup.select('img')
	if get_title_tag is None:
		print('見つかりません')
		quit()
	for sample in get_title_tag:
		element_titile = sample.get_text()
		yield element_titile
		title_list.append(element_titile)

for i in get_title(url_url):
	pass

print(len(title_list))
# """
for n in range(len(url_list)):
	# image_url = "https://www.google.com/?hl=ja" + url_list[n]
	image_url = url_list[n]
	print('画像をダウンロード中 {}...'.format(image_url))
	res = requests.get(image_url)
	res.raise_for_status()
	# image_file = open(os.path.join(folder, os.path.basename(title_list[n]+'.jpg')), 'wb')
	image_file = open(os.path.join(folder, os.path.basename(str(n) +'.jpg')), 'wb')
	# for chunk in res.iter_content(100000):
	for chunk in res.iter_content(100000):
		image_file.write(chunk)
	image_file.close()
# """
