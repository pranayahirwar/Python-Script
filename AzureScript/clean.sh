#!/bin/bash

accountName=cna
machineName=cartoonet
location=centralindia
resource_group_name=cartoon-rg
machineSize=Standard_B1s


echo "This script is going to create VM, with below following parameters"
echo "Computer Account Name : $accountName "
echo "VM Name : $machineName"
echo "Location : $location"
echo "Resource Group Name : $resource_group_name"
echo "Machine Size is : $size"

# echo "Deleting VMs"
# az vm delete --name $machineName --resource-group $resource_group_name -y
# sleep 3

echo "Deleteing $resource_group_name resources..."
az group delete --resource-group $resource_group_name -y

echo "Deleteing NetworkWatcherRG resources..."
az group delete -g NetworkWatcherRG -y