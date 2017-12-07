from kubernetes import client, config

config.load_kube_config()


class Pods:
    def __init__(self):
        pass
        
    def list():
        v1 = client.CoreV1Api()
        ret = v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))