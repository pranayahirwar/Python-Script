#!/bin/bash

# Fill basic details here.
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

dash
echo "For how long you would like to use this VM?"
echo "In Minutes"
read labRunTime



echo "Showing Basic Account details, wait for a while."
az account show
dash

echo "Creating resource group with name $resource_group_name in $location Location..."
az group create -l $location -n $resource_group_name -o jsonc