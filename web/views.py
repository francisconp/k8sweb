from django.shortcuts import render
from django.http import HttpResponse
from kubernetes import client, config


def index(request):
    return render(request, "web/index.html")


def get_pods(request)
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))