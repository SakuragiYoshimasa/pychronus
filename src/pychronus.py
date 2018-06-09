# coding: utf-8
import redis
import pickle
import bz2

# To any situation, Pychronus give us many way of data handling

place_options = ['strage', 'mem', 'redis']
compress_options = [None, 'gzip', 'bz2', 'zip']

def compress(data, compressed, compress_level):
    return bz2.compress(data, compress_level) if compressed else data

def decompress(data, compressed):
    return bz2.decompress(data) if compressed else data

def serialize(data):
    return pickle.dumps(data)

def deserialize(data):
    return pickle.loads(data)

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
        self.place = place
        self.compressed = compressed
        self.compress_level = compress_level
        self.memory_data = {}
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def save(self, data, dataname):
        filename = self.root_path + dataname
        place = self.place
        _data = serialize(data)
        _data = compress(_data, self.compressed, self.compress_level)
        if place == 'strage':
            with open(filename, 'wb') as f:
                f.write(_data)

        elif place == 'mem':
            self.memory_data[filename] = _data

        elif place == 'redis':
            self.redis.set(filename, _data)

    def load(self, dataname):
        filename = self.root_path + dataname
        place = self.place
        _data = None

        if place == 'strage':
            with open(filename, 'rb') as f:
                _data = f.read()

        elif place == 'mem':
            _data = self.memory_data[filename]

        elif place == 'redis':
            _data = self.redis.get(filename)

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
