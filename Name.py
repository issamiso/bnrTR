import os
import time
os.system('clear')
R  = '\33[1;31m'
G  = '\33[1;32m'
O  = '\33[1;33m'
B  = '\33[1;34m'
P  = '\33[1;35m'
def Name():
    Name=input(G+'Enter Your Name :')
    os.system(f"sed -i 's/#####/{Name}/g' bash.bashrc")
    os.system('cd /data/data/com.termux/files/usr/etc;rm -rif bash.bashrc')
    print(R+'Loding ...')
    time.sleep(1)
    os.system('cd /data/data/com.termux/files/home/bnrTR')
    os.system('cp bash.bashrc /data/data/com.termux/files/usr/etc')
    os.system('cd /data/data/com.termux/files/home/bnrTR')
    os.system('cp colors.properties /data/data/com.termux/files/home/.termux')
    os.system('cd /data/data/com.termux/files/home/bnrTR')
    os.system(f"sed -i 's/####/{Name}/g' .bnr.py")
    os.system('cp .bnr.py /data/data/com.termux/files/home')
    print(O+'Restart Termux ✓')
    
Name()
