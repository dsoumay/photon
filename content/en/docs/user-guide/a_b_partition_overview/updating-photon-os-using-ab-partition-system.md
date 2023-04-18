---
title:  Updating Photon OS Using A/B Partition System
weight: 3
---

To update or modify the Photon OS using A/B partition, perform the following steps:

1. To mount the shadow partition, execute the `abupdate mount` command.

2. Update the packages on the shadow partition.

3. To deploy the OS image on the shadow partition, specify the OS image in the following command, and then execute the command:

	`abupdate deploy <tar.gz>` 
	

4. Switch to the updated partition set.

	**Note**: If the `AUTO_SWITCH` parameter is set to yes in the configuration file, then the system automatically switches into the updated partition after the update is complete.

5. Verify that the system is running successfully in the updated partition set.
	
	**Note**: You can use the `check` command that runs various checks to verify the successful update of the partition set.

6. To finalize the update, execute the `abupdate finish` command.
	
	Note:  If the `AUTO_FINISH` parameter is set to yes, then the system automatically finalizes the switch with the finish command.

7. To sync the two partition sets, execute the `abupdate sync` command.







