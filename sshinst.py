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


      def image(self):
          img=self.nova.images.list()
          return img
      
      def flavor(self):
          flav=self.nova.flavors.list()
          return flav
      
      def network(self):
          net=self.neutron.networks.list()
          return net
          
      def keypair(self):
          key=self.nova.keypairs.list()
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
        i1= Instance(instance=args['instance'], image=args['image'],flavor=args['flavor'],network=args['network'],keypair=args['keypair'])
            
    
    




 
