# -*- coding: utf-8 -*-

import re,urllib,json,urlparse

from resources.lib.libraries import client
from resources.lib import resolvers
from resources.lib.libraries import cleantitle


class source:
    def __init__(self):
        self.base_link = 'http://fmovies.to'
        self.search_link = '/search?keyword=%s'
        self.hash_url = '/ajax/episode/info'
        self.XHR = {'X-Requested-With': 'XMLHttpRequest'}

    def get_movie(self, imdb, title, year):
        try:
            url = '%s %s' % (title, year)
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return

    def get_show(self,imdb,tvdb,tvshowtitle,year):
        try:
            url = tvshowtitle
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return

    def get_episode(self, url, imdb, tvdb, title, date, season, episode):
        try:
            if url == None: return
            url = '"%s S%01dE%02d"&type=series' % (url, int(season), int(episode))
            url = url.replace("Marvel's ", '')
            url = url.replace("DC's ", '')
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')
            return url
        except:
            return

    def get_token(self, data):
        n = 0
        for key in data:
            if not key.startswith('_'):
                for i, c in enumerate(data[key]):
                    n += ord(c) * (i + 1990)
        return {'_token': hex(n)[2:]}

    def get_sources(self, url, hosthdDict, hostDict, locDict):
        try:
            sources = []

            if url == None: return sources

            season = re.compile('.*(S\d+).*').findall(url)[0]
            episode = re.compile('.*(E\d+).*').findall(url)[0]
            url = url.replace(' ' + season + episode, '')

            query = self.base_link + self.search_link % urllib.quote_plus(url)

            result = client.source(query)
            fragment = client.parseDOM(result, 'div', attrs={'class': 'row movie-list'})

            if fragment:
                for item in client.parseDOM(fragment[0], 'div', {'class': 'item'}):
                    links = client.parseDOM(item, 'a', {'class': 'name'}, ret='href')
                    titles = client.parseDOM(item, 'a', {'class': 'name'})
                    is_season = client.parseDOM(item, 'div', {'class': 'status'})

                    for match_url, match_title in zip(links, titles):
                        if is_season:
                            season = season.replace('S1', '').replace('S', '')
                            episode = episode.replace('E', '')

                            clean_match_title = cleantitle.tv(match_title+'&type=series')
                            clean_original = cleantitle.tv(url+season)
                            original_s1 = url + '1'
                            original_s1 = original_s1.replace(' ','')
                            clean_original_s1 = cleantitle.tv(original_s1)

                            if clean_original == clean_match_title or clean_original_s1 == clean_match_title:
                                result = client.source(match_url)
                                episode_fragment = client.parseDOM(result, 'ul', {'class': 'episodes'})

                                if episode_fragment:
                                    episodes = re.compile('data-id="(.+?)" href="(.+?)"\>(\d+?)\<\/a\>').findall(episode_fragment[0])
                                    for hash_id, url, epi in episodes:
                                        if epi == episode:
                                            query = {'id': hash_id, 'update': '0'}
                                            query.update(self.get_token(query))
                                            hash_url = self.base_link + self.hash_url + '?' + urllib.urlencode(query)
                                            headers = self.XHR
                                            headers['Referer'] = url
                                            result = client.source(hash_url, headers=headers)

            js_data = json.loads(result)
            links = {}
            link_type = js_data['type']
            target = js_data['target']
            grabber = js_data['grabber']
            params = js_data['params']

            if link_type == 'iframe' and target:
                links[target] = {'direct': False, 'quality': '720p'}
            elif grabber and params:
                links = self.grab_links(grabber, params, url)

            for link in links:
                direct = links[link]['direct']
                quality = links[link]['quality']
                if direct:
                    host = self.get_direct_hostname(link)
                else:
                    host = urlparse.urlparse(link).hostname

                if quality == '720p':
                    quality = 'HD'
                else:
                    quality = 'SD'

                sources.append({'source': host, 'quality': quality, 'provider': 'FMovies', 'url': link})

            return sources
        except:
            return sources

    def get_direct_hostname(self, link):
        host = urlparse.urlparse(link).hostname
        if host and any([h for h in ['google', 'picasa', 'blogspot'] if h in host]):
            return 'gvideo'
        else:
            return 'fmovies'

    def grab_links(self, grab_url, query, referer):
        try:
            sources = {}
            query['mobile'] = '1'
            query.update(self.get_token(query))
            grab_url = grab_url + '?' + urllib.urlencode(query)
            headers = self.XHR
            headers['Referer'] = referer

            result = client.source(grab_url, headers=headers)

            js_data = json.loads(result)

            if 'data' in js_data:
                for link in js_data['data']:
                    stream_url = link['file']
                    sources[stream_url] = {'direct': True, 'quality': link['label']}
        except:
            pass

        return sources

    def resolve(self, url):
        try:
            url = resolvers.request(url)
            return url
        except:
            return
