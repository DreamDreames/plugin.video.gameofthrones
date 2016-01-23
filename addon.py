# -*- coding: utf-8 -*-
# Game of Thrones from Tencent video
import xbmcaddon
import xmbcgui

with open('vid.txt') as f:
    vids = f.readlines()
    for idx, vid in enumerate(vids):
        print idx, vid.strip('\n')
        print 'done'


