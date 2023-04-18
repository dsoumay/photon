---
title:  Commands for Operations
weight: 4
---

You can perform various operations in the A/B partition system using the following commands:

- `abupdate mount/unmount`: Use this command to mount or unmount the partition set that you want to update or modify. The partition set is mounted as a tree at the following location: `/mnt/abupdate/`. After you mount the partition set, the files are accessible for modifications. 

- `abupdate update`: Use this command to automatically upgrade the packages on the shadow system. This command supports tdnf and rpm as the package managers.

- `abupdate sync`: Use this command to syncronize the backup partition with the updated partition. Note that this command eliminates the ability to rollback to a safe system anymore as both becomes mirrored partitions after the command is executed.
 
- `abupdate clean`: Use this command to erase everything on the shadow partition set.
 
- `abupdate deploy <tar.gz>`: Use this command to erase and clean the shadow partition set, mount the shadow partition set, and then install or unpack the specified OS image as a tar file in the shadow partition set.
 
- `abupdate switch`: Use this command to switch from the active partition to the shadow or updated partition. Note that this command does not modify the EFI boot manager (or MBR in case of BIOS), and hence, any subsequent reboot rollbacks to the previously active partition set. 
 
- `abupdate finish`: Use this command to finalize the update. This command modifies the EFI boot manager (or MBR in case of BIOS). After you execute this command, the subsequent reboots load this partition instead of rolling back to the previous partition.





