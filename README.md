# pychronus

Pychronus give us many way of data handling

## Feature



## Installation

```
python setup.py install --record files.txt
```

## Dependency
- pickle
- redis
- bz2

## Usage


```python
p = Pychronus(root_path='./data/', place='strage', compressed=True, compress_level=9)
# save
p.save(somedata, dataname)
# load
p.load(dataname)
```
