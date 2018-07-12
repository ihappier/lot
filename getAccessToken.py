import requests as nq

netAdress = '180.101.147.89'
port = '8743'

appID = '4CFpzk3vFme73dJCogtqac6H1EIa'
secret = '6c1qCXEzcp0F0l47iWtvuLYsqlwa'
cert = (
    'D:\智慧热网\\2018\getdata\dianxin\dianxin\cert\client.crt', 'D:\智慧热网\\2018\getdata\dianxin\dianxin\cert\client.key')


def conectLot(appID, secret, cert, netAdress='180.101.147.89', port='8743'):
    """接入平台"""
    url = 'https://' + netAdress + ':' + port + '/iocm/app/sec/v1.1.0/login'
    r = nq.post(url, data={'appId': appID, 'secret': secret}, cert=cert, verify=False)
    if r.status_code == nq.codes.ok:
        d = eval(r.text)
        if d['accessToken']:
            return d
        else:
            return


def refreshToken(appID, secret, cert, refreshToken, netAdress='180.101.147.89', port='8743'):
    """刷新鉴权Token"""
    url = 'https://' + netAdress + ':' + port + '/iocm/app/sec/v1.1.0/refreshToken'
    r = nq.post(url, data={'appId': appID, 'secret': secret, 'refreshToken': refreshToken}, cert=cert, verify=False)
    if r.status_code == nq.codes.ok:
        d = eval(r.text)
        return d


def getDevicesMsg(appID, accessToken, deviceID, cert, netAdress='180.101.147.89', port='8743'):
    """获取已连接设备信息,返回list形式，list[0]是设备ID，list[1]是设备是否激活(true,false)，list[2]是设备名称"""
    url = 'https://' + netAdress + ':' + port + '/iocm/app/reg/v1.1.0/deviceCredentials/' + deviceID
    itemHeaders = {"app_key": appID, "Authorization": "Bearer " + accessToken, "Content-Type": "applicaton/json"}
    m = nq.get(url, headers=itemHeaders, cert=cert, verify=False)
    if m.status_code == nq.codes.ok:
        d = eval(m.text)
        if d['deciveId']:
            return [d['deciveId'], d['activated'], d['name']]
        else:
            return d
    else:
        return '页面不存在'


def registerDevice(appID, nodeId, accessToken, cert, netAdress='180.101.147.89', port='8743'):
    """注册设备"""
    url = 'https://' + netAdress + ':' + port + '/iocm/app/reg/v1.1.0/deviceCredentials?appId=' + appID
    itemHeaders = {"app_key": appID, "Authorization": "Bearer " + accessToken, "Content-Type": "applicaton/json"}
    r = nq.post(url=url, DeprecationWarning={'nodeId': nodeId}, headers=itemHeaders, cert=cert, verify=False)
    if r.status_code == nq.codes.ok:
        return eval(r.text)


def refreshVerifyCode(appID, nodeId, accessToken, cert, netAdress='180.101.147.89', port='8743'):
    """刷新"""
    url = 'https://' + netAdress + ':' + port + '/iocm/app/reg/v1.1.0/deviceCredentials?appId=' + appID
    return d


def modfyDevice(appID, nodeId, accessToken, cert, netAdress='180.101.147.89', port='8743'):
    """"修改设备"""
    return


def deleteDevice(appID, nodeId, accessToken, cert, netAdress='180.101.147.89', port='8743'):
    return


def
