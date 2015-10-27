# -*- coding: utf-8 -*-

'''
    DooFree Add-on
    Copyright (C) 2015 Mpie
'''

import os, sys, urlparse, json, urllib2

from resources.lib.libraries import control
from resources.lib.libraries import views

artPath = control.artPath()

addonFanart = control.addonFanart()

try: action = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))['action']
except: action = None

traktMode = False if control.setting('trakt_user') == '' else True

imdbMode = False if control.setting('imdb_user') == '' else True

sysaddon = sys.argv[0]


class navigator:

    def parseJson(self, url):
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        f = opener.open(req)
        data = json.loads(f.read())
        return data

    def root(self):
        views.setView('seasons', {'skin.confluence': 500})
        self.addDirectoryItem('Thai Live TV', 'thaiLiveTV', 'root_livetv.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('Thai Shows', 'thaiShows', 'root_thai.jpg', 'DefaultMovies.png')
        self.addDirectoryItem('Working on DooFree 3.0 to make things faster', '', '', 'DefaultMovies.png')
        '''
        self.addDirectoryItem(30001, 'movieNavigator', 'movies.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30002, 'tvNavigator', 'tvshows.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30003, 'channels', 'channels.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30004, 'myNavigator', 'mygenesis.jpg', 'DefaultVideoPlaylists.png')

        if not control.setting('movie_widget') == '0':
            self.addDirectoryItem(30005, 'movieWidget', 'moviesAdded.jpg', 'DefaultRecentlyAddedMovies.png')

        if (traktMode == True and not control.setting('tv_alt_widget') == '0') or (traktMode == False and not control.setting('tv_widget') == '0'):
            self.addDirectoryItem(30006, 'tvWidget', 'calendarsAdded.jpg', 'DefaultRecentlyAddedEpisodes.png')

        if not control.setting('calendar_widget') == '0':
            self.addDirectoryItem(30007, 'calendars', 'calendar.jpg', 'DefaultRecentlyAddedEpisodes.png')

        self.addDirectoryItem(30008, 'toolNavigator', 'tools.jpg', 'DefaultAddonProgram.png')

        self.addDirectoryItem(30009, 'searchNavigator', 'search.jpg', 'DefaultFolder.png')
        '''

        self.endDirectory()

    def thaiLiveTV(self):
        # live4 is asia, uk99 is uk
        self.addDirectoryItem('3', 'playThaiLiveTV&url=rtmp://uk99.seesantv.com/as99/ch3hd&name=3HD&image=ch3hd.png', 'ch3hd.png', 'DefaultMovies.png', isFolder=False)
        self.addDirectoryItem('5', 'playThaiLiveTV&url=rtmp://uk99.seesantv.com/as99/ch5hd&name=5HD&image=ch5hd.png', 'ch5hd.png', 'DefaultMovies.png', isFolder=False)
        self.addDirectoryItem('7', 'playThaiLiveTV&url=rtmp://uk99.seesantv.com/as99/ch7hd&name=7HD&image=ch7hd.png', 'ch7hd.png', 'DefaultMovies.png', isFolder=False)
        self.addDirectoryItem('8', 'playThaiLiveTV&url=rtmp://uk99.seesantv.com/as99/cheight1&name=8HD&image=ch8hd.png', 'ch8hd.png', 'DefaultMovies.png', isFolder=False)
        self.addDirectoryItem('MCOT', 'playThaiLiveTV&url=rtmp://uk99.seesantv.com/as99/chmcothd&name=MCOT_HD&image=ch9hd.png', 'ch9hd.png', 'DefaultMovies.png', isFolder=False)
        self.addDirectoryItem('ONE', 'playThaiLiveTV&url=rtmp://uk99.seesantv.com/as99/chonehd&name=ONE_HD&image=ch1hd.jpg', 'ch1hd.jpg', 'DefaultMovies.png', isFolder=False)
        self.addDirectoryItem('PPTV', 'playThaiLiveTV&url=rtmp://uk99.seesantv.com/as99/chpptv1&name=PPTV_HD&image=chpptvhd.png', 'chpptvhd.png', 'DefaultMovies.png', isFolder=False)
        self.addDirectoryItem('NOW26', 'playThaiLiveTV&url=rtmp://uk99.seesantv.com/as99/chnow261&name=PPTV_HD&image=chnow26hd.jpg', 'chnow26hd.jpg', 'DefaultMovies.png', isFolder=False)
        self.endDirectory()

    def thaiShows(self):
        self.addDirectoryItem('ละครไทย (ออนแอร์) / Thai Dramas (on air)', 'listShows&catid=18', '', 'DefaultMovies.png')
        self.addDirectoryItem('ละครไทย (อวสาน) / Thai Dramas (ended)', 'listShows&catid=27', '', 'DefaultMovies.png')
        self.addDirectoryItem('ซีรี่ย์เกาหลี / Korean Series', 'listShows&catid=17', '', 'DefaultMovies.png')
        self.addDirectoryItem('หนังจีนชุด / Chinese Series', 'listShows&catid=37', '', 'DefaultMovies.png')
        self.addDirectoryItem('รายการอาหาร / Cooking Shows', 'listShows&catid=15', '', 'DefaultMovies.png')
        self.addDirectoryItem('วาไรตี้โชว์ / Variety Shows', 'listShows&catid=8', '', 'DefaultMovies.png')
        self.addDirectoryItem('เรียลลิตี้โชว์ / Reality & Singing Contest', 'listShows&catid=84', '', 'DefaultMovies.png')
        self.addDirectoryItem('ข่าว / Thai News', 'listShows&catid=4', '', 'DefaultMovies.png')
        self.addDirectoryItem('ข่าวบันเทิง / Thai Entertainment News', 'listShows&catid=14', '', 'DefaultMovies.png')
        self.addDirectoryItem('ภาพยนตร์ไทย / Thai Movies', 'listShows&catid=92', '', 'DefaultMovies.png')
        self.addDirectoryItem('ภาพยนตร์ฝรั่งใหม่ / US Movies (Thai dubbed)', 'listShows&catid=98', '', 'DefaultMovies.png')
        self.addDirectoryItem('ซีรี่ย์ฝรั่ง / US Series (Thai dubbed)', 'listShows&catid=38', '', 'DefaultMovies.png')
        self.addDirectoryItem('ภาพยนตร์แอนนิเมชั่น / Animation', 'listShows&catid=93', '', 'DefaultMovies.png')
        self.endDirectory()

    def movies(self):
        self.addDirectoryItem(30021, 'movieGenres', 'movieGenres.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30022, 'movieYears', 'movieYears.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30023, 'moviePersons', 'movies.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30024, 'movieCertificates', 'movieCertificates.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30025, 'movies&url=featured', 'movies.jpg', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(30026, 'movies&url=trending', 'moviesTrending.jpg', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(30027, 'movies&url=popular', 'moviesPopular.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30028, 'movies&url=views', 'moviesViews.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30029, 'movies&url=boxoffice', 'moviesBoxoffice.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30030, 'movies&url=oscars', 'moviesOscars.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30031, 'movies&url=theaters', 'moviesTheaters.jpg', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(30032, 'movies&url=added', 'moviesAdded.jpg', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem(30033, 'movieFavourites', 'movieFavourites.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30034, 'moviePerson', 'moviePerson.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30035, 'movieSearch', 'movieSearch.jpg', 'DefaultMovies.png')

        self.endDirectory()


    def tvshows(self):
        self.addDirectoryItem(30051, 'tvGenres', 'tvGenres.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30052, 'tvYears', 'tvshows.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30053, 'tvNetworks', 'tvshows.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30054, 'tvshows&url=trending', 'tvshowsTrending.jpg', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(30055, 'tvshows&url=popular', 'tvshowsPopular.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30056, 'tvshows&url=airing', 'tvshows.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30057, 'tvshows&url=active', 'tvshowsActive.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30058, 'tvshows&url=premiere', 'tvshows.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30059, 'tvshows&url=rating', 'tvshowsRating.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30060, 'tvshows&url=views', 'tvshowsViews.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30061, 'calendars', 'calendar.jpg', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(30062, 'calendar&url=added', 'calendarsAdded.jpg', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(30063, 'episodeFavourites', 'tvFavourites.jpg', 'DefaultRecentlyAddedEpisodes.png')
        self.addDirectoryItem(30064, 'tvFavourites', 'tvFavourites.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30065, 'tvPerson', 'tvPerson.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30066, 'tvSearch', 'tvSearch.jpg', 'DefaultTVShows.png')

        self.endDirectory()


    def genesis(self):
        if traktMode == True:
            self.addDirectoryItem(30081, 'movies&url=traktcollection', 'moviesTraktcollection.jpg', 'DefaultMovies.png', context=(30191, 'moviesToLibrary&url=traktcollection'))
            self.addDirectoryItem(30082, 'movies&url=traktwatchlist', 'moviesTraktwatchlist.jpg', 'DefaultMovies.png', context=(30191, 'moviesToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(30083, 'movies&url=traktfeatured', 'movies.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(30084, 'movies&url=traktratings', 'movies.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(30085, 'tvshows&url=traktcollection', 'tvshowsTraktcollection.jpg', 'DefaultTVShows.png', context=(30191, 'tvshowsToLibrary&url=traktcollection'))
            self.addDirectoryItem(30086, 'tvshows&url=traktwatchlist', 'tvshowsTraktwatchlist.jpg', 'DefaultTVShows.png', context=(30191, 'tvshowsToLibrary&url=traktwatchlist'))
            self.addDirectoryItem(30087, 'tvshows&url=traktfeatured', 'tvshows.jpg', 'DefaultTVShows.png')
            self.addDirectoryItem(30088, 'tvshows&url=traktratings', 'tvshows.jpg', 'DefaultTVShows.png')
            self.addDirectoryItem(30089, 'calendar&url=progress', 'calendarsProgress.jpg', 'DefaultRecentlyAddedEpisodes.png')
            self.addDirectoryItem(30090, 'calendar&url=mycalendar', 'calendarsMycalendar.jpg', 'DefaultRecentlyAddedEpisodes.png')

        if imdbMode == True:
            self.addDirectoryItem(30091, 'movies&url=imdbwatchlist', 'moviesImdbwatchlist.jpg', 'DefaultMovies.png', context=(30191, 'moviesToLibrary&url=imdbwatchlist'))
            self.addDirectoryItem(30092, 'tvshows&url=imdbwatchlist', 'tvshowsImdbwatchlist.jpg', 'DefaultTVShows.png', context=(30191, 'tvshowsToLibrary&url=imdbwatchlist'))

        if traktMode == True or imdbMode == True:
            self.addDirectoryItem(30093, 'movieUserlists', 'movieUserlists.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(30094, 'tvUserlists', 'tvUserlists.jpg', 'DefaultTVShows.png')

        self.addDirectoryItem(30095, 'movieFavourites', 'movieFavourites.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30096, 'episodeFavourites', 'tvFavourites.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30097, 'tvFavourites', 'tvFavourites.jpg', 'DefaultTVShows.png')

        self.endDirectory()


    def tools(self):
        self.addDirectoryItem(30111, 'openSettings&query=0.0', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30112, 'openSettings&query=6.1', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30113, 'openSettings&query=1.0', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30114, 'openSettings&query=8.0', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30115, 'openSettings&query=2.0', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30116, 'openSettings&query=3.0', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30117, 'openSettings&query=4.0', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30118, 'openSettings&query=5.0', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30119, 'clearSources', 'cache.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30120, 'clearCache', 'cache.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30121, 'libtoolNavigator', 'tools.jpg', 'DefaultAddonProgram.png')

        self.endDirectory()


    def library(self):
        self.addDirectoryItem(30131, 'openSettings&query=7.0', 'settings.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30132, 'updateLibrary&query=tool', 'update.jpg', 'DefaultAddonProgram.png')
        self.addDirectoryItem(30133, control.setting('movie_library'), 'movies.jpg', 'DefaultMovies.png', isAction=False)
        self.addDirectoryItem(30134, control.setting('tv_library'), 'tvshows.jpg', 'DefaultTVShows.png', isAction=False)

        if traktMode == True:
            self.addDirectoryItem(30135, 'moviesToLibrary&url=traktcollection&query=tool', 'moviesTraktcollection.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(30136, 'moviesToLibrary&url=traktwatchlist&query=tool', 'moviesTraktwatchlist.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(30137, 'tvshowsToLibrary&url=traktcollection&query=tool', 'tvshowsTraktcollection.jpg', 'DefaultTVShows.png')
            self.addDirectoryItem(30138, 'tvshowsToLibrary&url=traktwatchlist&query=tool', 'tvshowsTraktwatchlist.jpg', 'DefaultTVShows.png')

        if imdbMode == True:
            self.addDirectoryItem(30139, 'moviesToLibrary&url=imdbwatchlist&query=tool', 'moviesImdbwatchlist.jpg', 'DefaultMovies.png')
            self.addDirectoryItem(30140, 'tvshowsToLibrary&url=imdbwatchlist&query=tool', 'tvshowsImdbwatchlist.jpg', 'DefaultTVShows.png')

        self.endDirectory()


    def search(self):
        self.addDirectoryItem(30151, 'movieSearch', 'movieSearch.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30152, 'tvSearch', 'tvSearch.jpg', 'DefaultTVShows.png')
        self.addDirectoryItem(30153, 'moviePerson', 'moviePerson.jpg', 'DefaultMovies.png')
        self.addDirectoryItem(30154, 'tvPerson', 'tvPerson.jpg', 'DefaultTVShows.png')

        self.endDirectory()


    def addDirectoryItem(self, name, query, thumb, icon, context=None, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if not context == None: cm.append((control.lang(context[0]).encode('utf-8'), 'RunPlugin(%s?action=%s)' % (sysaddon, context[1])))
        item = control.item(label=name, iconImage=thumb, thumbnailImage=thumb)
        item.addContextMenuItems(cm, replaceItems=False)
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self, cacheToDisc=True):
        control.directory(int(sys.argv[1]), cacheToDisc=cacheToDisc)


