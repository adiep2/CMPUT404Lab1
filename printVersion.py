import requests as rq

print(rq.__version__)
print(rq.get('http://google.com/').text)
print(rq.get('https://raw.githubusercontent.com/adiep2/CMPUT404Lab1/main/printVersion.py').text)