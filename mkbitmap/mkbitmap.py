#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       mkbitmap.py
#
#       The purpose of this module is to provide access to the
#       mkbitmap program on linux, from python.
#       It is originally designed as a component to the Docdump project.
#
#       Copyright 2009 Anthony Hiscox <anthonyhiscox@gmail.com>
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

import subprocess
import Image
import tempfile
import os
import sys

class MkBitmap:
    """
    Class "wrapping" the MkBitmap program on Linux.

    This class is currently very beta, and does not perform
    any real error checking (yet). It also does not provide
    very much functionality to most of the mkbitmap program.

    MkBitmap() can be used to pass images from python
    to the mkbitmap program which is part of the Potrace project

    See: http://potrace.sourceforge.net/mkbitmap.html

    Currently this module provides one method, L{threshold}
    which takes an image and returns a bitonal image processed by
    mkbitmap according to the instructions here:
    http://www.mscs.dal.ca/~selinger/ocr-test/

    """
    def threshold(self, image):
        """
        Applies thresholding to an image file.

        @type image: Image
        @param image: PIL Image to apply thresholding to.
        @rtype: Image
        @return: Bitonal PIL Image
        """
        mkb_filter = ['-x', '-f', '50', '-t', '0.02']
        return self.__run_mkbitmap(image, mkb_filter)

    def __run_mkbitmap(self, image, flags):
        """
        Execute the mkbitmap program on C{image} using mkbitmap
        arguments specified by C{flags}

        @type image: Image
        @param image: PIL Image of document to convert.
        @type flags: list
        @param flags: mkbitmap arguments

        @rtype: Image
        @return: Converted PIL Image
        """

        tmp = tempfile.mkdtemp()
        """Temp Path to store L{infile} and L{outfile}"""

        infile = os.path.join(tmp, 'infile.bmp')
        """Absolute path to input file"""

        outfile = os.path.join(tmp, 'outfile.pbm')
        """Absolute path to output file"""

        # Save memory image to infile.bmp
        image.save(infile)

        cmd = ['mkbitmap']
        """command to run with mkbitmap params"""

        # Append 'flags' to command line.
        for x in flags:
            cmd.append(x)

        cmd.append('-o')
        cmd.append(outfile)
        """command with outfile"""
        cmd.append(infile)
        """command to run with input and output files appended"""

        try:
            """Run mkbitmap"""
            subprocess.check_call(cmd)

        except subprocess.CalledProcessError as (returncode):
            """mkbitmap failed"""
            sys.stdout.write('MkBitmapError %s' % (returncode))
            sys.stdout.flush()

        #TODO: Cleanup temporary files by removing directory.
        m = Image.open(outfile)
        """Bitonal image"""
        return m

if __name__ == '__main__':
    n = MkBitmap()
    im = Image.open("/tmp/scan1.png")
    bitonal = n.threshold(im)
    bitonal.show()
