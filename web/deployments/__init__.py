from kubernetes import client, config

config.load_kube_config()

class Deployments:
    def __init__(self):
        pass

    def list():
        v1 = client.AppsV1beta1Api()
        ret = v1.list_deployment_for_all_namespaces(watch=False)
        print(ret)
        return ret.items