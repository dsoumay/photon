---
title:  Prerequisites for Running Photon OS on Azure
weight: 1
---

Before you use Photon OS with Microsoft Azure, perform the following prerequisite tasks:

1. Verify that you have a Microsoft Azure account. To create an account, see [https://azure.microsoft.com](https://azure.microsoft.com)

1. Install the latest version of Azure CLI. See [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) and [Get started with Azure CLI ](https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli?view=azure-cli-latest).

1. Verify that that you have a pair of SSH public and private keys. 

1. Download and extract the Photon OS VHD file.
    
    VMware packages Photon OS as an Azure-ready virtual hard disk (VHD file) that you can download for free from the [VMware Photon Packages](https://packages.vmware.com/photon/4.0/GA/azure/) site. This VHD file is a virtual appliance with the information and packages that Azure needs to launch an instance of Photon in the cloud. After you have downloaded the distribution archive, extract the VHD file from it. You will later need to upload this VHD file to Azure, where it will be stored in an Azure storage account. For more information, see [Downloading Photon OS](../../downloading-photon/).