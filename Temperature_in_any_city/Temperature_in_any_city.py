# SCRAPE WEATHER DATA FROM GOOGLE
import requests
from requests_html import HTMLSession

# ASK USER FOR CITY
x = input("Vilken stad vill du veta vädret i? ")

s = HTMLSession()
query = x
# Turn url into an f-string to allow query to be part of the url
url = f"https://www.google.com/search?q=weather+{query}"

# Build request
r = s.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"})
temp = r.html.find("span#wob_tm", first=True).text
unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
desc = r.html.find("div.VQF4g", first=True).find("span#wob_dc", first=True).text

print("Vädret i", query, "är: ", temp, unit, desc)



