import requests
from requests.auth import HTTPBasicAuth

URL = "https://suite-endpoint-api-apne2.superb-ai.com/endpoints/f42c3c31-4b05-45df-a4d6-caa3a1968498/inference"
ACCESS_KEY = "vpiu1lDi5T7x2rNqaQiIU9sak1MpCDMV8TixTJZt"

IMAGE_FILE_PATH = "/home/supreme/250108_Gooro/5w/E-3-5 2025-02-10 181824/pico/0.jpg"

image = open(IMAGE_FILE_PATH, "rb").read()

response = requests.post(
    url=URL,
    auth=HTTPBasicAuth("kdt2025_1-33", ACCESS_KEY),
    headers={"Content-Type": "image/jpeg"},
    data=image,
)

print(response.json())