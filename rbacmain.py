import json
import time
from threading import Thread, Event
from basetestcase import BaseTestCase
from couchbase_helper.document import DesignDocument, View
from couchbase_helper.documentgenerator import DocumentGenerator
from membase.api.rest_client import RestConnection
from membase.helper.rebalance_helper import RebalanceHelper
from membase.api.exception import ReadDocumentException
from membase.api.exception import DesignDocCreationException
from membase.helper.cluster_helper import ClusterOperationHelper
from remote.remote_util import RemoteMachineShellConnection
from random import randint
from clitest.cli_base import CliBaseTest
import psutil
import urllib
import httplib2
import json
from security.rbacPermissionList import rbacPermissionList
from security.rbacRoles import rbacRoles


class rbacmain:

    def __init__(self,
                master_ip,
                bucket_name
            ):

        self.master_ip = master_ip
        self.bucket_name = bucket_name

    def setUp(self):
        super(rbacmain, self).setUp()


    def tearDown(self):
        super(rbacmain, self).tearDown()


    def _iterate_role_mapping(self,role_var,username,password,params=None,restClient=None,port=None):
        role_var = 'rbacRoles.' + role_var
        z =  eval('%s'%(role_var))
        role_name = z()['name']
        tc_status = True
        failList = []
        masdict = {}
        for i in range(1,2):
                permission = z()['permissionList' + str(i)]
                for perm_set in permission:
                    print perm_set
                    perm_set = "rbacPermissionList." + perm_set
                    k =  eval('%s'%(perm_set))()
                    for perm in k:
                        url, method, param = self._return_url_header_param(perm_set,perm,params)
                        print param
                        status = self._rest_client_wrapper(username,password,url,method,param,restClient,port)
                        print status
                        if (status != (z()["httpResponse" + str(i)])):
                            failList.append(perm)
                            tc_status = False
                    masdict[perm_set] = failList
                    failList = []
        return masdict,tc_status
        #self.assertTrue(tc_status,"List of permission that have failed {0}".format(masdict))


    def _return_url_header_param(self,permission_set,permission,param):
        z =  eval('%s'%(permission_set))
        values = z()[permission]
        print values
        temp = values.split(";",2)
        url = temp[0]
        #if url in ['bucket','bucket_name','name']:
        if 'bucket_name' in url:
            url = url.replace('<bucket_name>',self.bucket_name)
        if 'node_id' in url:
            url = url.replace('<node_id>',self.master_ip.ip)
        if ('replication_id') in url:
            temp_params = (param['replication_id']).replace("/",'%2F')
            #temp_params = urllib.quote(param['replication_id'])
            url = url.replace('<replication_id>',temp_params)
        if ('remote_cluster_name') in url:
            url = url.replace('<remote_cluster_name>',param['remote_cluster_name'])
        if ('doc_id') in url:
            url = url.replace('<doc_id>',param['doc_id'])

        method = temp[1]
        if len(temp) > 2:
            #temp = temp[2].replace ("'","\"")
            #params = json.loads(temp)
            temp_param = param[temp[2]]
            params = urllib.urlencode(temp_param)
        else:
            params = None
        return url,method,params

    def _rest_client_wrapper(self,username,password, url,method,params,restClient,port=None):
        if restClient == None:
            restClient = self.master_ip
        if port != None:
            restClient.port=port
        rest = RestConnection(restClient)
        rest.username = username
        rest.password = password
        api = rest.baseUrl + url
        status, content, header = rest._http_request(api, method=method, params=params)
        print content
        print status
        return header['status']

    def _raw_urllib(self,url,header,params,method):
        api = self.baseUrl + "uilogin"
        header = {'Content-type': 'application/x-www-form-urlencoded'}
        params = urllib.urlencode()
        log.info ("value of param is {0}".format(params))
        http = httplib2.Http()
        status, content = http.request(api, 'POST', headers=header, body=params)
        log.info ("Status of login command - {0}".format(status))


    def _test_box_statistics(self):
        process_dict = {}
        process_name = "beam.smp"
        process_data_collect = {}
        proc_detail = {}
        pid_detail = {}
        pid_det_list = []
        for server in self.servers:
            shell = RemoteMachineShellConnection(server)
            o,r = shell.execute_command("top -b -n 1 | grep " + process_name + " | cut -d ' ' -f2")
            process_dict[process_name] = o

        print process_dict

        for items in process_dict: # Process Name
            print process_dict[items]
            for item in process_dict[items]: # PID
                print item
                pid_detail[item]={}
            pid_det_list.append(pid_detail)
        proc_detail[items] = pid_det_list
        print proc_detail

        j=1
        for i in range(0,10):
            for items in process_dict: # Process Name
                #for item in process_dict[items]: # PID
                for i in range(0,len(items)):
                    o,r = shell.execute_command("top -b -n 1 -p " + item + " | cut -d ' ' -f3")
                    print proc_detail[items]
                    print proc_detail[items][i]
                    #print proc_detail[items][j][item]
                    #proc_detail[items][j][item].append(o)
                    #j=j+1
                j=0
        print proc_detail

