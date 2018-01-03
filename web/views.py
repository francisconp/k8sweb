from django.shortcuts import render
from django.http import HttpResponse
from kubernetes import client, config
from .pods import Pods
from .deployments import Deployments
from .namespaces import NameSpaces

def index(request):
    return render(request, "web/index.html")


def get_pod_list(request):
    pods=Pods.list()
    context={"pods" : pods}
    return render(request, "pods/get_pod_list.html",context)

def get_deploy_list(request):
    deployments=Deployments.list()
    context={"deployments" : deployments}
    return render(request, "deploy/get_deploy_list.html",context)

def get_namespace_list(request):
    namespaces=NameSpaces.list()
    context={'namespaces': namespaces}
    return render(request, "namespace/get_namespace_list.html",context)