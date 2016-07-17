from couchbase import Couchbase
from couchbase.exceptions import CouchbaseError
import time
import thread
from couchbase.n1ql import N1QLError, N1QLQuery
import Queue
import threading
import datetime
import csv
import json
from Tkconstants import FIRST

totalnumber = 0
deletenumber = 0
updatenumber = 0
updateFlag = 0
temp = []
masterHost = '172.23.107.63'

machines = []

def write_to_file(data):
    f = open ("file.csv", 'a+')
    f.write("\n" + data)
    f.close()


def read_file():
    f = open ('results.csv', 'rb')
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if (i == 0):
            print 'first'
            i = i + 1
        else:
            try:
                s = row[4]
                json_acceptable_string = s.replace("'", "\"")
                json_acceptable_string = json_acceptable_string.replace("#", "\"")
                json_acceptable_string = json_acceptable_string.replace("(", "\"")
                json_acceptable_string = json_acceptable_string.replace(")", "\"")
                d = json.loads(json_acceptable_string)
                temp = str(d['component']) + "," + str(d['totalCount']) + "," + str(d['failCount']) + "," + str(d['os']) + "," + str(d['build'])
                write_to_file(temp)
            except:
                print json_acceptable_string

read_file()
