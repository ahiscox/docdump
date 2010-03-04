#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
#
#       This module provides a simple method of scanning data from a 
#       Automatic Document Feed scanner with full duplex using SANE API. 
# 
#       This module is part of the docdump project, YMMV. 
#       More information can be found at http://docdump.cotes.cc
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

import os, sys, time, tempfile, shutil

class Scan:

    def __init__(self):
        import sane

        sane.init()
        self.backup = False
        """ 
        When set to a fullpath, scans will be saved immediately to the path
        specified after scanning 
        """
        
        self.device = sane.get_devices()[0][0]
        self.sane = sane.open(self.device)
        self.sane.mode = 'Color'
        self.sane.source = 'ADF Duplex'
        self.sane.resolution = 300
        self.multi = self.sane.multi_scan()
        
        self.dd = time.strftime('%Y-%m-%d')
        """ Directory named after current date, used for self.backup """

        self.dt = time.strftime('%H-%M-%S')
        """ Directory named after current time, used for self.backup """ 

        self.cnt = 0
        """ Count used for files saved on backup """ 

	self.tmp = tempfile.mkdtemp()
	""" Temp directory used for scans """ 


    def grab_page(self):
        """ 
        Scans a single page (or in the case of duplex, the front page, and then the back
        on the next call to grab_page()). Returns a PIL Image object on success, 
        returns False if the StopIteration exception was raised.  
        If self.backup is a string, a copy of the scan is saved immediatley after
        scanning to this full system path. If the path does not exist, it will be created.
        """ 

        try:

            page = self.multi.next()
            
            # Save page to temp directory
            file = os.path.join(self.tmp, 'scan-%s.pbm' % (self.cnt))
            page.save(file, 'PPM')            

            if self.backup:
                backup_path = os.path.join(self.backup, self.dd, self.dt)
                """ Path to save backup image to """ 

                backup_file = os.path.join(backup_path, 'scan-%s.pbm' % (self.cnt))
                """ Full path and filename for backup file """ 

                if not os.path.exists(backup_path):
                    os.makedirs(backup_path)

                shutil.copy(file, backup_file)

            # Increase the count used to name files.
            self.cnt += 1
            return file

        except StopIteration:
            # Out of pages to scan, close sane and return False
            self.sane.close()
            return False 

    def grab_all(self):

        pages = []

        while 1:
            im = self.grab_page()
            if not im:
                # Out of pages to scan. 
                break

            pages.append(im)

        return pages




