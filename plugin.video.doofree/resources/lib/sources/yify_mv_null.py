# -*- coding: utf-8 -*-

import re,urllib,urlparse,json

from resources.lib.libraries import cleantitle
from resources.lib.libraries import client


class source:
    def __init__(self):
        self.base_link = 'http://yify.tv'
        self.search_link = '/wp-admin/admin-ajax.php'
        self.pk_link = '/player/pk/pk/plugins/player_p2.php'


    def get_movie(self, imdb, title, year):
        try:
            query = urlparse.urljoin(self.base_link, self.search_link)
            post = urllib.urlencode({'action': 'ajaxy_sf', 'sf_value': title})

            result = client.source(query, post=post)
            result = result.replace('&#8211;','-').replace('&#8217;','\'')
            result = json.loads(result)
            result = result['post']['all']

            title = cleantitle.movie(title)
            result = [i['post_link'] for i in result if title == cleantitle.movie(i['post_title'])][0]

            check = client.source(result)
            if not str(imdb) in check: raise Exception()

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

            base = urlparse.urljoin(self.base_link, url)

            result = client.source(base)
            result = client.parseDOM(result, 'script', attrs = {'type': 'text/javascript'})
            result = ''.join(result)

            links = re.compile('pic=([^&]+)').findall(result)
            links = [x for y,x in enumerate(links) if x not in links[:y]]

            for i in links:
                try:
                    url = urlparse.urljoin(self.base_link, self.pk_link)
                    post = urllib.urlencode({'url': i, 'fv': '16'})
                    result = client.source(url, post=post)
                    result = json.loads(result)

                    try: sources.append({'source': 'GVideo', 'quality': '1080p', 'provider': 'YIFY', 'url': [i['url'] for i in result if i['width'] == 1920 and 'google' in i['url']][0]})
                    except: pass
                    try: sources.append({'source': 'GVideo', 'quality': 'HD', 'provider': 'YIFY', 'url': [i['url'] for i in result if i['width'] == 1280 and 'google' in i['url']][0]})
                    except: pass

                    try: sources.append({'source': 'YIFY', 'quality': '1080p', 'provider': 'YIFY', 'url': [i['url'] for i in result if i['width'] == 1920 and not 'google' in i['url']][0]})
                    except: pass
                    try: sources.append({'source': 'YIFY', 'quality': 'HD', 'provider': 'YIFY', 'url': [i['url'] for i in result if i['width'] == 1280 and not 'google' in i['url']][0]})
                    except: pass
                except:
                    pass

            return sources
        except:
            return sources


    def resolve(self, url):
        try:
            if url.startswith('stack://'): return url

            url = client.request(url, output='geturl')
            if 'requiressl=yes' in url: url = url.replace('http://', 'https://')
            else: url = url.replace('https://', 'http://')
            return url
        except:
            return

