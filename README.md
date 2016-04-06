# File-Server-Sync-System-
> F.S.S.S. overcomes the problem of manually updating the file server
> of any institute/organization. SMB Client module of python
> is used to access a remote Samba Server. This system will sync all the
> directories/files, which the user wants. The user can specify the
> directories which he wants to sync using check box. This system’s
> capability also enables the user to upload his files to his registered
> directory on the remote server. Using crontab process of linux, this
> software runs after a particular interval of time.

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
