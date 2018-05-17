PROJECT TITLE:
Write a python module to spawn an openstack instance and fetch its CPU utilization, MEMORY utilization and PORT statistics using its public IP.


PREREQUISITES:
python packages PYTHON OPENSTACK SDK'S
PARAMIKO
THE ENVIRONMENT VARIABLES SHOULD BE EXPORTED BY THE USER 


PROCESS:
	The python module was developed to create an instance in openstack and do SSH to that insance to  fetch the CPU UTILIZATION ,MEMORY UTILIZATON and PORT characterstics from the remote instance.


USAGE:
     The program is useful in spawning an instance in openstack on remote server and associating the floating ip to it using python sdk available in openstack sdk and 
 doing SSH using keypair to instance we can extract the characterstics of that instance with python modules which will process the remote instance output.
The commandline arguments are obtained from the user and they are internally processed in the python script then depending upon the reachability of instnce SSH process is carried out.


SAMPLE OUTPUT:
USER INPUT:
python main.py  --instance test45 --image cirros --flavor m1.tiny --network privatenetwork --key_name testkey --key_filename /root/repo/testkey.pem --username cirros

OUTPUT:
user authorization completed

Creating instance ...
waiting for 10 seconds..
Instance:'test45' is in 'BUILD' state, sleeping for 5 seconds more...
Instance: 'test45' is in 'ACTIVE'
 floating_ip added successfully

Instance:'test45' reachability  '10.0.4.3' in this host is being checked, sleeping for 5 seconds more...
host '10.0.4.3' not reachable
host '10.0.4.3' not reachable

host '10.0.4.3'reachable
calculating characteristics from the instance

PERCENTAGE CPU_UTILIZED:74.0%

PERCENTAGE MEM_FREE :7.0% ,PERCENTAGE MEM_AVAILABLE:93.0%

PORT_STATISTICS :{'lo': {'TX PACKETS': '0 bytes', 'RX PACKETS': '0 bytes'}, 'eth0': {'TX 
PACKETS': '194 bytes', 'RX PACKETS': '143 bytes'}}


GIT REPOSITORY:
https://github.com/shansclensky/murphy/blob/master/main.py
https://github.com/shansclensky/murphy/blob/master/ssh_api.py
