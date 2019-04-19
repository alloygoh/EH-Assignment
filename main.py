#!/usr/bin/env python3

# imports
import inotify.adapters
from multiprocessing import Process, Manager
from ftplib import FTP
import os

def listener(folder):
    i = inotify.adapters.InotifyTree(folder)
    for event in i.event_gen(yield_nones = False):
        (_,status,path,filename) = event
        if "IN_CREATE" in status:
            final_path = path+'/'+filename
            p = Process(target=send_file,args=(final_path,))
            p.start()
def send_file(path):
    ftp = FTP()
    ftp.connect('127.0.0.1', 2121)
    ftp.login('anonymous','password')
    #ftp.cwd('/sambashare') # ftp root
    fp = open(path, 'rb')
    ftp.storbinary('STOR %s' % os.path.basename(path), fp, 1024)
    fp.close()
def main():
    p = Process(target=listener,args=("/root/Desktop",))
    p.start()


'''
control_devices.append(device.partition)
p = Process(target=listener,args=(device.mountpoint,device.partition,control_devices,))
p.start()
'''
if __name__ == "__main__":
    main()
