# ip9258
Python class to control an IP Power 9258 networked power switch

# Example use

```python
import time
from ip9258 import Ip9258

ip9258 = Ip9258('192.168.1.10', 'admin', 'password')

for i in range(4):
    ip9258.on(i)
    time.delay(1)

    ip9258.off(i)
    time.delay(1)
```
