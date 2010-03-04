#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Simple wrapper around the tesseract executable on Linux. 
#	See more here: http://code.google.com/p/tesseract-ocr/
# 	
#
#       This module is part of the docdump project, YMMV. 
#       More information can be found at http://docdump.cotes.cc
#  
#       Copyright 2009 Anthony Hiscox <docdump@cotes.cc>
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


import subprocess, tempfile, os, sys

def file_to_string(in_file):
    """ 
    Takes a temporary file as input, processes for ocr, reads the tesseract
    output file. Returns string from file. 
    """
    # temp file
    out_file = tempfile.mkstemp()[1]
       
    # Run tesseract
    try:
        tsubprocess.check_call(['tesseract', in_file, out_file])
        ocr_text = open(out_file + '.txt', 'r').read()
        os.remove(out_file)
        return ocr_text
        
    except subprocess.CalledProcessError as (returncode):
        sys.stderr.write('tesseract failed with exit code: %s' % (returncode))
        sys.stderr.flush()

if __name__ == '__main__':

	import doctest
	doctest.testmod()
