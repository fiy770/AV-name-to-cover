
import requests
import os
from tkinter import *
from bs4 import BeautifulSoup
import urllib

'''def getcover(files,files2):
    if __name__ == '__main__':
        print("main")
    else:
        f_error = open("c:\error\error.txt","a")
        cs_url ='http://www.javlibrary.com/tw/vl_searchbyid.php'
        for file in files:
            if file !="" :
                fname=os.path.splitext(file)[0]
                param ={'keyword':fname}
                r = requests.get(cs_url, params = param)
                bs = BeautifulSoup(r.text,"html.parser")
                link=bs.find(id="video_jacket_img")
                if link != None :
                    url=link.get('src')
                    pngweb = urllib.request.urlopen(url)
                    pngin = pngweb.read()
                    with open(fname+".jpg","wb") as code:
                       code.write(pngin)
                else :
                    print(fname)
                    f_error.writelines(fname+"\n")
            else :
                break
        f_error.close()
    return
'''
def main():
    inputpath = input("inputpath:")
    outputpath = input("outputpath:")
    files1 = os.listdir(inputpath)
    files2 = os.listdir(outputpath) 
    #getcover(files1,files2)
    return
'''
cur_path = os.getcwd() #得知目前路徑
 
'''
#mainTK = Tk()



