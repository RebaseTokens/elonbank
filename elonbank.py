from PIL import Image
from io import BytesIO
import requests
import sched, time, os
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from datetime import datetime
from time import mktime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from selenium.webdriver.common.by import By
import subprocess

s = sched.scheduler(time.time, time.sleep)
def pumpss(sc):
        
        try:
            print('Screenshot ElonBank Start')
            options = webdriver.FirefoxOptions()
            service = Service(executable_path='/usr/local/bin/geckodriver', log_path=os.devnull)
            driver = webdriver.Firefox(options=options, service=service)
            driver.get('https://alexarrig.godaddysites.com/elonbank')
            driver.maximize_window()
            time.sleep(30)

            element = driver.find_element(By.ID, 'ac33f880-3513-4ae3-a77a-f17c7b1fae33') 
            location = element.location
            size = element.size
            png = driver.get_screenshot_as_png() 
            driver.quit()

            im = Image.open(BytesIO(png)) 

            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']


            im = im.crop((left, top, right, bottom)) 
            im.save('/root/Desktop/elonbank/elonbank.png')

            print('Screenshot ElonBank End')
            s.enter(2, 1, pumppost, (s,))

        except:
            
            s.enter(2, 1, pumppost, (s,))

def pumppost(sc):
        try:
            
            options = webdriver.FirefoxOptions()
            service = Service(executable_path='/usr/local/bin/geckodriver', log_path=os.devnull)
            driver = webdriver.Firefox(options=options, service=service)
            driver.maximize_window()
        
            urlone = "https://charts.bogged.finance/?c=bsc&t=0xD5f363F83b36E10e8a823166b992c0bDc3deDE2C"
            driver.get(urlone)
            time.sleep(50)

            soup = BeautifulSoup(driver.page_source,'html.parser')

            price = soup.find('h4', {'class' : 'dark:text-primary-xtra_light text-gray-800 text-lg lg:text-xl', }).get_text()            
            mcap = soup.find_all('h4', {'class' : 'dark:text-white w-full text-gray-900 text-sm md:text-base 2xl:text-lg', })[2].get_text()           
            volume = soup.find_all('h4', {'class' : 'dark:text-white w-full text-gray-900 text-sm md:text-base 2xl:text-lg', })[0].get_text()           
            liq = soup.find_all('h4', {'class' : 'dark:text-white w-full text-gray-900 text-sm md:text-base 2xl:text-lg', })[1].get_text()            
            holdersone = soup.find('h4', {'class' : 'dark:text-white w-full text-gray-900 text-sm md:text-base 2xl:text-lg group', })            
            holders = holdersone.find('span').get_text()
            apy = "400,977%"
            roi5days = "11.96%"
            nextreward = "0.02368%"
            

            driver.quit()

            others = elonvalue()

            treasury = others[0]
            reserves = others[1]
            tokenburn = others[2]
            valueburn = others[3]
            percentburn = others[4]

            total = {'mcap': mcap, 'volume':volume, 'liquidity':liq, 'holders':holders, 'price':price, 'treasury': treasury, 'reserves': reserves, 'tokenburn':tokenburn, 'valueburn':valueburn, 'percentburn':percentburn}
            print(total)

            with open("/root/Desktop/elonbank.json", "w") as f:
                json.dump(total, f, indent=2)


            keyboard = [
                [
                    InlineKeyboardButton("Poocoin", url='https://poocoin.app/tokens/0xd5f363f83b36e10e8a823166b992c0bdc3dede2c'),
                    InlineKeyboardButton("MC Chart", url='https://alexarrig.godaddysites.com/elonbank')
                ]
            ]
             
            reply_markup = InlineKeyboardMarkup(keyboard)
            

            data = {
                    'photo': ('elonbank.png', open('/root/Desktop/elonbank/elonbank.png', 'rb')),
                    'action': (None, 'send'),
                    'chat_id': (None, '-1001695731586'),
                    'caption': (None, f"\U0001F48E <a href='https://t.me/elonbankbscglobal'>ElonBank/a> Official Group \U0001F48E\n<i>Auto-staking & Auto-compounder BSC Protocol: Earn {apy} APY</i>\n\n \U0001F4B5 <b>Market Cap:</b> {mcap}\n \U0001F4B0	<b>Price:</b> {price}\n \U0001F5D3 <b>24h Volume:</b> {volume}\n \U0001F3E6 <b>Treasury:</b> {treasury}\n \U0001F45C <b>Reserves:</b> {reserves}\n \U0001F512 <b>Liquidity:</b> {liq}\n \U0001F4AC <b>Holders:</b> {holders}\n\n \U0001F525 <b>Burn Pit</b> \U0001F525\n {tokenburn} has been burned, valued {valueburn}, {percentburn} of the Supply! ( <a href='https://bscscan.com/token/0xd5f363f83b36e10e8a823166b992c0bdc3dede2c?a=0x3b7ff88c4898b479c92ef3325131cbca2d5e11ec'>BSCScan.com</a> )\n \n\n\U0001F4C8 <b>Charts:</b> <a href='https://www.dextools.io/app/bsc/pair-explorer/0xe153abd5b5debbfe17c0a50d50c3013ed7cf05fe'>DexTools</a> | <a href='https://charts.bogged.finance/?c=bsc&t=0xD5f363F83b36E10e8a823166b992c0bDc3deDE2C'>Bogged Finance</a>\n\U0001F30E <b>Website:</b> <a href='https://elonbank.io/'>elonbank.io</a>\n\U0001F99C <b>Twitter:</b> <a href='https://twitter.com/ElonBankBSC'>twitter.com/ElonBankBSC</a>\n\U0001F95E<b>Buy from:</b> <a href='https://flooz.trade/wallet/0xd5f363f83b36e10e8a823166b992c0bdc3dede2c?selectedTab=swap'>FloozTrade</a>"),
                    "reply_markup": (None, json.dumps(reply_markup.to_dict())),
                    "parse_mode": (None, 'HTML')
            }

            time.sleep(0.01)    
            requests.post(url='https://api.telegram.org/bot5317695525:AAFMW8CLuyMz4NOWBRdHjfb5yTGTTYI4R8A/sendPhoto', files=data)

            now = datetime.now()
            newDate = mktime(now.timetuple())
            unixTime = newDate * 1000
            mcap = mcap.replace('$','')
            mcap = mcap.replace(',','')
            mcap = int(mcap)

            result = {'timestamp': unixTime, 'value': mcap},
        
            with open("/root/Desktop/elonbank/elonbank.json", "a") as f:
                json.dump(result, f, indent=2)

            subprocess.call(['/root/Desktop/elonbank/cleaner.sh'])

            s.enter(2, 1, pumpss, (sc,))
            
        except Exception as errore:

            print(errore)
            subprocess.call(['/root/Desktop/elonbank/cleaner.sh'])
            s.enter(2, 1, pumpss, (sc,))


def elonvalue():
        
            options = webdriver.FirefoxOptions()
            service = Service(executable_path='/usr/local/bin/geckodriver', log_path=os.devnull)
            driver = webdriver.Firefox(options=options, service=service)
            driver.maximize_window()
        
            urlone = "https://app.elonbank.io/dashboard"
            driver.get(urlone)
            time.sleep(50)

            treasury = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/h6').text
            reserves = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/h6').text
            tokenburn = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/h6').text
            valueburn = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/h6').text
            percentburn = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/div[3]/div/div/div/div[1]/div/h6').text

            driver.quit()

            return treasury, reserves, tokenburn, valueburn, percentburn

        
s.enter(5, 1, pumpss, (s,))
s.run()