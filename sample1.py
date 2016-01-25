#-*- coding: utf-8 -*-

import urllib
from json import *

def qqvideoparse(url):


	jsurl = "http://vv.video.qq.com/getinfo?vids=c001640aimv&otype=json&defaultfmt=fhd"
	jspage = urllib.urlopen(jsurl)
	data = jspage.read()[13:-1]

	jsdata = JSONDecoder().decode(data)

	fvkey =  jsdata['vl']['vi'][0]['fvkey']
	keyid =  jsdata['vl']['vi'][0]['cl']['ci'][0]['keyid'].split(".")
	fn = keyid[0] + ".p" + keyid[1][2:] + "." + keyid[2] + ".mp4"
	server = jsdata['vl']['vi'][0]['ul']['ui'][3]['url']

	downurl = server + fn + "?vkey=" + fvkey + "?type=mp4"
	return downurl

url = raw_input("腾讯视频页面地址:")
downurl = qqvideoparse(url)
print "视频下载地址："
print downurl