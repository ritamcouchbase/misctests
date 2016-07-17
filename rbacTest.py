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
from security.ldaptest import ldaptest
from security.rbacmain import rbacmain
from xdcr.xdcrnewbasetests import XDCRNewBaseTest
from membase.helper.cluster_helper import ClusterOperationHelper


class rbacTest(ldaptest):

    def setUp(self):
        super(rbacTest, self).setUp()
        self.rest = RestConnection(self.master)
        self.userList = "bjons:password"
        self.userList = self.returnUserList(self.userList)
        #self._removeLdapUserRemote(self.userList)
        #self._createLDAPUser(self.userList)
        self.roleName = self.input.param("roleName")
        self.rbac = rbacmain(self.master,'default')
        #rest.ldapUserRestOperation(True, ROadminUser=self.userList, exclude=None)

    def tearDown(self):
        super(rbacTest, self).tearDown()

    def _XDCR_role_test(self):
        params = {}
        remote_cluster_name = 'rbac_cluster'
        remote_server01 = self.servers[1]
        remote_server02 = self.servers[2]
        read_role = '_replication_admin_read'
        write_role = '_replication_admin_write'
        rest_remote01 = RestConnection(remote_server01)
        rest_remote01.create_bucket(bucket='default', ramQuotaMB=100)
        rest_remote02 = RestConnection(remote_server02)
        rest_remote02.create_bucket(bucket='default', ramQuotaMB=100)

        #------ First Test the Get Requests for XDCR --------------#

        #Remove all remote cluster references
        self.rest.remove_all_replications()
        self.rest.remove_all_remote_clusters()

        #Add remote cluster reference and replications
        self.rest.add_remote_cluster(remote_server01.ip,8091,'Administrator','password',remote_cluster_name)
        replication_id = self.rest.start_replication('continuous','default',remote_cluster_name)
        masDict,tc_status = self.rbac._iterate_role_mapping(read_role,"Administrator","password",{'replication_id':replication_id})

        self.rest.remove_all_replications()
        self.rest.remove_all_remote_clusters()
        rest_remote01.remove_all_replications()
        rest_remote01.remove_all_remote_clusters()
        rest_remote02.remove_all_replications()
        rest_remote02.remove_all_remote_clusters()


        # ----------- Second Test for POST requests for XDCR ---------------#

        self.rest.remove_all_replications()
        self.rest.remove_all_remote_clusters()
        rest_remote01.remove_all_replications()
        rest_remote01.remove_all_remote_clusters()
        rest_remote02.remove_all_replications()
        rest_remote02.remove_all_remote_clusters()


        self.rest.add_remote_cluster(remote_server01.ip,8091,'Administrator','password',"onetotwo")
        #self.rest.add_remote_cluster(remote_server02.ip,8091,'Administrator','password','onetothree')
        #rest_remote01.add_remote_cluster(remote_server02.ip,8091,'Administrator','password',"twotothree")
        rest_remote01.add_remote_cluster(self.master.ip,8091,'Administrator','password','twotoone')
        rest_remote02.add_remote_cluster(remote_server01.ip,8091,'Administrator','password',"threetotwo")
        rest_remote02.add_remote_cluster(self.master.ip,8091,'Administrator','password','threetoone')

        params['remote_cluster_name']='onetotwo'
        params['remoteCluster01'] = {'username': 'Administrator', 'password': 'password', 'hostname': '192.168.46.103:8091', 'name': 'onetothree'}

        params['create_replication'] = {'replicationType': 'continuous','toBucket': 'default','fromBucket': 'default','toCluster': 'twotoone','type': 'xmem'}
        params['replication_id'] = rest_remote01.start_replication('continuous','default','twotoone')



        masDict,tc_status = self.rbac._iterate_role_mapping('_replication_admin_write01',"Administrator","password",params)
        masDict,tc_status = self.rbac._iterate_role_mapping('_replication_admin_write02',"Administrator","password",params,self.servers[1])

        '''
        self.rest.remove_all_replications()
        self.rest.remove_all_remote_clusters()
        rest_remote01.remove_all_replications()
        rest_remote01.remove_all_remote_clusters()
        rest_remote02.remove_all_replications()
        rest_remote02.remove_all_remote_clusters()
        '''


    def _raw_urllib(self):
        api = "http://192.168.46.101:8092/" + "default/_design/test1"
        header = {'Content-Type': 'application/json'}
        params = '{"views":{"test1":{"map":"function (doc, meta) {emit(meta.id, null);}"}}}'
        http = httplib2.Http()
        status, content = http.request(api, 'PUT', headers=header,body=params)
        print status
        print content


    def _view_admin_role_test(self):
        #----------------Get ddocs -----------#
        view = ['abcd']
        default_design_doc_name = "Doc1"
        default_map_func = 'function (doc) { emit(doc.age, doc.first_name);}'
        params = {}
        view = View('abcd', default_map_func, None)
        self.cluster.create_view(
             self.master, default_design_doc_name, view,
                    'default',180,with_query=False)
        masDict,tc_status = self.rbac._iterate_role_mapping('_view_admin_read',"Administrator","password")

        doc_id = "_design/dev_Doc1"

        params['doc_id'] = doc_id
        test_param = {"views" : {"byloc" : {"map" : "function (doc, meta) {\n  if (meta.type == \"json\") {\n    emit(doc.city, doc.sales);\n  } else {\n    emit([\"blob\"]);\n  }\n}"}}}

        masDict,tc_status = self.rbac._iterate_role_mapping('_view_admin_write01',"Administrator","password",params)


    # ------------------------------------#

    def checkRole(self):
        masDict = {}
        tc_status = None
        #---Setup for XDCR ------#
        #self._XDCR_role_test()
        #self._view_admin_role_test()
        self._raw_urllib()
        #masDict,tc_status = self.rbac._iterate_role_mapping('_replication_admin_write01',"Administrator","password",params)
        #masDict,tc_status = self.rbac._iterate_role_mapping(self.roleName,"Administrator","password")
        #self.assertTrue(tc_status,"List of permission that have failed {0}".format(masDict))






