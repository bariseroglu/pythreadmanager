# pythreadmanager
A minimal thread management package for python

## Installation

```bash
pip install pythreadmanager
```
## Usage

```python
from pythreadmanager.threadmanager import Loop, Timeout
import time

def test(a, b, c, thread):
    print(a, b, c, thread)

if __name__ == '__main__':
    Timeout(test, args=(1, 2, 3, 'timeout'), timeout=2)
    l1 = Loop(test, args=(1, 2, 3, 'loop'), timer=3)
    time.sleep(10)
    l1.terminate()
```

