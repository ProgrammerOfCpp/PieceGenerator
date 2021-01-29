import time
from threading import Thread
import requests


class ServerPinger (Thread):
    def __init__(self, url, delay_sec):
        super().__init__()
        self.url = url
        self.delay_sec = delay_sec

    def run(self):
        while True:
            try:
                requests.get(self.url)
                time.sleep(self.delay_sec)
            except Exception as e:
                print(e)


ServerPinger(
    url='https://piecegenerator.herokuapp.com/ping',
    delay_sec=10
).start()
