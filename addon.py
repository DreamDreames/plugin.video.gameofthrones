# -*- coding: utf-8 -*-
# Game of Thrones from Tencent video
import xbmcaddon
import xmbcgui


#with open('vid.txt') as f:
    #vids = f.readlines()
    #for idx, vid in enumerate(vids):
        #print idx, vid.strip('\n')
        #print 'done'
addon = xmbcaddon.Addon()
addonname = addon.getAddonInfo('name')

line1 = "plugin of"
line2 = "Game of Thrones"
line3 = "from tencent video"

xmbcgui.Dialog().ok(addonname, line1, line2, line3)


