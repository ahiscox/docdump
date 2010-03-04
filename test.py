#!/usr/bin/env python


import unittest, os
""" Skip tesseract & unpaper tests 
class TestTesseract(unittest.TestCase):
    
    def runTest(self):
        import Image
        from tesseract import Tesseract

        im = Image.open('test.bmp')
        assert im, 'Failed to open test bitmap'

        tess = Tesseract()
        assert tess, 'Failed to instantiate Tesseract'

        result = tess.process(im)
        assert len(result) > 0, 'There was no OCR returned, or page is blank!'


class TestUnPaper(unittest.TestCase):

    def setUp(self):
        from unpaper import UnPaper
        import Image

        self.im = Image.open('test.bmp')
        assert self.im, 'Failed to open test bitmap'

        self.unpaper = UnPaper()
        assert self.unpaper, 'Failed to instantiate unpaper'

    def runTest(self):
        
        # First grab a full path to a file
        fixed_page_file = self.unpaper.process(self.im, False)
        assert fixed_page_file, 'Failed to fix image and return file path'

        # Check that fixed_page_file returned an existing file.
        assert os.path.exists(fixed_page_file)
        
        # Next grab a PIL image fixed by unpaper (note, this deletes the tmp file):
        fixed_page_image = self.unpaper.process(self.im)
        assert fixed_page_image, 'Failed to fix image and return PIL Image instance'
        
        
 """ 

class TestScan(unittest.TestCase):

    def setUp(self):
        import scan3
        import sane

        self.scan = scan3.Scan()
        self.scan.backup = '/home/fnadmin/testbackup/'
        # self.scan.device = sane.get_devices[0][0]

        # assert self.scan.device
        assert self.scan.backup == '/home/fnadmin/testbackup/'


class TestScanGrabPage(TestScan):

    def runTest(self):
        page = self.scan.grab_page()
	print page
        print type(page).__name__
        # assert type(page).__name__ == 'string'



class TestScanGrabAll(TestScan):
    def runTest(self):
        pages = self.scan.grab_all()
        assert pages
        assert len(pages) > 0, 'No pages were scanned!'

	print str(pages)
        for page in pages:
            print "Got scan: %s" % (page)
	    
if __name__ == '__main__':

    unittest.main()

    while 1: 
        time.sleep(10)

