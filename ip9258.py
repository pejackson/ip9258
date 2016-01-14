#
# IP Power 9258 networked power switch class
#
# This work is released under the Creative Commons Zero (CC0) license.
# See http://creativecommons.org/publicdomain/zero/1.0/

# Example use:
#
# import time
# from ip9258 import Ip9258
#
# ip9258 = Ip9258('192.168.1.10', 'admin', 'password')
#
# for i in range(4):
#     ip9258.on(i)
#     time.delay(1)
#
#     ip9258.off(i)
#     time.delay(1)

import urllib2

class Ip9258:
    def __init__(self, hostname, username, password):
        self._hostname = hostname

        # create a password manager
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, 'http://' + hostname, username, password)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        # Now all calls to urllib2.urlopen use our opener.
        urllib2.install_opener(opener)

    def on(self, port):
        return urllib2.urlopen('http://' + self._hostname + '/set.cmd?cmd=setpower+p6' + str(port) + '=1')

    def off(self, port):
        return urllib2.urlopen('http://' + self._hostname + '/set.cmd?cmd=setpower+p6' + str(port) + '=0')