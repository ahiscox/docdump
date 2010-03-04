#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Simple wrapper around the unpaper executable on Linux. 
#       More information on unpaper can be found at their website:
#       http://unpaper.berlios.de/ - unpaper@jensgulden.de
#       Unpaper is copyright Jens Gulden and released under the GPL. 
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


import subprocess, tempfile, os, sys, shutil

class UnPaper:
    """
    Takes temporary files and converts them using unpaper.
    """
    
    def __init__(self):
        
        self.tmpdir = tempfile.mkdtemp()
        """ Temp Directory for output files from unpaper """

        self.cnt = 0
        """ Counter for file naming """ 
        
        
    def process(self, in_file, tiff=False):
        """
        Processes in_file and returns full path to converted file. 
        Deletes in_file upon successful completion. 
        Returns out_file (full path to output pbm)
        Optional tiff parameter converts output files to uncompressed
        tiff files for Tesseract OCR deleting the pbm originals. 
	"""
        from PIL import Image 

	out_file = os.path.join(self.tmpdir, "scan-%s.pbm" % (self.cnt))
	self.cnt += 1

        try:
            subprocess.check_call(['unpaper', in_file, out_file])
            # Now check file exists:
            if os.path.exists(out_file):
                # If tiff=True convert to tiff file.
                if tiff: 
                    tiff_out_file = out_file + '.tif'
                    Image.open(out_file).save(tiff_out_file, 'TIFF')
                    os.remove(out_file)
                    os.remove(in_file)
                    return tiff_out_file
                else:
                    os.remove(in_file)
                    return out_file

            else: 
                raise UnpaperWriteFailed('unpaper failed to write to %s' % (out_file))
        
        except subprocess.CalledProcessError as (returncode):
		raise UnpaperRunFailed('unpaper failed with exit code: %s' % (returncode))

    def process_dir(self, in_dir, tiff=False):
        """
        Process an entire directory using the self.process() method. 
        Removes entire directory when done. 
        Optional parameter converts pbm output to tiff for tesseract.
        Returns a list of absolute paths to all output files. 
        """ 

        files = os.listdir(in_dir)
        
        # For each file in directory, process
        # Pack list for returning 
        out_files = [] 
        for file in files:
            out_file = self.process(os.path.join(in_dir, file), tiff)
            out_files.append(out_file)

        # Clean up
        shutil.rmtree(in_dir)
        return out_files
        
class UnpaperRunFailed(Exception):
    def __init__(self, m): Exception.__init__(self, m) 

class UnpaperWriteFailed(Exception): 
    def __init__(self, m): Exception.__init__(self, m)

if __name__ == '__main__':
	
	import doctest
	doctest.testmod()
