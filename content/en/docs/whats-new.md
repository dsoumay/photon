---
title: What is New in Photon OS 5
linkTitle: What is New in Photon 5
weight: 15
---

Photon OS 5.0  provides enhancements in Network Configuration Manager, PMD-nextgen, Container Runtime Security, Linux Real-Time Kernel, and TDNF Features. This release of Photon OS also supports XFS and BTRFS filesystems, Control Group V2,  ARM64 on Linux-esx kernel, PostgreSQL. It contains installer improvements, and critical updates to the OSS packages including Linux kernel version updates. This topic summarizes what's new and different in Photon OS 5.0.

## New Features

- **Enhancements in Network Configuration Manager:** You can now use Network Configuration Manager to perform the following tasks:

	- Configure multiple routes and addresses section
	- Configure WireGuard
	- Configure SR-IOV
	- Create NetDev, VLAN, VXLAN, Bridge, Bond, VETH (Virtual Ethernet), MacVLAN/MacVTap, IPvlan/IPvtap, tunnels (IPIP, SIT, GRE, VTI)
	- Create, configure, and remove virtual network devices

	You can run query or configure the following parameters of network devices:
	
	- Alias, Description, MTUBytes, WakeOnLan, WakeOnLanPassword, Port, BitsPerSecond, Duplex and Advertise
	- Offload parameters and other features
	- MACAddressPolicy or MACAddress
	- NamePolicy or Name
	- AlternativeNamesPolicy or AlternativeName
	- Pending packets receive a buffer
	- Queue size
	- Flow control
	- GSO
	- Channels
	- Coalesce
	- Coalesced frames
	- Coalesce packet rate

- **PMD-Nextgen Enhancement:** The capabilities to configure the following options are added to pmd-nextgen:
	- Configure system hostname
	- Configure network sriov
	- Configure Tun
	- Configure Tap
	- Configure TLS


- **Network-event-broker:** Network-event-broker now supports emitting network data in JSON format.


- **Kernel-Version Update:** The following Kernel flavors are updated to kernel version 6.0.7 in Photon OS:  
	- Linux  
	- Linux-esx  
	- Linux-secure  
	- Linux-rt  


- **Support for New Filesystems:** Support is added for the following filesystems in Photon OS:
	- XFS: With the support of the XFS filesystem, you can implement an environment that requires high performance, and scalability for data-intensive tasks.
	- BTRFS: You can use the BTRFS filesystem for high performance, better reliability, and efficient data storage capabilities.



- **Support for Control Group V2:** cgroup v2 is now available in Photon OS. With cgroup v2, you get improved resource management capabilities, a unified hierarchy scheme, and a safer sub-tree delegation to containers. Features like Pressure Stall Information and rootless containers in cgroup v2 ensure better management and security capabilities of the control groups.


- **Enhanced Container Runtime Security:** To improve the runtime security of the containers, the following enhancements are added to Photon OS:
	- Support for SELinux policy: You can now enable and configure the SELinux policy to manage access to files, directories, and other system resources. This drastically reduces the risk of a security breach.
	- Support for rootless containers: Photon OS supports rootless containers. An unprivileged user can now create and manage containers. Since unprivileged users do not have root privileges on the host machine, it prevents any security threat to the host machine.



- **Improved Linux Real-Time Kernel:** The linux-rt kernel flavor comes with improvements such as low-latency optimizations, stability enhancements, and debugging enhancements. Linux-rt now also supports the Intel Sapphire Rapids CPUs including the Telco-specific 5G ISA.


- **Support for ARM64:** Support for ARM64 is now available for the linux-esx kernel in Photon OS.
 

- **PostgreSQL versions:** The following PostgreSQL versions are supported on Photon OS:
	- PostgreSQL 13
	- PostgreSQL 14 (recommended version)


- **Driver VM SDK:** Photon OS 5.0 introduces a GPU driver VM SDK that the users can use for a specific kernel version of Photon OS. This ensures support for multiple Photon kernels on an ESXi version.

- **TDNF Feature enhancements:** The metalink functionality in tdnf is now available as a plugin. In tdnf, support is added for the following:

	- history (`list`, `rollback`, `undo` and `redo`)
	- `mark` command
	- checking the available cache size of a download
	- multiple base URLs
	- `--skip-broken` option
	- `--alldeps` option when downloading
	- `--testonly` option

### Installer and Build System Updates
- Support Pre-install script in photon installer
- A tool is now available to generate a custom initial RAM disk (initrd)
- A tool is now available to generate custom installer ISO

### Package Updates:

The following OS packages are updated:

- Linux kernel 6.0.7
- Gcc : 12.2
- Glibc 2.36
- Systemd 252.4
- Python3 3.11
- Openjdk : 11 and 17
- Openssl : 3.0.7
- Cloud-init: 22.4.2
- Rubygem: 3.1.2
- Perl: 5.36

## Notes
 
The following OS packages are removed in this release.

- Photon Management Daemon (PMD)
- lightwave
- likewise-open
- openjdk8
- fcgi
- libnss-ato
- tiptop
- ndsend
- ulogd
- lightstep-tracer-cpp
- json_spirit
- cgroup-utils
- c-rest-engine
- dcerpc
- gssapi-unix
- python3-PyPAM
- python3-backports_abc
- sshfs