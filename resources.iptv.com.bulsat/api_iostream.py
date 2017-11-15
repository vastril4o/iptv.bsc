import io
import os
import StringIO
import gzip
import xmltv
import time

import xbmc
import xbmcaddon

import api_debug


_addon = xbmcaddon.Addon()
_files_path = _addon.getSetting('settings_files_path')


def save_channel(live):
    play_list = u'#EXTM3U\n'
    for i, channel in enumerate(live):
        ch_epg_name = channel['epg_name']
        ch_title = channel['title']
        ch_sources = channel['sources']
        ch_radio = channel['radio']
        ch_genre = channel['genre']
        ch_id = channel['channel']
        
        play_list = play_list + '#EXTINF:-1 radio="%s" group-title="%s" tvg-logo="%s" tvg-id="%s",%s\n%s\n' % (ch_radio, ch_genre, ch_epg_name + '.png', ch_epg_name, ch_title, ch_sources)
        
    f_m3u = open(os.path.join(_files_path, '', 'bulsat.m3u'), 'wb+')
    f_m3u.write(play_list.encode('utf-8', 'replace'))
    f_m3u.close()


def save_epg(live):
    w = xmltv.Writer(encoding='UTF-8', date=str(time.time()), source_info_url="", source_info_name="", generator_info_name="", generator_info_url="")
                          
    for i, channel in enumerate(live):
        w.addChannel({'display-name': [(channel['title'], u'bg')], 'id': channel['epg_name'], 'url': ['https://test.iptv.bulsat.com']})
        
        if channel.has_key('program'):
            for p in channel['program']:
                if len(p['title']) > 0:
                    w.addProgramme({'start': p['start'], 'stop': p['stop'], 'title': [(p['title'], u'')], 'desc': [(p['desc'], u'')], 'category': [(channel['genre'], u'')], 'channel': channel['epg_name']})    
    
    out = StringIO.StringIO()
    w.write(out, pretty_print=True)
    f_lmx = gzip.open(os.path.join(_files_path, '', 'bulsat.xml.gz'), 'w+', 9)
    f_lmx.write(out.getvalue())
    f_lmx.close()
    out.close()
