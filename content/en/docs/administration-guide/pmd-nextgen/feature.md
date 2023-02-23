---
title:  Features
weight: 1
---

The following table lists the `photon-mgmtd` features details:

| Feature      	| Details 	  |
| ----------- 	| ----------- |
| systemd      	|Information, services (start, stop, restart, status), service properties such as CPUShares|
| see information from /proc fs | netstat, netdev, memory and much more        |
|system			|Fetch and configure system information. For example, hostname. |
|network		|Fetch and configure network information. For example, dns, iostat, interface, and so on.|
|network link	|Configure network link parameters such as dhcp, linkLocalAddressing, multicastDNS, Address, route, domains, dns, ntp, ipv6AcceptRA, mode, mtubytes, mac, group, requiredFamilyForOnline, activationPolicy, routingPolicyRule, DHCPv4, DHCPv6, DHCPServer, Ipv6SendRA, and so on|
|login			|Fetch the list of users and sessions. You can also use this get information related to an id.|
|network devices| Create and remove virtual network devices such as VLAN, Bond, Bridge, MacVLan, IpVLan, VxLan, WireGuard, and so on.|
|ethtool		|Fetch ethernet settings for a link also based on a action|
|sysctl			|Fetch, set, load and automate kernel parameters|
|user			|Fetch, add, and remove user on the system|
|group			|Fetch, add, and remove group on the system|
|link			|Configure link parameters such as MACAddress, Name, AlternativeNames, Offload, VLANTAG, Channels, Buffers, Queues, FlowControls, Coalesce, and so on|
|firewall		|Add, delete, or view nftables, chain, and rules. You can also use this to run any nft commands|
|package management (tdnf)|Manage package on the system such as list, info, download, update, remove, clean cache, list repositories, search package, and so on|





