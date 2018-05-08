"""
    Description: Check all the zones in /etc/bind the quick way
"""

import subprocess
import os

__author__ = 'Ronald Osure (c) KENET 2018'

def main():
    zones_tmp = subprocess.check_output('ls /etc/bind/pri.*', shell=True)
    zones = zones_tmp.split('\n')
    zones.remove('')
    for zone in zones:
        zone_with_pri = os.path.split(zone)[1]
        domain = zone_with_pri.split('pri.')[1]
        print "DEBUG: processing %s" % domain
        # We are simply looking for a none zero exit status. That will mean that
        # named-checkzone failed
        try:
            a = subprocess.check_output('named-checkzone %s %s' % (domain, zone), shell=True)
            print "DEBUG: domain %s is OK" % domain
        except subprocess.CalledProcessError,e:
            print "----------\nERROR: on domain %s" % domain
            print e
            print e.output + "----------\n"


if __name__ == '__main__':
    main()
