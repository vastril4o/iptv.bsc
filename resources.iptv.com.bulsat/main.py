import xbmc
import xbmcaddon

import json

import api_debug
import api_data
import api_login
import api_iostream


_addon = xbmcaddon.Addon()
_user = _addon.getSetting('settings_username')
_password = _addon.getSetting('settings_password')
_files_path = _addon.getSetting('settings_files_path')
_iptv_simple_reload = _addon.getSetting('settings_iptv_simple_reload')
_download_epg = _addon.getSetting('settings_epg')
_download_logo = _addon.getSetting('settings_logo')


if not _user or not _password or not _files_path:
    api_debug.show_notifycation('Settings empty')
else:
    api_debug.show_progress()
    
    # login
    session = api_login.login(_user, _password)
    api_debug.update_progress(25)

    # channel
    json_channel = api_data.get_channel(session)
    api_iostream.save_live(json_channel)
    api_debug.update_progress(50)
    
    # epg
    if _download_epg == 'true':
        json_epg = api_data.get_epg(json_channel)
        api_iostream.save_epg(json_epg)
        api_debug.update_progress(75)
    
    # logo
    if _download_logo == 'true':
        api_debug.update_progress(100)
        #json_logo = api_data.get_logo(json_live)
        #api_iostream.save_logo(json_live)
        
    api_debug.update_progress(100)
    api_debug.close_progress()
    
    if _iptv_simple_reload == 'true':
        jsonAction = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":"toggle"},"id":1}'
        
        xbmc.executeJSONRPC(jsonAction)
        xbmc.sleep(1000)
        xbmc.executeJSONRPC(jsonAction)
