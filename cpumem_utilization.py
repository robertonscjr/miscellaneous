import psutil
import time
import json


while(True):
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    time.sleep(1)
    summary = {
        "cpu": cpu,
        "mem": mem
    }
    print(json.dumps(summary))
