#!/usr/bin/python3

'''
Python script to generate a log file with a datetime stamp for log parsing
ideal out will match the ISO8601 time format
date filter format:
    date {
    match => ["t-stamp", "ISO8601"]
    target => "@timestamp"
    }
'''

import datetime, time, random

# set up a hostname data center
def generate_datacenter():
    if random.random() < 2/3:
        return('magrathea_')
    else:
        return('betelgeuse_')

# setup a hostname number b/w 100 and 300
def generate_hostnumber():
    return(int((random.random() * 1000)))

# output file setup
outfile = open('/home/zaphod/Documents/log_samples/python_log_gen.log', mode='wt')

# set the desired date
targetMonth = "03"
targetYear = "2019"
start_day = 1

# set the days in the month
for x in range(start_day, 10):
    currentTime = str(datetime.datetime.now().time())
    # print(currentTime)
    log_date = str(targetYear) + "-" + str(targetMonth) + "-" \
    + str(x) + "T" + str(currentTime[0:12]) + 'Z' + '\n'
    # print(log_date)
    # outfile.write(log_date)
    # time.sleep(1)
    print(generate_datacenter() + str(generate_hostnumber()))
