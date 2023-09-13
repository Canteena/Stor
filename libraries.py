''' Python3 installer libraries Build by TeaM ExEc '''
import os
from time import sleep,time

A = "\033[1;91m"
H = "\033[1;93m"
E = "\033[1;92m"

Banner = f'''{H}
 ███████╗ ██╗  ██╗ ███████╗  ██████╗
 ██╔════╝ ╚██╗██╔╝ ██╔════╝ ██╔════╝
 █████╗    ╚███╔╝  █████╗   ██║
 ██╔══╝    ██╔██╗  ██╔══╝   ██║
 ███████╗ ██╔╝ ██╗ ███████╗ ╚██████╗
 ╚══════╝ ╚═╝  ╚═╝ ╚══════╝  ╚═════╝
     Tool build by TeaM ExEc 
     '''
print(Banner)

Libraries_List = [
'--upgrade pip','requests','Flask','bs4','colorama','instaloader',
'lxml','mechanize','names','playwright','PyExecJS','pyfiglet','python',
'python-cfonts','pytz','pytube','pywifi','telebot','user-agent'
] # TeaM ExEc

liblen = len(Libraries_List)
sleep(0.8)
start = time()
c = 1
for Library in Libraries_List:
    print(f'{A}[{H}{c}/{liblen}{A}] {H}installing "{Library}" Start:')
    result = os.popen(f'pip3 install {Library}').read()
    print(f'{E}installing "{Library}" Done:')
    c += 1

pt = str(time() - start)
print(f'{A}installing {liblen} Libraries finish in {pt[0]}{pt[1]}{pt[2]}{pt[3]}s')
