from kubernetes import client, config

config.load_kube_config()

class NameSpaces:
    def __init__(self):
        pass

    def list():
        v1 = client.CoreV1Api()
        ret = v1.list_namespace(watch=False)
        return ret.items