---
title:  Build a Custom ISO from the Source Code for Photon OS Installer	
weight: 8
---

Custom-ISO builder is a tool that separates out the `ISO` and the `initrd` generation logic from the ISO build script of Photon OS and helps generate an `ISO` or `initrd` as per the user requirements.

You can use this tool to build the following images:

- Custom Initrd image: The function to generate this image  is `build-initrd`
- Custom ISO image: The function to generate this image is `build-iso`

As an input to the tool, you must provide the list of all the necessary packages for the custom ISO in a JSON file. The tool only uses the minimal list of packages and their dependencies that you specify.

You can customize the following files and configurations:

- List of packages to install
- Kickstart file
- Boot command line
- Repo to download the packages
- Installer `initrd` package list

Note that when you use the Custom ISO builder to build the `ISO` and the Installer `initrd`, the `ISO` and the `initrd` file is generated in the following format:

- ISO: `photon-<photon-release-version>.iso`

- Initrd: `initrd.img`

## Prerequisite

To generate a custom ISO, ensure that you provide the following required parameters:

- List of custom packages in JSON format
- Photon Release Version
- Generating Function: For example, `build-iso`, `build-initrd`

**Note**: You must provide the additional repository if you want to include a package that the Photon OS official repository does not provide.

You can also provide the following optional parameters:

- Custom Kickstart file
- Additional repositories
- Boot command line parameters
- Custom `Initrd` package list file


## Generating a Custom ISO

1. Install the following prerequisite packages:

	- python3-pip
	- git
	- tar
	- createrepo_c
	- binutils
	- dosfstools
	- cdrkit

	*i*. To install the specified packages on Photon OS, use the following command: 
	```
	tdnf install -y python3-pip git tar createrepo_c binutils dosfstools cdrkit
	``` 

2. Run following command to install photon-os-installer python library:

	```
	pip3 install git+https://github.com/vmware/photon-os-installer.git
	```   

3. Enable the following services before you build the custom `iso`/`initrd`: `docker`
	
	i. To enable the docker service and log in to the docker account, use the following command:	
	
	```
	systemctl start docker.service;
	docker login # To avoid docker pull rate limit
	```   

4. Create the file containing the custom package list.

	The following list shows some of the sample custom package files:
	- Sample custom package file for an ISO: [packages_minimal.json](https://github.com/vmware/photon/blob/5.0/common/data/packages_minimal.json)
	- Sample initrd package list file: [packages_installer_initrd.json](https://github.com/vmware/photon/blob/master/common/data/packages_installer_initrd.json)

	Package list json format-
	```
	{
    "packages": <list-of-pkgs>,
    "packages_x86_64": <x86-specific-pkgs>,
    "packages_aarch64": <aarch64-specific-pkgs>
	}
	```    	

	**Note**: The `packages_minimal.json` file is a sample file. You can create your own JSON file with the list of custom packages that you want, and provide the directory path for the file in the command to generate the `iso`/`initrd`.

5. Generate the custom `iso`/`initrd`.

	**Case 1**: To generate a custom ISO with the provided package list, use the command in the following format:


	```
	photon-iso-builder -v <photon-release-version> -p <path/to/custom-package-list-json>
 	```  
	Example:
	```
	photon-iso-builder -v 4.0 -p /root/packages_custom.json
	```   
	**Note**: you can skip the `--function` invocation because `photon-iso-builder` sets the default function to `build-iso`.

	**Case 2**: To generate a custom ISO with provided package list and additional repository, use the  command in the following format:

	```
	photon-iso-builder -v <photon-release-version> -p <path/to/custom-package-list-json> [-r <path/to/custom-repo-list>]
	```   
	Example:
	```
	photon-iso-builder -v 4.0 -p /root/packages_custom.json -r local.repo -r local2.repo
	```   

	**Note**: In order to create your own custom repository, see the following page: [Adding a New Repository](https://vmware.github.io/photon/docs/administration-guide/managing-packages-with-tdnf/adding-a-new-repository/)


	**Case 3**: To generate a custom ISO with custom kickstart file, use the command in the following format:
	
	```
	photon-iso-builder -v <photon-release-version> -p <path/to/custom-package-list-json> -k <path-to-kickstart>
	```   

	Example:
	```
	photon-iso-builder -v 4.0 -p /root/packages_custom.json -k /root/custom_kickstart.json
	```   

	To create a custom kickstart configuration file, see the follow page: [Kickstart Configuration](https://github.com/vmware/photon-os-installer/blob/master/docs/ks_config.md)  

	**Note**: If the Kickstart file is provided while creating the custom ISO, boot command line parameter is not edited to install the ISO through kickstart.
	
	To boot the ISO through the provided kickstart file, you need to create the custom ISO file using the following format:

	```
	photon-iso-builder -v <photon-release-version> -p <path/to/custom-package-list-json> -f build-iso -k <path-to-kickstart> -b "ks=cdrom:/isolinux/<kickstart-file-base-name>"
	```   
	Example:
	```
	photon-iso-builder -v 4.0 -p /root/packages_custom.json -k /root/custom_kickstart.json -b "ks=cdrom:/isolinux/custom_kickstart.json"
	```

	**Case 4**: To generate a custom ISO with extra boot command line parameters, use the command in the following format:


	```
	photon-iso-builder -v <photon-release-version> -p <path/to/custom-package-list-json> -f build-iso -b <extra-boot-parameter>
	```   

	Example:
	```
	photon-iso-builder -v 4.0 -p /root/packages_custom.json -b "ks=http://10.197.102.86:8000/sample_ks.cfg insecure_installation=1"
	```    

	**Case 5**: to generate a custom `initrd`, use the command in the following format:

	```
	photon-iso-builder -v <photon-release-version> -c <path/to/custom-initrd-pkg-list-file> -f build-initrd
	```   
	Example:
	```
	photon-iso-builder -v 4.0 -c /root/packages_custom_initrd.json -f build-initrd
	```

	The default initrd package list file is located in the following directory: https://github.com/vmware/photon/blob/master/common/data/packages_installer_initrd.json


## Generating custom ISO through source code:

The following command demonstrate how to generate a custome ISO through the source code:

```
git clone https://github.com/vmware/photon-os-installer.git
cd photon-os-installer/photon_installer
./isoBuilder -v 4.0 -p packages_minimal.json
```

	
	
	




