
## Running the FTP Server

Run the ftp server using `python -m pyftpdlib -w`

### persist the script for reboot

`sudo cp -i /path/to/your_script.py /bin`

`sudo crontab -e`

Scroll to the bottom and add the following line (after all the #'s):

`@reboot python3 /bin/your_script.py &`
