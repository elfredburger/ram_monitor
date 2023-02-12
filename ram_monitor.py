import psutil
import requests
from tqdm import tqdm
from time import sleep
api_url=''
with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
    while True:
        rambar.n=psutil.virtual_memory().percent
        cpubar.n=psutil.cpu_percent()
        if psutil.virtual_memory().percent>50:
            print(requests.get(api_url))

        rambar.refresh()
        cpubar.refresh()
        sleep(5)
