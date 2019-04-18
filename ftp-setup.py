from ftplib import FTP 
import os

ftp = FTP()
ftp.connect('your ftp server', 21)
ftp.login('username','password')
ftp.cwd('/upload') # ftp root
fp = open(localfile, 'rb')
ftp.storbinary('STOR %s' % os.path.basename(localfile), fp, 1024)
fp.close()

