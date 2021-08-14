from django.http import HttpResponse


def top(request):
    return HttpResponse(b"Hello World")


def snippets_new(request):
    return HttpResponse('スニペットの登録')


def snippets_edit(request):
    return HttpResponse('スニペットの編集')


def snippets_detail(request):
    return HttpResponse('スニペットの詳細')
