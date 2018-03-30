import os
import time
from os import environ as env
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
from neutronclient.v2_0 import client as neuclient




class Instance:
      def __init__(self,auth_url, username,password, project_name,user_domain_name,project_domain_name):
          self.loader = loading.get_plugin_loader('password')
          self.auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'],
                                project_domain_name=env['OS_PROJECT_DOMAIN_NAME'])


          self.sess = session.Session(auth=auth)
          self.nova = client.Client('2.1', session=sess)
          self.neutron=neuclient.Client(session=sess)   


      def image(self,imagename):
          if:
            img=self.nova.find_image(name=imagename)
             return img
          else:
             print "image not found"
      def flavor(self,flavorname):
          if:
            flav=self.nova.find_flavor(name=flavorname)
            return flav
          else:
             print "flavor not found"
      def network(self,networkname):
          if:
            net=self.neutron.find_network(name=networkname)
          return net
          else:
            print "network not found"
          
      def keypair(self):
          key=self.nova.find_keypairs()
          return key
      
     def instance(self):
          inst=nova.servers.create(name=None, image=img, flavor=flav,network = net,key_name=key)
          return inst  
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="validation for logging")
    parser.add_argument('--instance',help='enter valid instancename',required=True)
    parser.add_argument('--image',help='enter valid imagename',required=True)
    parser.add_argument('--flavor',help='enter valid flavorname',required=True)
    parser.add_argument('--network',help='enter the networkname',required=True)
    parser.add_argument('--keypair',help='enter the keypair',required=False)
    args = vars(parser.parse_args())
    print args
    if not(args['instancename'] or args['imagename'] or args['flavorname'] or args['networkname']):
        print "prime argument missing"
    elif  not(args['keypair']): 
        print"keypair missing "
            
    else:
          i1 =Instane(auth_url,username,password, project_name,user_domain_name,project_domain_name)
          if agrs['imagename'] not in self.nova.images.list():
                  print"enter a valid imagename"
          else:
              img1 = i1.image()
          if agrs['flavorname'] not in self.nova.flavors.list():
                  print"enter a valid flavorname"
          else:
               flav1=i1.flavor()
          if agrs['networkname'] not in self.neutron.list_networks():
                  print"enter a valid networkname"
          else:
              netw1=i1.network()
          insta=i1.instance()
          print"instance created suucessfully"
                   
    
    




 
