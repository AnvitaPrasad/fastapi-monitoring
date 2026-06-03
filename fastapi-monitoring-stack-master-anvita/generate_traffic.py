import requests, time
for i in range(1000):
    r = requests.get("http://localhost:8000/hello")
    time.sleep(0.2)
