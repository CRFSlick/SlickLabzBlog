# CIS216 WeatherApp | Log Module

This module can be used to keep a public log within the application.

# Example Usage

log_usage_example.py:
```
from log import *

log = Log()
log.clear() # Makes sure that log is empty
log.out('This thing happened')
log.out('Oops, something went wrong here!', level='error')
```
log.txt:

```
2019-10-08 14:24:27.906826 | log_usage_example.py | INFO: This thing happened
2019-10-08 14:24:27.907532 | log_usage_example.py | ERROR: Oops, something went wrong here!
```

# Usage
Log():
```
Creates Log() object

Arguments:
   filename (str): Filename of log file [Default: log] *Optional
   extension (str): Extension of log file [Default: txt] *Optional
   directory (str): Directory of log file [Default: ./] *Optional
```

out:
```
Logs data into the specified log file

Arguments:
   message (str): Log Message
   level (str): Log Level [Default: info] *Optional
```

clear:
```
Clears the log, creating a new, empty file

Arguments:
   None
```

