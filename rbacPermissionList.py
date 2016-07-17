class rbacPermissionList:

    bucket_name = 'default'
    node_id = "ns_1@192.168.46.101"

    @staticmethod
    def _get_cluster_admin_internal():
        _cluster_admin_internal = {
            "cbauth":"/_cbauth;POST",
            "log":"/_log:POST",
            "regexpValidation":"/_goxdcr/regexpValidation;POST",
            "GetMeatkv":"/_metakv;GET",
            "PutMeatkv":"/_metakv;PUT",
            "DelMetakv":"/metavk;DELETE"
            #RPCONNECT
        }
        return _cluster_admin_internal

    @staticmethod
    def _get_cluster_admin_diag_read():
        _cluster_admin_diag_read = {
            "getDiag":"/diag;GET",
            #"getDiagVbuckets":"/diag/vbuckets:GET",
            "getDiagAle":"/diag/ale;GET",
            #"getDiagMasterEvents":"/diag/masterEvents:GET",
        }
        return _cluster_admin_diag_read

    @staticmethod
    def _get_cluster_admin_diag_write():
        _cluster_admin_diag_write = {
            "eval":"/diag;POST"
        }
        return _cluster_admin_diag_write


    @staticmethod
    def _get_cluster_admin_setup_write():
        _cluster_admin_setup_write = {
            "engageCluster":"/engageCluster2;POST",
            "completeJoin":"/completeJoin;POST",
            "doJoinCluster":"/node/controller/doJoinCluster;POST",
            "doJoinClusterV2":"/node/controller/doJoinClusterV2;POST",
            "rename":"/node/controller/rename:POST",
            "settings":"POST /nodes/<node>/controller/settings;POST",
            "setupServices":"/node/controller/setupServices;POST",
            "settings":"/settings/web;POST"
        }
        return _cluster_admin_setup_write


    @staticmethod
    def _get_cluster_pools_read():
        _cluster_pools_read = {
            "Pools":"/pools;GET",
            "PoolsDefault":"/pools/default;GET",
            #"poolsStreaming":"/poolsStreaming/default:GET"
            "poolsNode":"/pools/nodes;GET",
            "nodeServices":"/pools/default/nodeServices;GET",
            "nodeServiceStreaming":"/pools/default/nodeServicesStreaming;GET"
        }
        return _cluster_pools_read



    @staticmethod
    def _get_cluster_nodes_read():
        _cluster_nodes_read = {
            "pools_nodeStatus":"/nodeStatuses;GET",
            "pools_nodes":"/nodes/"+node_id+";GET",
        }
        return _cluster_nodes_read

    @staticmethod
    def _get_cluster_sample_read():
        _cluster_sample_read = {
            "getSampleBuckets":"/sampleBuckets:GET"
        }
        return _cluster_sample_read


    @staticmethod
    def _get_cluster_settings_read():
        _cluster_settings_read = {
            "settingsWeb":"/settings/web;GET",
            "settingsAlert":"/settings/alerts;GET",
            "settingsStat":"/settings/stats;GET",
            "settingsAutoFailover":"/settings/autoFailover;GET",
            "settingsAutoCompaction":"/settings/autoCompaction;GET"
        }
        return _cluster_settings_read

    @staticmethod
    def _get_cluster_admin_memcached_read():
        _cluster_admin_memcached_read = {
            "settingsMemcached":"/pools/default/settings/memcached/global;GET",
            "settingsMemcached":"/pools/default/settings/memcached/effective/<node>;GET",
            "settingsMemcachedNode":"/pools/default/settings/memcached/node/<node>;GET",
            "settingsMemcacheSetting":"/pools/default/settings/memcached/node/<node>/setting/<name>;GET",
            "settingsInternal":"/internalSettings;GET"
        }
        return _cluster_admin_memcached_read



    @staticmethod
    def _get_cluster_tasks_read():
        _cluster_tasks_read = {
            "TasksRebalanceProg":"/pools/default/rebalanceProgress;GET",
            "Tasks":"/pools/default/tasks;GET"
        }
        return _cluster_tasks_read

    @staticmethod
    def _get_cluster_pools_write():
        _cluster_pools_write = {
            "poolsDefault":"/pools/default;POST"
        }
        return _cluster_pools_write

    @staticmethod
    def _get_cluster_settings_write():
        _cluster_settings_write = {
            "alertsWrite":"/settings/alerts:POST",
            "testEmailWrite":"/settings/alerts/testEmail;POST",
            #POST /settings/stats (enable sending stats to remote server) is it even used?
            "autoFailoverWrite":"/settings/autoFailover;POST",
            "resetCountWrite":"/settings/autoFailover/resetCount;POST",
            "autoCompactionWrite":"/controller/setAutoCompaction;POST",
            "resetAlerts":"/controller/resetAlerts;POST"
        }
        return _cluster_settings_write


    @staticmethod
    def _get_cluster_admin_memcached_write():
        _cluster_admin_memcached_write = {
            "settingsMemcachedWrite":"/pools/default/settings/memcached/global;POST",
            "settingsMemcachedWrite":"/pools/default/settings/memcached/effective/<node>;POST",
            "settingsMemcachedNodeWrite":"/pools/default/settings/memcached/node/<node>;POST",
            "settingsMemcacheSettingWrite":"/pools/default/settings/memcached/node/<node>/setting/<name>;POST",
            "settingsInternalWrite":"/internalSettings;GET"
        }
        return _cluster_admin_memcached_read


    @staticmethod
    def _get_cluster_nodes_write():
        _cluster_nodes_write = {
            "ejectNode":"/controller/ejectNode;POST",
            "addNode":"/controller/addNode;POST",
            "addNodeV2":"/controller/addNodeV2;POST",
            "uuidAddNode":"pools/default/serverGroups/<uuid>/addNode;POST",
            "uiidAddNodev1":"/pools/default/serverGroups/<uuid>/addNodeV2;POST",
            "failover":"/controller/failOver;POST",
            "graceFullFailover":"/controller/startGracefulFailover;POST",
            "rebalance":"/controller/rebalance;POST",
            "reAddNode":"/controller/reAddNode;POST",
            "reFailover":"/controller/reFailOver;POST",
            "stopRebalance":"/controller/stopRebalance;POST",
            "setRecoveryType":"/controller/setRecoveryType;POST"
        }
        return _cluster_nodes_write

    @staticmethod
    def _get_cluster_bucket_all_create():
        _cluster_bucket_all_create = {
            "sampleInstall":"/sampleBuckets/install;POST",
            "Buckets":"/pools/default/buckets;POST"
        }
        return _cluster_bucket_all_create


    @staticmethod
    def _get_cluster_bucket_settings_read(bucket='default'):
        _cluster_bucket_settings_read = {
            "default":"/pools/default/b/<bucket-name>;GET",
            #"defaultBS":"/pools/default/bs/" + bucket + ":GET",
            "bucketNodes":"/pools/default/buckets/<bucket-name>/nodes;GET",
            "bucketNodeID":"/pools/default/buckets/<bucket-name>/nodes/<node_id>:8091;GET",
            "bucketDot":"/dot/<bucket-name>;GET",
            "bucketsvg":"/dotsvg/<bucket-name>;GET",
            "bucketPools":"/pools/default/buckets;GET",
            #"bucketName":"/pools/default/buckets/" + bucket + ":GET",
            #"bucketStreaming":"/pools/default/bucketsStreaming/" + bucket + ":GET"
        }
        return _cluster_bucket_settings_read


    @staticmethod
    def _get_cluster_recovery_read(bucket='default'):
        _cluster_recovery_read = {
            "recoverStatus":"/pools/default/buckets/<name>/recoveryStatus;GET"
        }
        return _cluster_recovery_read

    @staticmethod
    def _get_cluster_bucket_settings_write():
        _cluster_bucket_settings_write ={
            "bucketSettingsWrite":"/pools/default/buckets/<bucket_name>;POST"
        }
        return _cluster_bucket_settings_write


    @staticmethod

    @staticmethod
    def _get_cluster_stats_read():
        _cluster_stats_read = {
            "overviewStats":"/pools/default/overviewStats;GET",
            "statsDirectory":"/pools/default/buckets/<name>/statsDirectory;GET",
            "queryStats":"/pools/default/buckets/@query/stats;GET",
            "XDCRStats":"/pools/default/buckets/@xdcr-<bucket_name>/stats;GET",
            "IndexStats":"/pools/default/buckets/@index-<bucket_name>/stats;GET",
            "QueryStats":"/pools/default/buckets/@query/nodes/<node_id>/stats;GET",
            "XDCRNodeStats":"/pools/default/buckets/@xdcr-<bucket_name>/nodes/<node_id>/stats;GET",
            "IndexNodeStats":"/pools/default/buckets/@index-<bucket_name>/nodes/<node_id>/stats;GET",
            "BucketStats":"/pools/default/buckets/<bucket_name>/stats/sample;GET",
            "UIStats":"/_uistats;GET",
            "BucketStats":"/pools/default/buckets/<name>/stats;GET",
            "BucketNodeStats":"/pools/default/buckets/<bucket_name>/nodes/<node_id>:8091/stats;GET"
        }
        return _cluster_stats_read



    #XDCR Settings Permission List#

    @staticmethod
    def _get_cluster_xdcr_settings_read():
        _cluster_xdcr_settings_read = {
            "xdcrSettingsRead":"/settings/replications;GET"
        }
        return _cluster_xdcr_settings_read

    @staticmethod
    def _get_cluster_xdcr_settings_write():
        _cluster_xdcr_settings_write = {
            "xdcrSettingsWrite":"/settings/replications;POST"
        }
        return _cluster_xdcr_settings_write

    @staticmethod
    def _get_cluster_bucket_xdcr_read():
        _cluster_bucket_xdcr_read = {
            "xdcrBucketRead":"settings/replications/<replication_id>;GET"
        }
        return _cluster_bucket_xdcr_read


    @staticmethod
    def _get_cluster_bucket_xdcr_write():
        _cluster_bucket_xdcr_write = {
            "createReplication":"controller/createReplication;POST;create_replication",
            "cancelXDCR":"controller/cancelXDCR/<replication_id>;POST",
        }
        return _cluster_bucket_xdcr_write

    @staticmethod
    def _get_cluster_xdcr_remote_clusters_read():
        _cluster_xdcrremote_clusters_read = {
            "remoteClusters":"/pools/default/remoteClusters;GET"
        }
        return _cluster_xdcrremote_clusters_read

    @staticmethod
    def _get_cluster_xdcr_remote_clusters_write():
        _cluster_xdcr_remote_clusters_write = {
            #"remoteClusterID":"/pools/default/remoteClusters/<id>;POST",
            "remoteClusterDelete":"pools/default/remoteClusters/<remote_cluster_name>;DELETE",
            "remoteCluster":"pools/default/remoteClusters;POST;remoteCluster01"
        }
        return _cluster_xdcr_remote_clusters_write

    @staticmethod
    def _get_cluster_bucket_views_read():
        _cluster_bucket_views_read = {
            "getddocs":"/pools/default/buckets/<bucket_name>/ddocs;GET"
        }
        return _cluster_bucket_views_read

    @staticmethod
    def _get_cluster_bucket_views_compact():
        _cluster_bucket_views_compact = {
            "compactView":"/pools/default/buckets/<bucket_name>/ddocs/<doc_id>/controller/compactView;POST",
            "cancelViewCompaction":"/pools/default/buckets/<bucket_name>/ddocs/<doc_id>/controller/cancelViewCompaction;POST"
        }
        return _cluster_bucket_views_compact


    @staticmethod
    def _get_cluster_bucket_views_write():
        _cluster_bucket_views_write = {
            "setUpdateMinChanges":"/pools/default/buckets/<bucket_name>/ddocs/<doc_id>/controller/setUpdateMinChanges;POST"
        }
        return _cluster_bucket_views_write

    @staticmethod
    def _get_cluster_data_write():
        _cluster_data_write = {
            "createView":"/pools/default/buckets/<bucket_name>/docs/<doc_id>;POST",
            #"deleteView":"/<bucket_name>/<doc_id>;DELETE"
        }
        return _cluster_data_write

