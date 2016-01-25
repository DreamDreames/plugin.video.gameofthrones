# -*- coding: utf-8 -*-
# Game of Thrones from Tencent video
import sys
import urlparse
import xbmcplugin
import xbmcgui
import xbmc
import resources.vids as episode
import urllib2
import json
import gzip
from StringIO import StringIO
from backport_collections import OrderedDict

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
    #link = __play_url__ + params['vid']
    vid = params['vid']
    link = qqvideo(vid)
    play_item = xbmcgui.ListItem(path=link)
    play_item.setInfo(type='Video', infoLabels={'Title':'Play'})
    xbmc.Player().play(link, play_item)
    #xbmcplugin.setResolvedUrl(handle, True, play_item)

def _http(url):
    """
    open url
    """
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) {0}{1}'.
                   format('AppleWebKit/537.36 (KHTML, like Gecko) ',
                          'Chrome/28.0.1500.71 Safari/537.36'))
    req.add_header('Accept-encoding', 'gzip')
    rsp = urllib2.urlopen(req, timeout=30)
    if rsp.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(rsp.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
    else:
        data = rsp.read()
    rsp.close()
    return data

def qqvideo(vid):
    #html = _http(self.url)
    #vid = re.compile(r'vid:"([^"]+)"').search(html).group(1)
    vid = 'c001640aimv'
    murl = 'http://vv.video.qq.com/'
    #vinfo = _http('%sgetvinfo?otype=json&vids=%s&platform=70202&utype=-1&appver=3.2.19.325'% (murl, vid) + '&ehost=http%3a%2f%2fcache.tv.qq.com%2fqqplayerout.swf%3fvid%3dc001640aimv' )
    vinfo = _http('%sgetinfo?otype=json&vids=%s&defaultfmt=fhd'% (murl, vid))
    infoj = json.loads(vinfo.split('=')[1][:-1])
    qtyps = OrderedDict((
        ('1080P', 'fhd'), ('超清', 'shd'), ('高清', 'hd'), ('标清', 'sd')))
    vtyps = {v['name']:v['id'] for v in infoj['fl']['fi']}
    qtypid = vtyps['sd']
    sels = [k for k,v in qtyps.iteritems() if v in vtyps]
    #sel = dialog.select('清晰度', sels)
    sel = 0
    surls = []
    urlpre = infoj['vl']['vi'][0]['ul']['ui'][-1]['url']
    if sel is not -1:
        qtypid = vtyps[qtyps[sels[sel]]]
    for i in range(1, int(infoj['vl']['vi'][0]['cl']['fc'])):
        fn = '%s.p%s.%s.mp4' % (vid, qtypid%10000, str(i))
        sinfo = _http(
                '{0}getkey?format={1}&filename={2}&vid={3}&otype=json'.format(
                        murl, qtypid, fn, vid))
        skey = json.loads(sinfo.split('=')[1][:-1])['key']
        surl = urllib2.urlopen(
                '%s%s?vkey=%s' % (urlpre, fn, skey), timeout=30).geturl()
        if not surl: break
        surls.append(surl)
        movurl = 'stack://{0}'.format(' , '.join(surls))
        return movurl

{
    'index': index,
    'play': play
}[params.get('act', 'index')]()


