from django.shortcuts import render
from django.http import HttpResponse
from kubernetes import client, config
from .pods import Pods

def index(request):
    return render(request, "web/index.html")


def get_pod_list(request):
    pods=Pods.list()
    context={"pods" : pods}
    return render(request, "pods/get_pod_list.html",context)