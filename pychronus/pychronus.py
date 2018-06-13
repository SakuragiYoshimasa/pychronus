# coding: utf-8
from pychronus.utils import *
from pychronus.data_places import *

# To any situation, Pychronus give us many way of data handling
class Pychronus():
    # Constructor
    # place:
    #   - 'strage': IO through strage (i.e HDD or SSD)
    #   - 'mem': on Memory (use hash table)
    #   - 'redis': on redis

    def __init__(self, root_path='./', place='strage', compressed=True, compress_level=9):

        if place not in place_options:
            raise ValueError("'place' shuold be 'strage', 'mem', or 'redis'")
        self.root_path = root_path
        self.compressed = compressed
        self.compress_level = compress_level

        if place == 'strage':
            self.dplace = Strage()
        elif place == 'mem':
            self.dplace = Memory()
        elif place == 'redis':
            self.dplace = Redis()

    def save(self, data, dataname):
        filename = self.root_path + dataname
        _data = serialize(data)
        _data = compress(_data, self.compressed, self.compress_level)
        self.dplace.write(_data, filename)

    def load(self, dataname):
        filename = self.root_path + dataname
        _data = self.dplace.read(filename)
        _data = decompress(_data, self.compressed)
        _data = deserialize(_data)
        return _data

    def delete(self, dataname):
        pass

    def update(self, data, dataname):
        self.save(data, dataname)


if __name__ == '__main__':
    p = Pychronus('./','redis')
    p.save('hoge', 'test_data')
    print(p.load('test_data'))
