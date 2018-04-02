import requests
r=requests.get('https://dev.periscope.mckinsey-solutions.com/tstapp4/promo/')
print(r.status_code)
print(r.headers)
print(r.cookies)
print(r.text)