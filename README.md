# uptime
Return human readable time elapsed since program start.

Example usage:

```python
import time
import uptime
    
start_uptime: float = time.perf_counter()
print(uptime.uptime(start_uptime)) # 2 hours, 46 minutes, 40 seconds 

# ~5 days later 
print(uptime.uptime(start_uptime)) # 5 days, 8 hours, 40 minutes, 2 seconds 
```
