from gtts import gTTS
from playsound import playsound
from bs4 import BeautifulSoup
import os
import requests

url = 'https://www.cnn.com/2022/01/13/opinions/bidens-approval-rating-history-zelizer/index.html'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page)

j = 0
for i in soup.find_all(class_ = "pg-rail-tall__body"):
    mytext = i.get_text()
    if len(mytext) == 0:
        continue
    print(mytext)
    j = j + 1
    sound = gTTS(mytext, lang_check = False)
    sound.save("welcome" +str(j)+".mp3")
    playsound("welcome" +str(j)+".mp3")

for i in range (1, j+1):
    os.remove("welcome" +str(i)+".mp3")

