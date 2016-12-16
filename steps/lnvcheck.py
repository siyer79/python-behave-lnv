import os
import sys
import subprocess
import commands
from behave import *

@given('VNI is configured')
def step_impl(context):
    status, output = commands.getstatusoutput('grep "auto vni" /etc/network/interfaces')
    if status != 0:
       raise NotImplementedError('VNI not defined in /etc/network/interfaces') 


@when('VNI is in a bridge?')
def step_impl(context):
    status, output = commands.getstatusoutput('grep "vxlan-id" /etc/network/interfaces | nawk \'{print $2}\'')

    # Create an Array with vxlan-id's
    vxlanids = output.split('\n')

    vnilist = []
   
    #  Look in the nearby lines of the vxlan id for "auto" and then add that 
    #  interface id in array vnilist
    for vxlanid in vxlanids:
       status, output = commands.getstatusoutput('grep -C 2 "vxlan-id '+vxlanid+'" /etc/network/interfaces | grep auto | nawk \'{print $2}\'')
       vnilist.append(output) 

    # Assumes that VNI matches with a bridge-port in interfaces, if it doesn't match below in the for 
    # loop then val is changed to 1
    val = 0  

    # Check if VNI is in a bridge-port  
    for vni in vnilist:
        status, output = commands.getstatusoutput('grep bridge /etc/network/interfaces | grep '+vni) 
        # check if output is blank and set val to 1 
        if not output:
           val = 1 

    if val != 0:
       raise NotImplementedError('VNI defined in interfaces is NOT in a Bridge (bridge-ports)!') 


@then('is that bridge up?')
def step_impl(context):
    status, output = commands.getstatusoutput('grep "vxlan-id" /etc/network/interfaces | nawk \'{print $2}\'')

    # Create an Array with vxlan-id's
    vxlanids = output.split('\n')

    vnilist = []

    #  Look in the nearby lines of the vxlan id for "auto" and then add that
    #  interface id in array vnilist
    for vxlanid in vxlanids:
       status, output = commands.getstatusoutput('grep -C 2 "vxlan-id '+vxlanid+'" /etc/network/interfaces | grep auto | nawk \'{print $2}\'')
       vnilist.append(output)

    bridgelist = []

    # assumes that VNI is in a bridge with val at 0, if netshow command in for loop fails
    # then it's value is changed to 1 and indicates that VNI defined is not in a bridge
    val = 0

    # Map the VNI to the Bridge, array index matches bridge to VNI
    for vni in vnilist:
        status, output = commands.getstatusoutput('netshow bridges -1 | grep '+vni+' | nawk \'{print $2}\'')
        bridgelist.append(output)
        # Check for blank string in output (i.e. no match in bridges with that VNI)
        if not output:
           val = 1 
 
    if val != 0:
       raise NotImplementedError('Bridge where VNI is defined is down!')


@then('are there other ports in the bridge?')
def step_impl(context):
    status, output = commands.getstatusoutput('grep "auto vni" /etc/network/interfaces | nawk \'{print $2}\'')

    # Create an Array with list of VNI's set on interfaces file
    vnilist = output.split('\n')
    pass


@then('do I have a route to the remote endpoints?')
def step_impl(context):
    pass


