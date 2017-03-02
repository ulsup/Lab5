import time
from urllib.request import urlopen

class WebPage:
    def __init__(self, url):
        self.__time = time.time()
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content or time.time() - self.__time > 10:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
            self.__time = 0
        return self._content

