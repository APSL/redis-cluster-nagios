#!/usr/bin/python
### Check if two nodes redis cluster is in a correct status
### AUTHOR: Edu Herraiz <eherraiz@apsl.net>

import subprocess
import sys
import os

def check(option):
    command = "redis-cli info | grep %s" % option
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    return output.split(':')[1].rstrip()

role = check('role')

if role == 'slave':
    # is asociated and read only?
    mls = check('master_link_status')
    sro = check('slave_read_only')
    master = check("master_host")
    if mls == 'up' and sro == '1':
        print "OK. Slave Redis read only and master (%s) redis is up" % master
    else:
        print "CRITICAL: Slave redis is not connected to master or not marked like read_only"
elif role == 'master':
    # Check master status up
    slaves = check('connected_slaves')
    if slaves == "1":
        print "OK. Master redis and one slave connected."
    else:
        print "CRITICAL: Master redis with not slave connected"
else:
    # Unexpected error, critical informing probably redis-cli not found
    print "CRITICAL: Redis cluster information is no correct (It's a cluster? redis-cli operative?)"
 
