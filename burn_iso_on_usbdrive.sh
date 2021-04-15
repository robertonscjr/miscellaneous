lsblk
umount /dev/sdb1
sudo dd bs=4M if=/path/to/debian-10.9.0-amd64-netinst.iso of=/dev/sdb status=progress oflag=sync
