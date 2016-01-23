# -*- coding: utf-8 -*-
# Game of Thrones from Tencent video
import sys
import urlparse
import xbmcplugin
import xbmcgui
import resources.vids as episode

plugin_url = sys.argv[0]
handle = int(sys.argv[1])
params = dict(urlparse.parse_qsl(sys.argv[2].lstrip('?')))

__play_url__ = r'http://cache.tv.qq.com/qqplayerout.swf?vid='

def index():
    for idx, vid in enumerate(episode.vids):
        li = xbmcgui.ListItem('第{}集'.format(idx))
        url = plugin_url + '?act=play&vid=' + vid
        xbmcplugin.addDirectoryItem(handle, url, li, True)

    xbmcplugin.endOfDirectory(handle)

def play():
    link = __play_url__ + params['vid']
    play_item = xbmcgui.ListItem(path=link)
    xbmcplugin.setResolvedUrl(handle, True, listitem=play_item)

{
    'index': index,
    'play': play
}[params.get('act', 'index')]()


