import requests
check='5'
if check=='5':
    a=''
    a=a+requests.get(url='https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt').text.strip()+'\n'
    a=a+requests.get(url='https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt').text.strip()+'\n'

    file=open('proxy.txt','w')
    file.write(a)
    file.close()
    file=open('proxy.txt')
    a=file.readlines()
    a=list(set(a))
    file.close()
    file=open('proxy.txt','w')
    for i in a:
      if i.strip()!='':
        file.write(i)
    file.close()

