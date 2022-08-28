from asyncio import streams
from importlib.resources import path
from pathlib import Path
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# ...
# stream = """
# class2:
#  - A
#  - B
#  - C
#  """

stream = open(u'F:\\code\\python\\yaml\\test-01.yaml', encoding="UTF-8")

data = load(stream, Loader=Loader)
print(data)
# ...

output = dump(data, Dumper=Dumper)
print(output)