# coding: utf-8
import unittest
from pychronus import Pychronus, serialize
import numpy as np
from sys import getsizeof
import string
import random

class CompressionTest(unittest.TestCase):

    def setUp(self):
        data = []
        # TODO : select valid data to evaluate compression
        #data.append(np.random.rand(10))
        #data.append(np.random.rand(100))
        data.append(np.random.rand(10000))
        data.append(np.random.rand(60, 1500))
        #data.append(''.join([random.choice(string.ascii_letters + string.digits) for i in range(100)]))
        data.append(''.join([random.choice(string.ascii_letters + string.digits) for i in range(1000)]))
        #data.append(np.random.rand(100000000))
        datanames = ['10', '100', '10000', '100000000', '10000000000']
        self.data = data
        self.datanames = datanames

    def test_compression(self):

        p = Pychronus(root_path='./data/', place='mem', compressed=True, compress_level=9)
        for d, dname in list(zip(self.data, self.datanames)):
            p.save(d, dname)
            print('orig: %d, compressed: %d' % (getsizeof(d), getsizeof(p.memory_data[p.root_path + dname])))
            self.assertLess(getsizeof(p.memory_data[p.root_path + dname]), getsizeof(d))

if __name__ == "__main__":
    unittest.main()
