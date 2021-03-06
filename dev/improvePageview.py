import random
import re
import threading
import urllib.error
import urllib.parse
import urllib.request

proxy_list = []
total_proxy = 0

blog_list = ['https://www.biorxiv.org/content/early/2017/09/07/185876',
             'https://www.biorxiv.org/content/early/2017/09/07/185876.full.pdf+html',
             'https://www.biorxiv.org/content/biorxiv/early/2017/09/07/185876.full.pdf']
total_blog = 0

total_visit = 0

total_remove = 0

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]


# request_list = ['http://www.xicidaili.com/nn/','http://www.xicidaili.com/nn/4','http://www.xicidaili.com/nn/5']

def get_proxy_ip():
    global proxy_list
    global total_proxy
    request_list = []
    headers = {
        'Host': 'www.xicidaili.com',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Accept': r'application/json, text/javascript, */*; q=0.01',
        'Referer': r'http://www.xicidaili.com/',
    }
    for i in range(11, 21):
        request_item = "http://www.xicidaili.com/nn/" + str(i)
        request_list.append(request_item)

    for req_id in request_list:
        req = urllib.request.Request(req_id, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')

        ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+', html)
        port_list = re.findall(r'<td>\d+</td>', html)
        for i in range(len(ip_list)):
            total_proxy += 1
            ip = ip_list[i]
            port = re.sub(r'<td>|</td>', '', port_list[i])
            proxy = '%s:%s' % (ip, port)
            proxy_list.append(proxy)
    return proxy_list


def get_proxy_ip2():
    global proxy_list
    global total_proxy
    request_list = []
    headers = {
        'Host': 'http://www.66ip.cn/',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Accept': r'application/json, text/javascript, */*; q=0.01',
        'Referer': r'http://www.66ip.cn/',
    }
    for i in range(1, 50):
        request_item = "http://www.66ip.cn/" + str(i) + ".html"
        request_list.append(request_item)

    for req_id in request_list:
        req = urllib.request.Request(req_id, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')

        ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+', html)
        port_list = re.findall(r'<td>\d+</td>', html)
        for i in range(len(ip_list)):
            total_proxy += 1
            ip = ip_list[i]
            port = re.sub(r'<td>|</td>', '', port_list[i])
            proxy = '%s:%s' % (ip, port)
            proxy_list.append(proxy)
    return proxy_list


def get_proxy_ip3():
    global proxy_list
    global total_proxy
    request_list = []
    headers = {
        # 'Host': 'http://www.youdaili.net/',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        # 'Accept': r'application/json, text/javascript, */*; q=0.01',
        # 'Referer': r'http://www.youdaili.net/',
    }
    # for i in range(2, 6):
    #     request_item = "http://www.youdaili.net/Daili/QQ/36811_" + str(i) + ".html"
    first = "http://www.youdaili.net/Daili/guowai/"
    req = urllib.request.Request(first, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    request_id = re.findall(r'href="http://www.youdaili.net/Daili/guowai/(\d+).html', html)
    print(request_id)

    for item in request_id:
        request_item = "http://www.youdaili.net/Daili/guowai/" + str(item) + ".html"
        request_list.append(request_item)

    print(request_list)
    # request_item="http://www.youdaili.net/Daili/guowai/4821.html"
    # request_list.append(request_item)
    # for i in range(2, 6):
    #     request_item = "http://www.youdaili.net/Daili/QQ/36811_" + str(i) + ".html"
    #     request_list.append(request_item)

    for req_id in request_list:
        req = urllib.request.Request(req_id, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')

        ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+', html)
        port_list = re.findall(r':+\d*@HTTP#', html)
        for i in range(len(ip_list) - 20):
            total_proxy += 1
            ip = ip_list[i]
            print(port_list[i])
            tmp = re.sub(r':', '', port_list[i])
            port = re.sub(r'@HTTP#', '', tmp)
            proxy = '%s:%s' % (ip, port)
            print(port)
            proxy_list.append(proxy)
    print(proxy_list)
    return proxy_list


# def create_blog_list():
#     list1 = []
#     list2 = []
#     global blog_list
#     global total_blog
#     pr = r'href="http://www.cnblogs.com/zpfbuaa/p/(\d+)'
#     rr = re.compile(pr)
#     my_blog = []
#     # my_blog = ['http://www.cnblogs.com/zpfbuaa/p/?page=1', 'http://www.cnblogs.com/zpfbuaa/p/?page=2',
#     #           'http://www.cnblogs.com/zpfbuaa/p/?page=3']
#     for i in range(1, 25):
#         blogitem = "http://www.cnblogs.com/zpfbuaa/p/?page=" + str(i)
#         my_blog.append(blogitem)
#
#     for item in my_blog:
#         req = urllib.request.Request(item)
#
#         # proxy_ip = random.choice(proxyIP.proxy_list)  # 在proxy_list中随机取一个ip
#         # print proxy_ip
#         # proxy_support = urllib2.ProxyHandler(proxy_ip)
#         # opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
#
#         req.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)")
#         cn = urllib.request.urlopen(req)
#         f = cn.read().decode(encoding='utf8')
#         # print(f)
#         list2 = re.findall(rr, f)
#         list1 = list1 + list2
#         cn.close()
#     for blog_key in list1:
#         total_blog = total_blog + 1
#         url = 'http://www.cnblogs.com/zpfbuaa/p/' + blog_key + ".html"
#         blog_list.append(url)


def main():
    # create_blog_list()
    get_proxy_ip()
    # get_proxy_ip2()
    # get_proxy_ip3()


def sorry_to_visit_you(url):
    global total_visit
    global proxy_list
    global total_proxy
    global total_remove
    proxy_ip = random.choice(proxy_list)
    user_agent = random.choice(user_agent_list)
    print(proxy_ip)
    print(user_agent)

    proxy_support = urllib.request.ProxyHandler({'http': proxy_ip})
    opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

    req = urllib.request.Request(url)
    req.add_header("User-Agent", user_agent)

    try:
        c = urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        proxy_list.remove(proxy_ip)
        total_proxy -= 1
        total_remove += 1
        print("删除ip")
        print(proxy_ip)
        print("当前移除代理ip个数为:%d" % total_remove)

        print('******打开失败！******')

    else:
        total_visit += 1
        print(('OK!总计成功%d次!' % total_visit))
        print("当前刷的网址为%s" % url)
        print("当前剩余代理ip个数为:%d" % total_proxy)
    sem.release()


if __name__ == "__main__":
    main()
    print("开始刷访问量！")
    print("共计代理总数为%s个！" % total_proxy)
    print("共计博客个数为%s个！" % total_blog)
    max_thread = 5
    sem = threading.BoundedSemaphore(max_thread)
    while 1:
        for blog_url in blog_list:
            sem.acquire()
            T = threading.Thread(target=sorry_to_visit_you, args=(blog_url,))
            T.start()