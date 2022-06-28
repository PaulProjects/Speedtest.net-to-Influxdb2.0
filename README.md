# Speedtest.net-to-Influxdb2.0
Reads the results of a speedtest.net cli run and pushes them to influxdb2.0

# Instructions:
1. Make sure you have the speedtest.net cli tool, influxdb2.0 and python3.9 installed
2. Download the file
3. Insert your Token, organisation and desired bucket (Influxdb)
4. Insert the port number of influxdb2.0 (I suggest running both on the same device)
5. Create a cron job (I suggest every 5 min)
6. Done

# Notes:
- Uses 0 values if the check fails (can be replaced with null)
