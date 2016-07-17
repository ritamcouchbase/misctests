from couchbase import Couchbase
from couchbase.exceptions import CouchbaseError
import time
import thread
from couchbase.n1ql import N1QLError, N1QLQuery
import Queue
import threading
import datetime

key1 = 'demo_key'
value1 = {
          "name":"demo_value",
          "lastname":'lastname',
          "areapin":'',
          "preference":'veg',
          "type":''
        }


totalnumber = 0
deletenumber = 0
updatenumber = 0
updateFlag = 0
temp = []
masterHost = 'localhost'

machines = []

def write_to_file(data):
    f = open ("stat.txt", 'a+')
    f.write("\n" + data)
    f.close()

def initialSetup(bucketName='voltest01', host='localhost'):
    conn = Couchbase.connect (bucket=bucketName, host=host)
    return conn

def createBulkDocuments(start_num=0, end_num=100000, client='conn'):
    global totalnumber
    global updateFlag
    start_time = time.time()
    for x in range (start_num, end_num):
        value = value1.copy()
        key = 'demo_key'
        key = key + str(x)
        for key1 in value:
            if value[key1] == 'type' and x % 2 == 0:
                value['type'] = 'odd'
            else:
                value['type'] = 'even'
            value[key1] = value[key1] + str(x)
        value['id'] = str(x)
        result = client.set(key, value)
        totalnumber = totalnumber + 1
        #print "Inserted Key", key
    #value = {"name":"demo_value1" + str(x), "number":x}
    #result = c.set(key, value)
    end_time = time.time()
    updateFlag = 1
    print "Time taken", end_time - start_time

def createBulkDocumentsTime(runsec, client='conn'):
    try:
        write_to_file("Bulk Create Documents started")
        write_to_file('Time when bulk create started' + str(datetime.datetime.now()))
        global totalnumber
        global updateFlag
        elapsedtime = 0
        start_time = time.time()
        temp_time = 0
        while (elapsedtime < runsec):
            value = value1.copy()
            key = 'demo_key'
            key = key + str(totalnumber)
            for key1 in value:
                if value[key1] == 'type' and x % 2 == 0:
                    value['type'] = 'odd'
                else:
                    value['type'] = 'even'
                value[key1] = value[key1] + str(totalnumber)
            value['id'] = str(totalnumber)
            result = client.set(key, value)
            totalnumber = totalnumber + 1
            #print "Inserted Key", key
            elapsedtime = time.time() - start_time
        #value = {"name":"demo_value1" + str(x), "number":x}
        #result = c.set(key, value)
        end_time = time.time()
        updateFlag = 1
        write_to_file("Time taken for initial document load " + str(end_time - start_time))
        write_to_file("Time taken for initial document load " + str(datetime.datetime.now()))
        write_to_file("Total documents written in first load " + str(totalnumber))
    except:
        write_to_file("Exception occurred in creating initial data")
        write_to_file("Time taken for initial document load " + str(datetime.datetime.now()))
        write_to_file("Total documents written in first load " + str(totalnumber))

    print "Time taken", end_time - start_time


def createDocuments(create_num, client='conn'):
    try:
        print "Into Create Documents"
        write_to_file("Create Documents started")
        write_to_file('Time when second load started' + str(datetime.datetime.now()))
        global totalnumber
        start_time = time.time()
        updates = (totalnumber * create_num) / 100
        for x in range(totalnumber, totalnumber + updates):
            value = value1.copy()
            key = "demo_key"
            key = key + str(x)
            for key1 in value:
                if value[key1] == 'type' and x % 2 == 0:
                    value['type'] = 'odd'
                else:
                    value['type'] = 'even'
                value[key1] = value[key1] + str(x)
            value['id'] = str(x)
            result = client.set(key, value)
            totalnumber = totalnumber + 1
            #print "Inserted Key", key
        write_to_file("Time taken for second document load " + str(end_time - start_time))
        write_to_file("Time taken for second document load " + str(datetime.datetime.now()))
        write_to_file("Total documents written in seocnd load" + str(totalnumber))
    except:
        write_to_file("Exception occurred in 2nd set of data")
        write_to_file("Time taken for second document load " + str(datetime.datetime.now()))
        write_to_file("Total documents written in seocnd load" + str(totalnumber))


def deleteDocuments(delete_num, client="conn"):
    try:
        print "Into Delete Documents"
        write_to_file("Delete Documents started")
        write_to_file('Time when delete started' + str(datetime.datetime.now()))
        global deletenumber
        global totalnumber
        deletenum = (totalnumber * delete_num) / 100
        temp_total = totalnumber
        start_time = time.time()
        for x in range (temp_total - deletenum, temp_total):
            key = key1
            key = key + str(x)
            result = client.delete(key)
            totalnumber = totalnumber - 1
            deletenumber = deletenumber + 1
            #print "Key Deleted", key
        end_time = time.time()
        write_to_file("Time taken for document deletion " + str(end_time - start_time))
        write_to_file("Time taken for document deletion " + str(datetime.datetime.now()))
        write_to_file("Total documents after document deletion" + str(totalnumber))
        write_to_file("Total documents deletion" + str(deletenumber))
    except:
        write_to_file("Exception occured while deleting documents ")
        write_to_file("Time taken for document deletion " + str(datetime.datetime.now()))
        write_to_file("Total documents after document deletion" + str(totalnumber))
        write_to_file("Total documents deletion" + str(deletenumber))


def updateDocuments(update_num, client='conn'):
    try:
        print "Into Update Documents"
        write_to_file("Update Documents started")
        write_to_file('Time when update started' + str(datetime.datetime.now()))
        global updatenumber
        global totalnumber
        update_num = (totalnumber * update_num) / 100
        start_time = time.time()
        for x in range (0, update_num):
            key = key1
            key = key + str(x)
            temp = client.get(key)
            temp.value['type'] = 'updated'
            result = client.set(key, temp.value)
            updatenumber = updatenumber + 1
            #print "Key Update", key
        #value = {"name":"demo_value1" + str(x), "number":x}
        #result = c.set(key, value)
        end_time = time.time()
        print "Time taken", end_time - start_time
        write_to_file("Time taken for document updating " + str(end_time - start_time))
        write_to_file("Time taken for document updating " + str(datetime.datetime.now()))
        write_to_file("Total documents after document updation" + str(totalnumber))
        write_to_file("Total documents updated" + str(updatenumber))
    except:
        write_to_file("Exception occured while updating documents ")
        write_to_file("Time taken for document updating " + str(datetime.datetime.now()))
        write_to_file("Total documents after document updation" + str(totalnumber))
        write_to_file("Total documents updated" + str(updatenumber))


def createQuery(query, client):
    result = client.n1ql_query(query).execute()

def queryDocuments(query, client, time1):
    try:
        write_to_file("Querying started for query " + query)
        write_to_file("querying started " + str(datetime.datetime.now()))
        start_time = time.time()
        end_time = 0
        while end_time < time1:
            for row in client.n1ql_query(query):
                print '...', row
            end_time = time.time() - start_time
        end_time = time.time()
        write_to_file("Time taken for querying " + str(end_time - start_time))
        write_to_file("Time taken for querying " + str(datetime.datetime.now()))
        write_to_file("Total from query " + str(row))
    except:
        write_to_file("Exception occured while quering documents ")
        write_to_file("Time taken for querying " + str(end_time - start_time))
        write_to_file("Time taken for querying " + str(datetime.datetime.now()))


def simpleQueryDocuments(query, client):
    for row in client.n1ql_query(query):
        temp.append(row)
    return temp


'''
1. Initial setup:
- Create a Bucket in advance. 
- Pass in the cluster ip address that needs to be run. SDK will automatically divide the load. 
'''

createIndexConn01 = initialSetup(host=masterHost)
docCreateBulk = initialSetup(host=masterHost)
docCreate = initialSetup(host=masterHost)
docUpdate = initialSetup(host=masterHost)
docDelete = initialSetup(host=masterHost)
query01 = initialSetup(host=masterHost)
query02 = initialSetup(host=masterHost)
query03 = initialSetup(host=masterHost)


createIndex = threading.Thread(name='createIndex', target=createQuery, args=("Create primary index on voltest01", createIndexConn01,))
createIndex.start()
createIndex.join()
time.sleep(60)
createIndex = threading.Thread(name='createIndex', target=createQuery, args=('create index index5 on voltest01(type) using gsi WITH {"nodes": ["172.30.0.203:8091"]}', createIndexConn01,))
createIndex.start()
createIndex.join()
time.sleep(60)
createIndex = threading.Thread(name='createIndex', target=createQuery, args=('create index index6 on voltest01(id) using gsi WITH {"nodes": ["172.30.0.159:8091"]}', createIndexConn01,))
createIndex.start()
createIndex.join()
time.sleep(60)


query01 = threading.Thread(name='query01', target=queryDocuments, args=("select count(*) from voltest01 where type == 'updated'", query01, 9600,))
query01.start()
query02 = threading.Thread(name='query02', target=queryDocuments, args=("select count(*) from voltest01 where id > 1000  and id < 10000", query02, 9600,))
query02.start()

docCreateBulk = threading.Thread(name='docCreateBulk', target=createBulkDocumentsTime, args=(7200, docCreateBulk,))
docCreateBulk.start()
docCreateBulk.join()
time.sleep(30)

print totalnumber

docCreate = threading.Thread(name='docCreate', target=createDocuments, args=(50, docCreate,))
docCreate.start()
docUpdate = threading.Thread(name='docUpdate', target=updateDocuments, args=(50, docUpdate,))
docUpdate.start()
docDelete = threading.Thread(name='docDelete', target=deleteDocuments(50, docDelete,))
docDelete.start()

temp = simpleQueryDocuments("select * from system:indexes", query01)
print temp
time.sleep(30)


docCreate.join()
docUpdate.join()
docDelete.join()
query01.join()
query02.join()
print totalnumber
print updatenumber
print deletenumber


temp = simpleQueryDocuments("select count(*) from voltest01 where type == 'updated'", query03)
print temp
temp = simpleQueryDocuments("explain select count(*) from voltest01 where type == 'updated'", query03)
print temp
temp = simpleQueryDocuments("select count(*) from voltest01 where type == 'odd'", query03)
print temp
temp = simpleQueryDocuments("select count(*) from voltest01 where type == 'odd'", query03)
print temp
