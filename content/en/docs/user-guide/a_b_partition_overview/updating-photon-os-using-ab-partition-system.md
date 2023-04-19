---
title:  Executing Update and Rollback Using A/B Partition System
weight: 3
---

To modify or rollback Photon OS updates using A/B partition system, perform the following workflow:

1. Edit the files on the inactive partition.
	You can use the command options like `mount`, `update`, and `deploy` to mount and edit the files based on your requirements.

2. Switch to an inactive partition using the `abupdate switch` command.
3. If you are satisfied with the update on the inactive partition, finalize the switch with the `abupdate finish` command.
4. If the update fails, reboot the system to switch back to the old active partition.


To know more about the commands for various operations, visit the following topic: **Commands for Operations**


