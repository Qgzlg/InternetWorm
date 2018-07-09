#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数

count = 670
def getHtml(url):
    user_agent = '"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8', errors='ignore')
    return html

def getText(url):
    fo = open(url,'r', encoding = "utf-8")
    html = fo.read()
    return html

def getImg(html):
    try:
        reg = '<a jsname="hSRGPd" href="(.+?uact=8)"'    #正则表达式，得到图片地址
        imgre_1 = re.compile(reg, re.I)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
        imglist_1 = re.findall(imgre_1,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
        #把筛选的图片地址通过for循环遍历并保存到本地
        #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
        for imgLink in imglist_1:
            try :
                global count
                imgLink = imgLink.replace("%3A", ":")
                imgLink = imgLink.replace("%2F", "/")
                imgLink = imgLink.replace("&amp;", "&")
                html = getHtml(imgLink)
                reg = 'content="(.+?\.[a-zA-Z]{3})"'  # 正则表达式，得到图片地址
                imgre_2 = re.compile(reg, re.I)  # re.compile() 可以把正则表达式编译成一个正则表达式对象.
                imglist_2 = re.findall(imgre_2, html)
                for imgurl in imglist_2:
                    if ('jpg' == imgurl[-3 : ] or 'png' == imgurl[-3 : ]) :
                        urllib.request.urlretrieve(imgurl, 'E:\IMG\%s.png' % count)
                        count +=1
            except Exception as e:
                continue
    except Exception as e:
        return None
    return None

html = getText("camera.html")
print(getImg(html))