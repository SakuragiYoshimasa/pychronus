# coding: utf-8
import redis

place_options = ['strage', 'mem', 'redis']

class DataPlace():
    def write(self, data, filename):
        pass
    def read(self, filename):
        pass

class Strage(DataPlace):
    def write(self, data, filename):
        with open(filename, 'wb') as f:
            f.write(data)

    def read(self, filename):
        data = None
        with open(filename, 'rb') as f:
            data = f.read()
        return data

class Memory(DataPlace):
    def __init__(self):
        self.mem = {}

    def write(self, data, filename):
        self.mem[filename] = data

    def read(self, filename):
        return self.mem[filename]

class Redis(DataPlace):
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def write(self, data, filename):
        self.redis.set(filename, data)

    def read(self, filename):
        return self.redis.get(filename)
