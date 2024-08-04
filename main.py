from bs4 import BeautifulSoup
import requests,time,random,logging,os

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.info("Start of program")

# def choose_ua():
ua_list=[
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/25.0 Chrome/121.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Unique/100.7.6266.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0."
]
headers={"User-Agent":{random.choice(ua_list)}}

contents=input("enter what you want to get:\n")
os.makedirs(f"./image/{contents}")

url=f"https://www.google.com/search?q={contents}&sca_esv=5cd6974020d5545b&sca_upv=1&sxsrf=ADLYWIJsh2e8VaCsaMIJbpupHMNhA6RMYw:1722248316546&source=hp&biw=1920&bih=893&ei=fGynZq7QHoDk0PEPj4O1kQQ&iflsig=AL9hbdgAAAAAZqd6jFc-L01bD0hoP4s6brKMkuAXfI5S&oq=&gs_lp=EgNpbWciACoCCAAyBxAjGCcY6gJIzw5QAFgAcAB4AJABAJgBgQWgAYEFqgEDNS0xuAEByAEAigILZ3dzLXdpei1pbWeYAgGgAoUFqAIBmAOFBZIHAzUtMaAH5AE&sclient=img&udm=2"
response=requests.get(url,headers)
logging.info("Get page")
soup=BeautifulSoup(response.text,"html.parser")



robot_image=soup.find_all("img")
logging.info(f"len of img {len(robot_image)}")
num=0
for img in robot_image:
    src=img['src']
    
    if(f"{''.join(  [src[0],src[1],src[2],src[3] ] )}"=="http"):
        logging.info(src)
        img=requests.get(src).content
        with open(f"./image/{contents}/{num}.png","wb") as out_file:
                out_file.write(img)
        num+=1

    if num>100:
         break


logging.info("End of program")
