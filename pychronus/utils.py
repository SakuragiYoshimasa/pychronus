# coding: utf-8
import pickle
import bz2

def compress(data, compressed, compress_level):
    return bz2.compress(data, compress_level) if compressed else data

def decompress(data, compressed):
    return bz2.decompress(data) if compressed else data

def serialize(data):
    return pickle.dumps(data)

def deserialize(data):
    return pickle.loads(data)
