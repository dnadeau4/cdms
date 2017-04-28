import unittest
import shutil
import numpy
import tempfile
import cdms2
import os
import cdat_info

class CDMSBaseTest(unittest.TestCase):
    def getFile(self, path, mode="r"):
        f = cdms2.open(path, mode)
        self.files.append(f)
        return f

    def getDataFile(self, name):
        pth = cdat_info.get_sampledata_path()
        return self.getFile(os.path.join(pth, name))

    def getTempFile(self, path, mode="r"):
        return self.getFile(os.path.join(self.tempdir, path), mode)

    def setUp(self):
        global cdms2
        cdms2 = reload(cdms2)
        self.orig_cwd = os.getcwd()
        self.files = []
        self.NTIME = 3
        self.NLAT = 16
        self.NLON = 32
        self.test_arr = numpy.ma.arange(float(2 * self.NTIME * self.NLAT * self.NLON))
        self.test_arr.shape = (2, self.NTIME, self.NLAT, self.NLON)
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        for f in self.files:
            f.close()
        os.chdir(self.orig_cwd)
    #    shutil.rmtree(self.tempdir)

def run():
    unittest.main()
