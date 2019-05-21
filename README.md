# EH Assignment

This repo contains the code and guide on how to replicate the attack for my school's assignment on Ethical Hacking.

## Running the FTP Server

Run the ftp server using `python -m pyftpdlib -w`

### persist the script for reboot

`sudo cp -i /path/to/your_script.py /bin`

`sudo crontab -e`

Scroll to the bottom and add the following line (after all the #'s):

`@reboot python /bin/your_script.py &`
