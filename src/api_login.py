import requests
import aes
import base64

import xbmc
import xbmcaddon

import api_debug


_addon = xbmcaddon.Addon()
_url = _addon.getSetting('settings_api_url')
_timeout = float(_addon.getSetting('settings_timeout'))
_os = int(_addon.getSetting('settings_os'))

_s = requests.Session()

_ua = {
    'Host':'api.iptv.bulsat.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept':'*/*',
    'Accept-Language':'bg-BG,bg;q=0.8,en;q=0.6',
    'Accept-Encoding':'gzip, deflate, br',
    'Referer':'https://test.iptv.bulsat.com/iptv-login.php',
    'Origin':'https://test.iptv.bulsat.com',
    'Connection':'keep-alive'
}

_os_list = ['pcweb', 'samsungtv']

def login(username, password):
    url_auth = 'auth'
    # change auth url for diffrent then 'pcweb'
    if _os != 0:
        url_auth = '?' + url_auth
    
    r = _s.post(_url + '/' + url_auth, timeout = _timeout, headers = _ua)
    key = r.headers['challenge']
    session = r.headers['ssbulsatapi']
    
    if r.headers['logged'] == 'true':
        return session
    
    _s.headers.update({'SSBULSATAPI': session})
    
    enc = aes.AESModeOfOperationECB(key)
    password_crypt = enc.encrypt(password + (16 - len(password) % 16) * '\0')
    
    r = _s.post(_url + '/' + url_auth, timeout = _timeout, headers = _ua, data = {
        'user':['', username],
        'device_id':['', _os_list[_os]],
        'device_name':['', _os_list[_os]],
        'os_version':['', _os_list[_os]],
        'os_type':['', _os_list[_os]],
        'app_version':['', '0.01'],
        'pass':['', base64.b64encode(password_crypt)]
    })
    
    # debug
    api_debug.notifycation('Login ' + r.headers['logged'])
    api_debug.log('Login ' + str(r.request.headers))
    
    return session
