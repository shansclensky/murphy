import os
import time
from os import environ as env
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
from neutronclient.v2_0 import client as neuclient




class Instance:
      def __init__(self,image=None,flavor=None,network=None,key_name=None):
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
          self.image  
              





 
