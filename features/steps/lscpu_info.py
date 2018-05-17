#from __future__ import print_function
from behave import given,when,then,configuration
from hamcrest import*
import paramiko
import sys, pdb
import os,socket
import time
import logging
#pdb.Pdb(stdout=sys.__stdout__).set_trace() 
#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.basicConfig(filename="test.log",level=logging.INFO)

@Given ('establish ssh to a server')
def step_impl(context):
    logger.info('INITIALISING SSH  CONNECTION PROCESS')
    context.ssh_conn=paramiko.SSHClient()
    context.ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logger.info('TRYING TO ESTABLISH SSH CONNECTION ...')
    status=None
    try:
        logger.info('CONNECTING TO INSTANCE WITH A TIMEOUT ...')
        context.ssh_conn.connect(hostname=context.hostname,port=22,username=context.username,password=context.password,timeout=3)
        status=1 
    except(paramiko.ssh_exception.BadHostKeyException,IOError,paramiko.ssh_exception.AuthenticationException,paramiko.ssh_exception.SSHException,paramiko.ssh_exception.socket.error,socket.timeout) as e:
        status=2
        logger.info('Exception catched is: %s', e)
        assert_that(e==0,"{0}".format(e))
      


@When ('execute lscpu on a server')
def step_impl(context):
    context.cpuinfo=[]
    context.nic_info=[]
    context.cpu_val={}
    list_cpu=[]
    val_cpu=[]
    list_l1=[]
    list_l2=[]
    logger.info('EXECUTING CPU COMMAND  ON THE REMOTE SERVER ...')
    context.ssh_conn.stdin,context.ssh_conn.stdout,context.ssh_conn.stderr=context.ssh_conn.exec_command("lscpu")
    logger.info('RETRIVING CPU_INFO  EXECUTED ...')
    context.cpuinfo.append(context.ssh_conn.stdout.read())
    #logger.info('cpu_info retieved are: %s',context.cpuinfo)
    logger.info('CHECKING WHETHER RETRIVED CPU INFO IS EMPTY OR NOT ...')
    assert_that(len(context.cpuinfo),greater_than(0))
    logger.info('FURTHER PROCESSING THE CPU INFO TO EXTRACT FEATURES ...')
    list_cpu=(context.cpuinfo[0])
    val_cpu=list_cpu.split("\n")
    list_l1=[x.replace(" ","") for x in val_cpu]
    list_l2=[x.split(':') for x in list_l1]
    for l3 in list_l2:
        context.cpu_val[l3[0]]=l3[1:]
    logger.info(' RETRIVING  LSPCI CPU_NIC  INFO FROM REMOTE SERVER ...')

@Then('feature {feature} with {availability}')
def step_impl(context,feature,availability):
    #print(context.cpu_val)
    logger.info('CHECKING THE FEATURE AVAILABILITY ...')
    feature1=context.cpu_val['Architecture']
    feature2=context.cpu_val['Model']
    feature3=context.cpu_val['L2cache']
    assert_that(['x86_64'],equal_to(feature1),'architecture  not supported')
    assert_that(['13'],equal_to(feature2),'Model not supported')
    assert_that(['512K'],equal_to(feature3),'L2cache  not supported')
    




