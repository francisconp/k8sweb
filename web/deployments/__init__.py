from kubernetes import client, config

config.load_kube_config()

class Deployments:
    def __init__(self):
        pass

    def list(self):
        v1 = client.AppsV1beta1Api()
        ret = v1.list_deployment_for_all_namespaces(watch=False)
        return ret.items