from plyer import notification
import requests 
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\Coronavirus Outbreak Notification\Icon.ico",
        timeout = 3
    )

def getData(url):
    r = requests.get(url)
    return r.text   

if __name__ == "__main__":
    while True:
        # notifyMe("Siddhant", " Let's Stop the spread of the virus together")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[7].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]     
        itemList = myDataStr.split("\n\n")    
        
        states = ['Madhya Pradesh']
        for item in itemList [0:25]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of COVID-19'
                nText = f"State : {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured : {dataList[4]}\nDeaths : {dataList[5]} "
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)

