import time
from time import sleep
import os
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

counter = 10
url = os.getenv("PUSHGATEWAY_HOST")
if url == "":
  url = "127.0.0.1:9191"

registry = CollectorRegistry()
g = Gauge("python", 'metric description here', registry=registry)


def submit(name, url, registry, counter):
  g.set(counter)
  push_to_gateway(url, job=name, registry=registry)

while True:
  counter+=1
  submit("job_" + os.getenv("HOSTNAME", "localhost"), url, registry, counter)
  print(counter)
  time.sleep(10)
