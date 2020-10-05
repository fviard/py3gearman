import gearman

gm_admin_client = gearman.GearmanAdminClient(['localhost:4730'])
workers = gm_admin_client.get_workers()
print(workers)
