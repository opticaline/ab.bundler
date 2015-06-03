import json
import urllib
from urllib.request import Request

__author__ = 'opticaline'


class Ajax:
    opener = None

    def __init__(self, use_proxy=True):
        if use_proxy:
            proxyhand = urllib.request.ProxyHandler({"http": "http://zhang-xu-neu:Bronze3!@192.168.107.27:8080"})
            self.opener = urllib.request.build_opener(proxyhand)
        else:
            self.opener = urllib.request.build_opener()

    def get(self, url):
        return self.opener.open(url).readall().decode()


class Search:
    source = []
    ajax = None

    def __init__(self, source):
        self.source = source
        self.ajax = Ajax()

    def search(self, t, keyword):
        pass

    def get(self, url):
        return self.ajax.get(url)


class AcFunSearch(Search):
    def search(self, t, keyword):
        result = []
        if keyword:
            pass
        else:
            for url in self.source[t]:
                result += json.loads(self.get(url))
        return result


class BiliBiliSearch(Search):
    pass
