import requests as nq
import os, sys

path = os.path.dirname(os.path.realpath(__file__))
netAdress = '180.101.147.89'
port = '8743'

appID = '4CFpzk3vFme73dJCogtqac6H1EIa'
secret = '6c1qCXEzcp0F0l47iWtvuLYsqlwa'
cert = (
    path + '\cert\client.crt', path + '\cert\client.key')


def conectIoT(appID, secret, cert, netAdress='180.101.147.89', port='8743'):
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


def getDevicesStatus(appID, accessToken, deviceID, cert, netAdress='180.101.147.89', port='8743'):
    """查询设备是否激活,返回list形式，list[0]是设备ID，list[1]是设备是否激活(true,false)，list[2]是设备名称"""
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


def modfyDevice(appID, deviceId, accessToken, cert, netAdress='180.101.147.89', port='8743'):
    """"修改设备"""
    url = "https://" + netAdress + ":" + port + "/iocm/app/reg/v1.1.0/deviceCredentials/" + deviceId + "?appId=" + appID
    itemHeaders = {"app_key": appID, "Authorization": "Bearer " + accessToken}
    r = nq.put(url=url, headers=itemHeaders, cert=cert, verify=False)
    if r.status_code == 204:  # 修改后，如果返回的status code值为204，则返回修改成功，否则返回修改失败
        return True
    else:
        return False


def deleteDevice(appID, accessToken, deviceId, cert, netAdress='180.101.147.89', port='8743'):
    """删除设备"""
    url = "https://" + netAdress + ":" + port + "/iocm/app/dm/v1.4.0/devices/" + deviceId + "?"
    itemHeaders = {"app_key": appID, "Authorization": "Bearer " + accessToken}
    r = nq.delete(url=url, headers=itemHeaders, cert=cert, verify=False)
    if r.status_code == 204:  # 如果返回status code值为204，返回删除成功，否则返回删除失败
        return True
    else:
        return False


def getDeviceHistoryData(appID, accessToken, deviceID, gateWayId, cert, netAdress='180.101.147.89', port='8743'):
    """获取设备历史数据"""
    url = "https://" + netAdress + ":" + port + "/iocm/app/data/v1.2.0/deviceDataHistory?"
    key = {"deviceId": deviceID, "gatewayId": deviceID, "appId": appID, "pageNo": 1, "pageSize": 11}
    itemHeaders = {"app_key": appID, "Authorization": "Bearer " + accessToken, "Content-Type": "applicaton/json"}
    r = nq.get(url=url, params=key, cert=cert, headers=itemHeaders, verify=False)
    data = eval(r.text)['deviceDataHistoryDTOs']
    return data


def analysisHistoryData(data):
    """解析历史数据"""
    data_anakysied = {}
    for x in data:
        data_anakysied.update({x['serviceId']: x['data']})
    return data_anakysied


def getDeviceMsg(appID, accessToken, deviceID, cert, netAdress='180.101.147.89', port='8743'):
    """
    查询设备信息返回字典类型，
    ‘deviceID’：设备ID，
    ‘gatewayID’：网关ID，如果是直连设备则与设备ID相同
    ‘nodeType’：节点类型，取值ENDPOINT/GATEWAY/UNKNOW
    ‘createTime’：创建设备的时间， 时间格式：yyyyMMdd'T'HHmmss'Z'
    ‘lastModifiedTime’：最后修改设备的时间
    ‘deviceInfo’：设备信息
    ‘services’：设备服务列表
    """
    url = "https://" + netAdress + ":" + port + "/iocm/app/dm/v1.4.0/devices/" + deviceID + "?" + "appId=" + appID
    itemHeaders = {"app_key": appID, "Authorization": "Bearer " + accessToken, "Content-Type": "applicaton/json"}
    r = nq.get(url, headers=itemHeaders, cert=cert, verify=False)
    data = eval(r.text)
    return data


def get_device_service(app_id, access_token, device_id, cert, net_address='180.101.147.89', port='8743'):
    """
    获取设备服务信息
    “deviceCapabilitys” ：设备能力 为list，只有一个子项，子项为dic包括
        {
        “deviceId”：设备ID ，字符串类型
        “serviceCapabilities”：服务项目，list类型，子项为dic，包括
            {
            “serviceId”：服务ID
            “serviceType”：设备的服务类型
            “option”：设备的服务选项

            }
        }
    """
    url = "https://" + netAdress + ":" + port + "/iocm/app/data/v1.1.0/deviceCapabilities?"
    key = {"deviceId": device_id, "gatewayId": device_id, "appId": app_id}
    item_headers = {"app_key": app_id, "Authorization": "Bearer " + access_token, "Content-Type": "applicaton/json"}
    r = nq.get(url=url, params=key, cert=cert, headers=item_headers, verify=False)
    data = eval(r.text)
    return data


def send_command(app_key, access_token, cert, device_id, command, net_address='180.101.147.89', port='8743'):
    """"
    下发命令
    需要输入参数appId，accessToken，cert(证书)，deviceId,command(字典类型)
    """
    url = "https://" + net_address + ":" + port + "/iocm/app/cmd/v1.4.0/deviceCommands"
    key = {"deviceId": device_id, "command": command}
    item_headers = {"app_key": app_key, "Authorization": "Bearer " + access_token, "Content-Type": "applicaton/json"}
    r = nq.post(url=url, headers=item_headers, params=key, cert=cert, verify=False)
    if r.status_code == 201:
        return True
    else:
        return False
