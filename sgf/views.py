from django.shortcuts import render

# Create your views here.
def index(request,url=None):
    if request.method == 'GET':
        branches = None
        context = {
            'message' : "",
            'branches' : branches
        }
        return render(request, 'sgf/index.html', context)
