from django.db import models

"""
Server Group Table
"""
class ServerGroup(models.Model):
    sever_group_id = models.AutoField(auto_created=True, primary_key=True, null=False)
    group_name = models.CharField(max_length=20, blank=True, null=False)
    description = models.TextField(null=False)
    changed = models.DateTimeField(auto_now_add=True)
    changer_account = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        return '%s_%s' % (self.sever_group_id, self.group_name)

    class Meta:
        app_label = 'server'
        db_table = 'service_server_group'

"""
Service Server List
"""
class ServiceServer(models.Model):
    sever_group_id = models.ForeignKey(ServerGroup, on_delete=models.DO_NOTHING)
    server_id = models.AutoField(auto_created=True, primary_key=True, null=False)
    host_name = models.CharField(max_length=20, blank=True, null=False)
    public_ip = models.GenericIPAddressField(protocol='IPv4', null=False)
    private_ip = models.GenericIPAddressField(protocol='IPv4', null=False)
    changed = models.DateTimeField(auto_now_add=True)
    changer_account = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        return '%s_%s' % (self.server_id, self.host_name)

    class Meta:
        app_label = 'server'
        db_table = 'service_server'
