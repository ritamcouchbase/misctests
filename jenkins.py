import json
import urllib2
import sys

job_list = {'views':['cen006-p0-sanit-vset01-00']}

url = "http://qa.sc.couchbase.com/job/"
end_url = "/lastBuild/api/json"
end_url1 = "/api/json"
filename = 'report.csv'

def write_file(line):
    f = open(filename, 'a+')
    f.write("\n" + data)
    f.close()


for key, value in job_list.items():
    for items in value:
        final_url = url + str(items) + end_url1
        job_details = urllib2.urlopen(final_url)
        job_details = json.load(job_details)
        i = 0
        job_list01 = []
        print len(job_details['builds'])
        while i < len(job_details['builds']):
            job_list01.append(job_details['builds'][i]['url'])
            i = i + 1
        for job_temp_list in job_list01:            
        print job_list01
'''
for key, value in job_list.items():
    for items in value:
        temp_str = ''
        final_url = url + str(items) + end_url
        job_details = urllib2.urlopen(final_url)
        job_details = json.load(job_details)
        temp_str = items + ","
        temp_str = temp_str + str(job_details['actions'][8]['failCount']) + ","
        temp_str = temp_str + str(job_details['actions'][8]['skipCount']) + ","
        temp_str = temp_str + str(job_details['actions'][8]['totalCount']) + ","
        temp_str = temp_str + str(job_details['actions'][0]['parameters'][0]['value'])
        print temp_str
'''


