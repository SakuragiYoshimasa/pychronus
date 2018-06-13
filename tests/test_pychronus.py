# coding: utf-8
import unittest
import numpy as np
from pychronus.pychronus import Pychronus

class PychronusTest(unittest.TestCase):

    def setUp(self):
        data = []
        data.append('hoge')
        data.append(123456)
        data.append(1.23456)
        data.append([1,3,4,5])
        data.append(np.arange(1.0, 10.0, dtype='float64'))
        datanames = ['str_test', 'int_test', 'float_test', 'list_test', 'nplist_test']
        self.data = data
        self.datanames = datanames

    def test_strage(self):
        # compressed
        p = Pychronus(root_path='./data/', place='strage', compressed=True, compress_level=9)
        for d, dname in list(zip(self.data, self.datanames)):
            p.save(d, dname)
            if type(d) == np.ndarray:
                self.assertEqual(np.allclose(p.load(dname), d), True, dname)
            else:
                self.assertEqual(p.load(dname), d, dname)

        # not compressed
        p = Pychronus(root_path='./data/', place='strage', compressed=False, compress_level=9)
        for d, dname in list(zip(self.data, self.datanames)):
            p.save(d, dname)
            if type(d) == np.ndarray:
                self.assertEqual(np.allclose(p.load(dname), d), True, dname)
            else:
                self.assertEqual(p.load(dname), d, dname)

    def test_memory(self):
        p = Pychronus(root_path='./data/', place='mem', compressed=True, compress_level=9)
        for d, dname in list(zip(self.data, self.datanames)):
            p.save(d, dname)
            if type(d) == np.ndarray:
                self.assertEqual(np.allclose(p.load(dname), d), True, dname)
            else:
                self.assertEqual(p.load(dname), d, dname)

        # not compressed
        p = Pychronus(root_path='./data/', place='mem', compressed=False, compress_level=9)
        for d, dname in list(zip(self.data, self.datanames)):
            p.save(d, dname)
            if type(d) == np.ndarray:
                self.assertEqual(np.allclose(p.load(dname), d), True, dname)
            else:
                self.assertEqual(p.load(dname), d, dname)

    def test_redis(self):
        p = Pychronus(root_path='./data/', place='redis', compressed=True, compress_level=9)
        for d, dname in list(zip(self.data, self.datanames)):
            p.save(d, dname)
            if type(d) == np.ndarray:
                self.assertEqual(np.allclose(p.load(dname), d), True, dname)
            else:
                self.assertEqual(p.load(dname), d, dname)

        # not compressed
        p = Pychronus(root_path='./data/', place='redis', compressed=False, compress_level=9)
        for d, dname in list(zip(self.data, self.datanames)):
            p.save(d, dname)
            if type(d) == np.ndarray:
                self.assertEqual(np.allclose(p.load(dname), d), True, dname)
            else:
                self.assertEqual(p.load(dname), d, dname)

if __name__ == "__main__":
    unittest.main()
