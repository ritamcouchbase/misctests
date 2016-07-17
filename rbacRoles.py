class rbacRoles:

    @staticmethod
    def _replication_admin_read():
        per_set = {
            "name":"Replication Admin Read",
            "permissionList1":['_get_cluster_xdcr_settings_read','_get_cluster_bucket_xdcr_read','_get_cluster_xdcr_remote_clusters_read'],
            "httpResponse1":'200',
        }
        return per_set

    @staticmethod
    def _replication_admin_write01():
        per_set = {
            "name":"Replication Admin Write",
            "permissionList1":['_get_cluster_xdcr_remote_clusters_write'],
            "httpResponse1":'200',
        }
        return per_set

    @staticmethod
    def _replication_admin_write02():
        per_set = {
            "name":"Replication Admin Write",
            "permissionList1":['_get_cluster_bucket_xdcr_write'],
            "httpResponse1":'200',
        }
        return per_set

    @staticmethod
    def _view_admin_read():
        per_set = {
            "name":"View Admin Read",
            "permissionList1":['_get_cluster_bucket_views_read'],
            "httpResponse1":'200',
        }
        return per_set

    @staticmethod
    def _view_admin_write01():
        per_set = {
            "name":"View Admin Write",
            "permissionList1":['_get_cluster_data_write'],
            "httpResponse1":'200',
        }
        return per_set