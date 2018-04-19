import time, os, sys
import random
from os import environ as env
from keystoneauth1 import loading
from novaclient.exceptions import NotFound
from  novaclient import client
from keystoneauth1 import session
from neutronclient.v2_0 import  client as neuclient
import argparse
import pdb
from ssh_api import wait_for_device_avaialbility  
from ssh_api import SystemInfo  
from ssh_api import Sshclient 
#get_cpuutilization,get_memoryutilzation,get_portstatistics  

#environment variables are loaded to authenticate user
loader = loading.get_plugin_loader('password')
try:
   auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                   username=env['OS_USERNAME'],
                                   password=env['OS_PASSWORD'],
                                   project_name=env['OS_PROJECT_NAME'],
                                   user_domain_name=env['OS_USER_DOMAIN_NAME'],
                                   project_domain_name=env['OS_PROJECT_DOMAIN_NAME'])
except:
    raise Exception(" environment variables are missing!")

sess = session.Session(auth=auth)
nova = client.Client('2.1', session=sess)
neutron=neuclient.Client(session=sess)

#validation of user input 
parser = argparse.ArgumentParser(description="validation for logging")
parser.add_argument('--instance',help='enter valid instancename',required=True)
parser.add_argument('--image',help='enter valid imagename',required=True)
parser.add_argument('--flavor',help='enter valid flavorname',required=True)
parser.add_argument('--network',help='enter the networkname',required=True)
parser.add_argument('--key_name',help='enter the keypair_name',required=True)
parser.add_argument('--key_filename',help='enter the key_filenamepath --key_filename=/root/repo/testkey.pem',required=True)
parser.add_argument('--username',help='enter the username of the instance',required=True)
args = vars(parser.parse_args())

img=args['image']
flav=args['flavor']
nett=args['network']
key=args['key_name']
insta=args['instance']
key_filename=args['key_filename']
userinst=args['username']

#function to check network availability
def get_network_name():
   n1=[]
   n1=(neutron.list_networks()['networks'])
   for i in n1:
       n2=n1[0]['name']
   return n2
net1=[]
net2=get_network_name()
if(nett!=net2):
   raise Exception("Network '{0}' doesn't exist in openstack".format(nett))
else:
   pass

#function to check instance name repetition
def get_insta_name():
    inst_list = nova.servers.list()[0].__dict__
    v1=[]
    for i  in nova.servers.list():
        inst_list = i.__dict__
        v1.append(inst_list['name'])
    return v1
  
l1=len(nova.servers.list())
inst_l=[]
inst_l= l1 if l1==0 else get_insta_name()

#validation of image,flavor and keyname in openstack
try:
    image = nova.images.find(name=img)
except:
    raise Exception("Image '{0}' doesn't exist in openstack".format(img))
try:
    flavor = nova.flavors.find(name=flav)
except:
    raise Exception("Flavor '{0}' doesn't exist in openstack".format(flav))
try:
    key_name=nova.keypairs.find(name=key)
except:
    raise Exception("SSHKeypair '{0}' doesn't exist in openstack".format(key))
if inst_l==0:
   pass
else:
  for instname in inst_l:
      if(instname!=insta):
         pass
      else:
         raise Exception("instance '{0}' already exists try different instance name".format(insta))
print("user authorization completed")

#function to associate floating ip to the instance
def get_free_floating_ip():
    fl_ip_list=[]
    fl_ip_list=neutron.list_floatingips()['floatingips']
    fp_list = list()
    for ele in fl_ip_list:
        if not ele['fixed_ip_address']:
           fp_list.append(ele['floating_ip_address'])
           print fp_list 
    avail=random.choice(fp_list)
    return avail


#function to create  floatingip if floatingip list is empty
def create_floating_ip():
   cre_fl=[]
   cre_fl.append(nova.floating_ips.create(nova.floating_ip_pools.list()[0].name))
   avai=cre_fl[0]
   #avail2=random.choice(avai)
   return avai    

#networkname to netid conversion
net =nova.networks.find(label=nett)
nics=[{"net-id":net.id}]


print("Creating instance ..." )
#pdb.set_trace()
try:
   instance = nova.servers.create(name=insta, image=image, flavor=flavor,nics=nics,key_name=key)
   inst_status = instance.status
   print "waiting for 10 seconds.. "
   time.sleep(10)
except:
   raise Exception("instance '{0}' cannot be created".format(insta))

while inst_status != 'ACTIVE':
    print("Instance:'{0}' is in '{1}' state, sleeping for 5 seconds more...".format(instance.name,inst_status))
    time.sleep(5)
    instance = nova.servers.get(instance.id)
    inst_status = instance.status

print("Instance: '{0}' is in '{1}'".format(instance.name,inst_status))

#Association of floatingip 
network_pool_len=len(neutron.list_floatingips())
fll=get_free_floating_ip() if network_pool_len==0 else create_floating_ip()
instance.add_floating_ip(fll)
print(" floating_ip added successfully ")
print("Instance:'{0}' reachability  '{1}' in this host is being checked, sleeping for 5 seconds more...".format(instance.name,fll.ip))
#if the ssh to remote instance is possible then obtain characterstics 
#try reaching the remote instance 3 times and then proceed to obtain characterstics

for i in range(3):
    check_avail,ssh_connection=wait_for_device_avaialbility(hostname=str(fll.ip),username=args['username'],key_filename=args['key_filename'])


if(check_avail==True):
    sys_info=SystemInfo()
    cpu_info=sys_info.get_cpuutilization(ssh_connection)
    mem_info=sys_info.get_memoryutilization(ssh_connection)
    port_info=sys_info.get_portstatistics(ssh_connection)
    print("PERCENTAGE CPU_UTILIZED:{0}%".format(cpu_info))
    print("PERCENTAGE MEM_FREE :{0}% ,PERCENTAGE MEM_AVAILABLE:{1}%".format(mem_info[0],mem_info[1]))
    print("PORT_STATISTICS :{0}".format(port_info))
else:
   print("ssh connection cannot be made since host is unreachable")


