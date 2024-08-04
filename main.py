from bs4 import BeautifulSoup
import requests,random,logging,os,function

logging.disable(logging.INFO)
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.info("Start of program")

#get ua
headers=function.return_ua()

contents=input("enter what you want to get:\n")
os.makedirs(f"./image/{contents}",exist_ok=True)

url=f"https://www.google.com/search?q={contents}&sca_esv=5cd6974020d5545b&sca_upv=1&sxsrf=ADLYWIJsh2e8VaCsaMIJbpupHMNhA6RMYw:1722248316546&source=hp&biw=1920&bih=893&ei=fGynZq7QHoDk0PEPj4O1kQQ&iflsig=AL9hbdgAAAAAZqd6jFc-L01bD0hoP4s6brKMkuAXfI5S&oq=&gs_lp=EgNpbWciACoCCAAyBxAjGCcY6gJIzw5QAFgAcAB4AJABAJgBgQWgAYEFqgEDNS0xuAEByAEAigILZ3dzLXdpei1pbWeYAgGgAoUFqAIBmAOFBZIHAzUtMaAH5AE&sclient=img&udm=2"
response=requests.get(url,headers)
logging.info("Get page")
soup=BeautifulSoup(response.text,"html.parser")



robot_image=soup.find_all("img")
logging.info(f"len of img {len(robot_image)}")

function.download_img(robot_image,contents)

print("Download completed!")


logging.info("End of program")
