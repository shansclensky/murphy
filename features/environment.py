#file---features/environment
import paramiko
import time

def before_all(context):
    context.hostname=context.config.userdata.get("hostname")
    context.username=context.config.userdata.get("username")
    #context.key_filename=context.config.userdata.get("key_filename")
    context.password=context.config.userdata.get("password")
    if(context.hostname=="None" or len(context.hostname)<=0):
        raise ValueError("enter a valid hostname!")
    if(context.username=="None" or len(context.username)<=0):
        raise ValueError("enter a valid username")
    #if(context.key_filename=="None"or len(context.key_filename)<=0):
    #    raise ValueError("enter a valid key_filename")
    if(context.password=="None" or len(context.password)<=0):
        raise ValueError("enter a valid password")
