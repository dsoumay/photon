---
title:  Seamless Update with A/B Partition System
weight: 6
---

You can seamlessly update or roll back Photon OS with the A/B storage partition system. When you enable the A/B partition system, Photon OS creates a shadow partition set of the system. The system maintains an active set of partitions (partition A) and an inactive set of partitions (partition B). 

The two partitions ensure that the working system runs seamlessly on the active partition set while the update is performed on the inactive partition set. After the inactive partition set is updated, the system needs a restart to switch to updated partition B. If the updated partition set does not work, the system can roll back to the previously working state on partition A. 