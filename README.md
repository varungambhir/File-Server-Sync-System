# File-Server-Sync-System-
##To install required packagesfor  File-Server-Sync Software, run:
`sudo pip install requirments.txt`

Now, use crontab process of linux to run the software after a particular interval of time (need to do only once).
###Run the following commands on terminal:
`crontab -e`

paste

  **0 * * * * export DISPLAY=:0.0 && python ~/File-Server-Sync-System-/samba.py**  at the end of the file

###Now run:
`sudo visudo -f /etc/sudoers.d/90-cloudimg-ubuntu`

paste

**$(user) ALL=(ALL) NOPASSWD:ALL** in the file


##To launch the software run `python index.py`


    
###Optional:To make a launcher on your dashboard follow the steps on: [Create Launcher Icon on Linux][1]


  [1]: http://askubuntu.com/questions/64222/how-can-i-create-launchers-on-my-desktop