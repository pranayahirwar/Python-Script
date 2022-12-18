#!/bin/bash

# Define the function
timer() {
    # Set the time limit in minutes
    time_limit=$1

    # Convert the time limit to seconds
    time_limit_seconds=$(( time_limit * 60))

    # Set the interval at which the timer should display the time remaining, in seconds
    interval=180

    # Initialize the counter
    counter=0

    while [ $counter -lt $time_limit_seconds ]
    do
      # Calculate the time remaining in minutes
      time_remaining=$(( (time_limit_seconds - counter) / 60 ))

      # Display the time remaining
      echo "Time remaining: $time_remaining minutes"

      # Sleep for the specified interval
      sleep $interval

      # Increment the counter by the interval
      counter=$(( counter + interval ))
    done

    echo "Time limit reached!"
}

dash() {
    echo ""
    echo "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
}

vmWithPassword() {
  echo "Creating VM it may take some time. Relax"
  echo "use PASSWORD for Virtual Machine connection, Account name $cna"

  az vm create \
  --resource-group $resource_group_name \
  --name $machineName \
  --image UbuntuLTS \
  --location $location \
  --admin-username $accountName \
  --admin-password $password \
  --size "$machineSize" \
  --verbose
}

vmWithSSH() {
  echo "Creating VM it may take some time. Relax"
  echo "use SSH for Virtual Machine connection, Account name $cna"

  az vm create \
  --resource-group $resource_group_name \
  --name $machineName \
  --image UbuntuLTS \
  --location $location \
  --admin-username $accountName \
  --generate-ssh-keys \
  --size "$machineSize" \
  --verbose
}

# Fill basic details here.
accountName=cna
password=QBJawPSKVOmLcZ6
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
dash

vmWithPassword
# vmWithSSH

echo "VM is created. Your time start's Now."
sleep 2
dash
timer $labRunTime
dash

echo "Deleting VMs"
az vm delete --name $machineName --resource-group $resource_group_name -y
sleep 3

echo "Deleteing resources..."

az group delete -n $resource_group_name -y
az group delete -n NetworkWatcherRG -y

