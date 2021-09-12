from django.shortcuts import render, redirect
from django.views import generic
# from django.http import HttpResponseRedirect

from .models import Host, Rule, Group, Client

def index(request):
    """
    Main page
    """
    hostCount = Host.objects.all().count()
    groupCount = Group.objects.all().count()
    ruleCount = Rule.objects.all().count()
    clientCount = Client.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'clientCount' : clientCount,
            'groupCount' : groupCount,
            'ruleCount' : ruleCount,
            'hostCount' : hostCount,
        }
    )

def clients(request):
    """
    Clients page
    """
    clients = Client.objects.all()
    return render(
        request,
        'clients.html',
        context={'clients': clients}
    )

def groups(request):
    """
    Groups page
    """
    groups = Group.objects.all()
    return render(
        request,
        'groups.html',
        context={'groups': groups}
    )

def group_detail(request, pk):
    # TODO
    # try:
    #     group = Group.objects.get(pk=pk)
    # except Group.DoesNotExist:
    #     raise Http404("Группы не существует")

    group = Group.objects.get(pk=pk)

    return render(
        request,
        'group_id.html',
        context={'group': group}
    )

def rules(request):
    """
    Rules page
    """
    rules = Rule.objects.all()
    return render(
        request,
        'rules.html',
        context={'rules': rules}
    )

def rule_detail(request, pk):

    rule = Rule.objects.get(pk=pk)

    return render(
        request,
        'rule_id.html',
        context={'rule': rule}
    )

def rule_create(request):
    if request.method == "GET":
        return render(
            request,
            'rule_create.html'
        )
    elif request.method == "POST":
        pass

def hosts(request):
    """
    Hosts page
    """
    hosts = Host.objects.all()
    return render(
        request,
        'hosts.html',
        context={'hosts': hosts}
    )

    