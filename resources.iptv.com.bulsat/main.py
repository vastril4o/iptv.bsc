import xbmc
import xbmcaddon

import api_debug
import api_data
import api_login
import api_iostream


_addon = xbmcaddon.Addon()
_user = _addon.getSetting('settings_username')
_password = _addon.getSetting('settings_password')
_files_path = _addon.getSetting('settings_files_path')
_iptv_pvr_reload = _addon.getSetting('settings_iptv_pvr_reload')
_download_epg = _addon.getSetting('settings_epg')
_download_logo = _addon.getSetting('settings_logo')


if not _user or not _password or not _files_path:
    api_debug.show_notifycation('Settings empty')
else:
    api_debug.show_progress()
    
    # login
    session = api_login.login(_user, _password)
    api_debug.update_progress(10)

    # live
    json_live = api_data.get_live(session)
    api_debug.update_progress(20)

    api_iostream.save_live(json_live)
    api_debug.update_progress(30)
    
    # epg
    if _download_epg == 'true':
        json_epg = api_data.get_epg(json_live)
        api_debug.update_progress(40)
        
        api_iostream.save_epg(json_epg)
        api_debug.update_progress(50)
    
    # logo
    if _download_logo == 'true':
        #json_logo = api_data.get_logo(json_live)
        api_debug.update_progress(60)
        
        #api_iostream.save_epg(json_live)
        #api_debug.update_progress(50)


    api_debug.close_progress()
    
    if _iptv_pvr_reload == 'true':
        xbmc.executebuiltin('XBMC.StopPVRManager')
        xbmc.sleep(1000)
        xbmc.executebuiltin('XBMC.StartPVRManager')
