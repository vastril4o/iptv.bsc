import json
import requests

import xbmc
import xbmcaddon

import api_login
import api_debug


_addon = xbmcaddon.Addon()
_url = _addon.getSetting('settings_api_url')
_url_live = _addon.getSetting('settings_api_url_live')
_url_epg = _addon.getSetting('settings_api_url_epg')
_url_logo = _addon.getSetting('settings_api_url_logo')
_timeout = float(_addon.getSetting('settings_timeout'))


def get_live(session):
    api_login._s.headers.update({'Access-Control-Request-Method': 'POST'})
    api_login._s.headers.update({'Access-Control-Request-Headers': 'ssbulsatapi'})
    api_login._s.headers.update({'SSBULSATAPI': session})
    api_login._s.options(_url + '/' + _url_live, timeout = _timeout, headers = api_login._ua)
    
    r = api_login._s.post(_url + '/' + _url_live, timeout = _timeout, headers = api_login._ua)
    
    # debug
    api_debug.show_notifycation('LIVE ' + str(r.status_code == requests.codes.ok))
    
    if r.status_code != requests.codes.ok:
        return [{}]
    else:
        # debug
        api_debug.log('LIVE ' + str(r.json()))
        
        return r.json()


def get_epg(live):
    for i, channel in enumerate(live):
        if channel.has_key('program'):
            #'epg': 'nownext' / '1day' / '1week'
            r = api_login._s.post(_url + '/' + _url_epg, timeout = _timeout, headers = api_login._ua, data = {'epg': '1week', 'channel': channel['epg_name']})
            
            if r.status_code == requests.codes.ok:
                channel['program'] = r.json().items()[0][1]['programme']
    
    # debug
    api_debug.show_notifycation('EPG ' + str(r.status_code == requests.codes.ok))
    api_debug.log('EPG ' + str(live))
    
    return live


def get_logo(live):
    r = api_login._s.get(_url + '/' + _url_logo, timeout = _timeout, headers = api_login._ua)
    
    # debug
    api_debug.show_notifycation('LOGO ' + str(r.status_code == requests.codes.ok))
    
    return live
