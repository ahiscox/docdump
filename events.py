#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       This module provides a simple method of implementing a supervisord
#       process event handler. It is part of the docdump project.
#       
#       Copyright 2010 Anthony Hiscox <docdump@cotes.cc>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


import sys, os

# Setup django models
sys.path.append('frontend')

os.environ['DJANGO_SETTINGS_MODULE'] = 'frontend.settings'
from django.core.management import setup_environ
from frontend import settings
setup_environ(settings)

class SupervisorEventListener:
    """
        A class to faciliate writing supervisord event listeners.
        Usage:
        >>> class onError(SupervisorEventListener):
                def callback(self):
                    self.write_out('callback_test', True)
        >>> e = onError()
        >>> e.eventloop()
        READY

        Simply override SupervisorEventListener.callback() in your
        event handler. 
    """

    def __init__(self):
        """ I currently don't have a need for this """ 
        pass    
    
    def write_out(self, s, err=False):
        """
            Write to stdout/stderr. if err=True write to stderr, else stdout.
        """
        if err:
            sys.stderr.write(s)
            sys.stderr.flush()
        else:
            sys.stdout.write(s)
            sys.stdout.flush()

    def eventloop(self):
        """
            Main loop that runs the event listener. 
        """

        while 1:
            self.write_out('READY\n')
            line = sys.stdin.readline()
            headers = dict([ x.split(':') for x in line.split() ])
            data = sys.stdin.read(int(self.headers['len']))
            self.callback(headers, data)
            self.write_out('RESULT 2\nOK')
            
    def callback(self, headers, data):
        """ 
            Override this method, it is called when the event is triggered.    
        """ 
        raise NotImplementedError("Subclass must implement abstract method")



# Example below uses ratpoison to echo the supervisord event payload
if __name__ == '__main__':
    import ratpoison
    import doctest
    
    class OnError(SupervisorEventListener):
        def callback(self, headers, data):
            ratpoison.rp_echo(data)
            for i in data.split('\n'):
                if 'Mongoose Incident Indentifier' in i:
                    # We encountered a Mongoose issue, update scan status.
                    ratpoison.rp_echo('ERROR! ' + data)
                    status = ScanStatus.objects.get(pk=1)
                    status.in_progress = False
                    status.percent = 0
                    status.message = i
                    status.save()

    doctest.testmod()
    j = OnError()
    j.eventloop()
    
