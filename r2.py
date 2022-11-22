from scapy.all import *
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd
all_macs = {iface.mac for iface in ifaces.values()}
print(all_macs)
connection2pid = {}
pid2traffic = defaultdict(lambda: [0,0])
print(pid2traffic)
global_df = None
is_program_running = True
def get_size(bytes):
    for unit in['','k','M','G','T','P']:
        if bytes < 1024:
            return f"(bytes:.2f)(unit)B"
        bytes /=1024    