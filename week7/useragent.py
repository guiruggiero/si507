import requests
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = {'User-agent': ua.chrome} # or ua.firefox or ua.random...
html = requests.get("https://www.michigandaily.com", headers=user_agent).text