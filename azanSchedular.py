from datetime import datetime

import schedule
import time
import requests
import json
import webbrowser

headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
response = requests.get('https://api.aladhan.com/v1/timingsByCity?city=woburn&country=United%20Arab%20Emirates&method=12', headers=headers)

fajar = '00:11'
zuhar = '00:12'
asar = '00:13'
magrib = '00:14'
isha = '00:15'

# this job runs once a day for latest time of azan
def getAzanApi():
    print("----getAzanApi-----",)

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)
    print('Azan Time Api Scheduled NOW !')
    if response.status_code == 200:
        print('Success!')

        json_data = json.loads(response.text)
        # print(json_data)
        fileData = json_data["data"]['timings']
        print(json_data["data"]['timings'])

        # writing data of azan in a file
        with open('azanData.txt', 'w') as outfile:
            json.dump(fileData, outfile)
            fajar = json_data["data"]['timings']['Fajr']
            zuhar = json_data["data"]['timings']['Dhuhr']
            asar = json_data["data"]['timings']['Asr']
            magrib = json_data["data"]['timings']['Maghrib']
            isha = json_data["data"]['timings']['Isha']
            print("Fajar %s Zuhar %s Asar %s Maghrib %s Isha %s" % (fajar, zuhar, asar, magrib, isha))
            # working
            # webbrowser.open("azan.mp3")
    elif response.status_code == 404:
        print('Not Found.')
    print("------------", )

    # play azan for fajar
    schedule.every().day.at(str(fajar)).do(playAzan)

    # play azan for zuhar
    schedule.every().day.at(str(zuhar)).do(playAzan)

    # play azan for asar
    schedule.every().day.at(str(asar)).do(playAzan)

    # play azan for maghrib
    schedule.every().day.at(str(magrib)).do(playAzan)

    # play azan for isha
    schedule.every().day.at(str(isha)).do(playAzan)


def playAzan():
    print("playAzan")
    # working
    webbrowser.open("azan.mp3")

def job3():
    print("Hello")


# this job runs once a day for latest time of azan
schedule.every().day.at("00:00").do(getAzanApi)
#
#
# # play azan for fajar
# schedule.every().day.at(str(fajar)).do(playAzan)
#
# # play azan for zuhar
# schedule.every().day.at(str(zuhar)).do(playAzan)
#
# # play azan for asar
# schedule.every().day.at(str(asar)).do(playAzan)
#
# # play azan for maghrib
# schedule.every().day.at(str(magrib)).do(playAzan)
#
# # play azan for isha
# schedule.every().day.at(str(isha)).do(playAzan)


# schedule.every().hour.do(job)
# schedule.every().day.at("12:25").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().thursday.at("19:15").do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# schedule.every(2).seconds.do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)