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
    status, output = commands.getstatusoutput('grep "auto vni" /etc/network/interfaces | nawk \'{print $2}\'')

    # Create an Array with list of VNI's set on interfaces file
    vnilist = output.split('\n')

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
       raise NotImplementedError('VNI defined in interfaces is NOT in a Bridge!')

 
@then('is that bridge up?')
def step_impl(context):
    pass 

@then('are there other ports in the bridge?')
def step_impl(context):
    pass

@then('do I have a route to the remote endpoints?')
def step_impl(context):
    pass
