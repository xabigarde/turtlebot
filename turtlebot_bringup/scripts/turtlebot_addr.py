#!/usr/bin/env python3
# warning: we don't express a rosdep on netifaces.  This is part of the turtlebot image
import sys
import netifaces

for inf in netifaces.interfaces():
  if inf.startswith('wlan'):
    addrs = netifaces.ifaddresses(inf)
    if not netifaces.AF_INET in addrs:
      continue
    else:
      print(addrs[netifaces.AF_INET][0]['addr'])
      break
else:
  print("failed to determine IP address", file=sys.stderr)
  print("127.0.0.1") #bind to loopback for now
  sys.exit(1)
