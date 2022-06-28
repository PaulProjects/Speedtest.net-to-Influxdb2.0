from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

import os
import re
import subprocess
import time

# You can generate an API token from the "API Tokens Tab" in the UI
token = "XXX"
org = "XXX"
bucket = "XXX"

#getting internet speed
response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

try:
    ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE).group(1)
    download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE).group(1)
    upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE).group(1)
    jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE).group(1)

    #adding it to a sqeuence
    sequence = ["mem,host=host1 ping="+ping,"mem,host=host1 download="+download,"mem,host=host1 upload="+upload,"mem,host=host1 jitter="+jitter]

except:
        sequence = ["mem,host=host1 ping="+0,"mem,host=host1 download="+0,"mem,host=host1 upload="+0,"mem,host=host1 jitter="+0]

with InfluxDBClient(url="http://127.0.0.1:XXXX", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket, org, sequence)
client.close()
