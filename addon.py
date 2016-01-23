# -*- coding: utf-8 -*-
# Game of Thrones from Tencent video
import sys
import urlparse
import xbmcplugin
import xbmcgui
import xbmc
import resources.vids as episode

plugin_url = sys.argv[0]
handle = int(sys.argv[1])
params = dict(urlparse.parse_qsl(sys.argv[2].lstrip('?')))

__play_url__ = r'http://cache.tv.qq.com/qqplayerout.swf?vid='

def index():
    for idx, vid in enumerate(episode.vids):
        li = xbmcgui.ListItem('第{}集'.format(idx + 1))
        url = plugin_url + '?act=play&vid=' + vid
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(handle, url, li, False)

    xbmcplugin.endOfDirectory(handle)

def play():
    link = __play_url__ + params['vid']
    play_item = xbmcgui.ListItem(path=link)
    play_item.setInfo(type='Video', infoLabels={'Title':'Play'})
    xbmc.Player().play(link, play_item)
    #xbmcplugin.setResolvedUrl(handle, True, play_item)

{
    'index': index,
    'play': play
}[params.get('act', 'index')]()


