import requests as nq 


netAdress = '180.101.147.89'
port = '8743'
url = 'https://' + netAdress + ':' + port + '/iocm/app/sec/v1.1.0/login'
appID = '4CFpzk3vFme73dJCogtqac6H1EIa'
sectet = '6c1qCXEzcp0F0l47iWtvuLYsqlwa'
cert = ('D:\智慧热网\\2018\iot\cert\client.crt', 'D:\智慧热网\\2018\iot\cert\client.key')
r = nq.post(url ,data={'appId':'4CFpzk3vFme73dJCogtqac6H1EIa','secret':'6c1qCXEzcp0F0l47iWtvuLYsqlwa'},cert = cert, verify=False)
d = eval(r.text)
print (r.status_code)