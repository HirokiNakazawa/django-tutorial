from django.http import HttpResponse
from django.shortcuts import render
from snippets.models import Snippet


def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request, "snippets/top.html", context)


def snippets_new(request):
    return HttpResponse('スニペットの登録')


def snippets_edit(request):
    return HttpResponse('スニペットの編集')


def snippets_detail(request):
    return HttpResponse('スニペットの詳細')
