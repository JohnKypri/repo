# -*- coding: utf-8 -*-

import re,urllib,urlparse

from resources.lib.libraries import cleantitle
from resources.lib.libraries import client


class source:
    def __init__(self):
        self.base_link = 'http://123movies.to'
        self.search_link = '/movie/search/%s'


    def get_movie(self, imdb, title, year):
        try:
            query = self.search_link % urllib.quote(title)
            query = urlparse.urljoin(self.base_link, query)

            result = client.source(query)

            title = cleantitle.movie(title)
            years = ['%s' % str(year), '%s' % str(int(year)+1), '%s' % str(int(year)-1)]

            result = client.parseDOM(result, 'div', attrs = {'class': 'ml-item'})
            result = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'h2'), re.compile('class *= *[\'|\"]jt-info[\'|\"]>(\d{4})<').findall(i)) for i in result]
            result = [(i[0][0], i[1][0], i[2][0]) for i in result if len(i[0]) > 0 and len(i[1]) > 0 and len(i[2]) > 0]
            result = [i for i in result if any(x in i[2] for x in years)]
            result = [(i[0], re.sub('\d{4}$', '', i[1]).strip()) for i in result]
            result = [i[0] for i in result if title == cleantitle.movie(i[1])][0]

            try: url = re.compile('//.+?(/.+)').findall(result)[0]
            except: url = result
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return


    def get_show(self, imdb, tvdb, tvshowtitle, year):
        try:
            url = '%s (%s)' % (tvshowtitle, year)
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return


    def get_episode(self, url, imdb, tvdb, title, date, season, episode):
        try:
            tvshowtitle, year = re.compile('(.+?) [(](\d{4})[)]$').findall(url)[0]

            query = self.search_link % urllib.quote(tvshowtitle)
            query = urlparse.urljoin(self.base_link, query)

            result = client.source(query)

            tvshowtitle = cleantitle.tv(tvshowtitle)
            season = '%01d' % int(season)
            episode = '%01d' % int(episode)
            years = ['%s' % str(year), '%s' % str(int(year)+1), '%s' % str(int(year)-1)]

            result = client.parseDOM(result, 'div', attrs = {'class': 'ml-item'})
            result = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'h2'), re.compile('class *= *[\'|\"]jt-info[\'|\"]>(\d{4})<').findall(i)) for i in result]
            result = [(i[0][0], i[1][0], i[2][0]) for i in result if len(i[0]) > 0 and len(i[1]) > 0 and len(i[2]) > 0]
            result = [(i[0], re.compile('(.+?) - Season (\d*)$').findall(i[1]), i[2]) for i in result]
            result = [(i[0], i[1][0][0], i[1][0][1], i[2]) for i in result if len(i[1]) > 0]
            result = [i for i in result if tvshowtitle == cleantitle.tv(i[1])]
            result = [i for i in result if season == i[2]]
            result = [(i[0], i[1], str(int(i[3]) - int(i[2]) + 1)) for i in result]
            result = [i[0] for i in result if any(x in i[2] for x in years)][0]

            result += '?S%02dE%02d' % (int(season), int(episode))

            try: url = re.compile('//.+?(/.+)').findall(result)[0]
            except: url = result
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return


    def get_sources(self, url, hosthdDict, hostDict, locDict):
        try:
            sources = []

            if url == None: return sources

            content = re.compile('(.+?)\?S\d*E\d*$').findall(url)

            try: url, season, episode = re.compile('(.+?)\?S(\d*)E(\d*)$').findall(url)[0]
            except: pass

            url = urlparse.urljoin(self.base_link, url)
            url = urlparse.urljoin(url, 'watching.html')

            result = client.source(url)

            try: quality = client.parseDOM(result, 'span', attrs = {'class': 'quality'})[0]
            except: quality = 'HD'

            if '1080p' in quality: quality = '1080p'
            else: quality = 'HD'

            url = re.compile('var\s+url_playlist *= *"(.+?)"').findall(result)[0]

            if len(content) == 0:
                url = '%s/0/0' % url
            else:
                episode = '%01d' % int(episode)
                result = client.parseDOM(result, 'div', attrs = {'class': 'les-content'})
                result = zip(client.parseDOM(result, 'a', ret='onclick'), client.parseDOM(result, 'a'))
                result = [(i[0], re.compile('(\d+)').findall(i[1])) for i in result]
                result = [(i[0], '%01d' % int(i[1][0])) for i in result if len(i[1]) > 0]
                result = [i[0] for i in result if episode == i[1]][0]
                result = re.compile('(\d+)').findall(result)
                url = '%s/%s/%s' % (url, result[0], result[1])


            sources.append({'source': 'Muchmovies', 'quality': quality, 'provider': 'Muchmoviesv2', 'url': url})

            return sources
        except:
            return sources


    def resolve(self, url):
        try:
            idx = int(re.compile('/(\d+)').findall(url)[-1])

            result = client.request(url)

            url = client.parseDOM(result, 'item')[idx]
            url = re.compile("file *= *[\'|\"](.+?)[\'|\"]").findall(url)
            url = [i for i in url if not i.endswith('.srt')][0]
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')

            if 'google' in url:
                url = client.request(url, output='geturl')
                if 'requiressl=yes' in url: url = url.replace('http://', 'https://')
                else: url = url.replace('https://', 'http://')

            else:
                url = '%s|User-Agent=%s' % (url, urllib.quote_plus(client.agent()))

            return url
        except:
            return


