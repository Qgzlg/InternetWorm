#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数

index = 1
count = 600
def getHtml(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8', errors='ignore')
    return html

def getImg(html):
    reg = '"objURL"\:"(.+?\.[a-zA-Z]{3})"'    #正则表达式，得到图片地址
    imgre = re.compile(reg, re.I)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    for imgurl in imglist:
        try :
            global count
            urllib.request.urlretrieve(imgurl,'E:\IMG\%s.png' % count)
            count +=1
        except Exception as e:
            continue;
    return None

def getButtonUrl(html):
    global index
    index += 1
    reg = r'<a href="/search/flip.*</a>'
    imgre = re.compile(reg, re.I)
    imglist = re.findall(imgre,html)
    str2 = str(index) +  "</span></a>"
    for imgurl in imglist:
        try :
            if str2 in imgurl :
                url = ""
                reg = r'<a href="(/search/flip.*)"><span'
                imgre = re.compile(reg, re.I)
                imglist = re.findall(imgre, imgurl)
                if len(imglist) > 0 :
                    url = imglist[0]
                    print(url)
                    html = getHtml("http://image.baidu.com" + url)
                    print(getImg(html))
                    getButtonUrl(html)
                    break;
        except Exception as e:
            continue;
    return None


html = getHtml("https://www.google.com/search?q=%E5%9B%BE%E7%89%87&newwindow=1&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwj-meDf1pHcAhXGfrwKHcuvCUcQsAQINg&biw=1600&bih=718")
print(getImg(html))
getButtonUrl(html)