---
title:  Seamless Update with A/B Partition System
weight: 6
---

You can seamlessly update or roll back Photon OS with the A/B storage partition system. When you enable the A/B partition system, Photon OS creates a shadow partition set of the system. The system maintains an active set of partitions and an inactive set of partitions (shadow partition). 

The two partitions ensure that the working system runs seamlessly on the active partition set while the update is performed on the inactive partition set. After the inactive partition set is updated, you can execute a fast boot that uses kexec to reboot the system into the updated partition. If the updated partition set does not work, the system can roll back to the previously working state on partition A. 

**Note**: The kexec boot is executed with the `abupdate switch` command. This is not a standard boot and does not modify the EFI boot manager (or MBR in the case of BIOS). This ensures a fast boot to quickly verify whether the system can run successfully on the updated partition. 


