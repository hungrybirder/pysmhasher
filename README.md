# Google SMHasher Python扩展#

参考[pypi smhasher](https://pypi.python.org/pypi/smhasher)，但它只封装了MurMurHash3。


## 安装方法 ##
```
pip install pysmhasher
```

## 使用方法 ##
```
>>> import pysmhasher
>>> pysmhasher.murmurhash2('hello')
3848350155
>>> seed = 27
>>> pysmhasher.murmurhash2('hello', seed)
1143501851
```

