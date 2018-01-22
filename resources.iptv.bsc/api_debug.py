import xbmc
import xbmcaddon
import xbmcgui


_addon = xbmcaddon.Addon()
_api_name = _addon.getAddonInfo('name')
_api_icon = _addon.getAddonInfo('icon')
_dialog_progress = xbmcgui.DialogProgressBG()


def show_notifycation(msg):
    if _addon.getSetting('settings_notification') == 'true':
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(_api_name, msg, 1000, _api_icon))


def log(msg):
    if _addon.getSetting('settings_notification') == 'true':
        xbmc.log(_api_name + ': ' + unicode(msg))


def show_progress():
    _dialog_progress.create(heading = _api_name)


def update_progress(progress):
    _dialog_progress.update(progress)

def close_progress():
    xbmc.sleep(1000)
    _dialog_progress.close()
