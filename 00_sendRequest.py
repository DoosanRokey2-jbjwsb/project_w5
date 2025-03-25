import requests
import json

url = 'https://requests-homework.onrender.com/submit'
payload = {"name": "권수빈", "student_number": "02039"}
r = requests.post(url, data = json.dumps(payload))

if r.status_code == 200:
    print(r.status_code)
    print(r.text)
else:
    print(r.status_code)
    print(r.text)