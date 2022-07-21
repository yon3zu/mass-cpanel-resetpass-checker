from multiprocessing.pool import ThreadPool
import requests,colorama
from colorama import init
colorama.init()

red = '\033[91m'
green = '\033[92m'
white = '\033[00m'

# Coded By #No_Identity
# telegram @xxyz4
# github.com/yon3zu

jkt48 = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

# user agent bisa lu ganti sesuka hatilu

def function(url):
    try:
        url = url.replace('\n', '').replace('\r', '')
        if url.startswith('http://'):
            url = url.replace('http://', '')
        elif url.startswith("https://"):
            url = url.replace('https://', '')
        else:
            pass
        op = requests.get('http://' + url + ':2083', headers=jkt48, timeout=15)
        op2 = requests.get('http://' + url + ':2082', headers=jkt48, timeout=15)
        if ("Reset Password") in op.text:
            print green + "[>>] Can Be Reset !! http://" + url + white + '\n'
            open("can_reset.txt", "a").write('http://' + url + ':2083\n')
        elif ("Reset Password") in op.text:
            print green + "[>>] Can Be Reset !! http://" + url + white + '\n'
            open("can_reset.txt", "a").write('http://' + url + ':2082\n')

        else:
            print ''+red+'[xx] Cannot Be Reset >>> http://' + red + url + '\n'
            open("cannot_reset.txt", "a").write('http://' +url+ '\n')

    except:
        pass

banner ="""
\033[36;1m
                                  
   (                        (     
   )\           )         ( )\    
 (((_) `  )  ( /(  (     ))((_|   
 )\___ /(/(  )(_)) )\ ) /((_) )\  
((/ __((_)_\((_)_ _(_/((_))| ((_) 
 | (__| '_ \) _` | ' \)) -_) |_ / 
  \___| .__/\__,_|_||_|\___|_/__| 
      |_|                                                                                                                 
\t
\t [ C0ded by #No_Identity ]
\t List Site Don't Use Http,/,https\033[36;1m
"""
print (banner)
print('\033[92mCpanel Reset Pass Checker\033[91m By #No_Identity\033[91m')
youez = open(raw_input("\033[97mroot@youez:~# list :\033[97m "), 'r').readlines()
ganteng = raw_input("\033[97mroot@youez:~# thread :\033[97m ")
pool = ThreadPool(int(ganteng))
pool.map(function, youez)
pool.close()
pool.join()

if __name__ == '__main__':
    print("\033[97mSuccess Scan !! Check can_reset.txt")
