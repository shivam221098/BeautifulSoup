from bs4 import BeautifulSoup

content = {}
with open("favorites_9_1_20.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

tags = soup.find_all("dl")
print(tags)
for i in tags:
    print(i.dt.a.text)

