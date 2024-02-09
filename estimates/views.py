from django.shortcuts import render
from .forms import SingleEstimateMOdelForm
from .models import Estimate


# Create your views here.
def index(request,url=None):
    if request.method == 'GET':
        context = {}
        return render(request, 'estimate/index.html', context)

def input(request,url=None):
    if request.method == 'GET':
        # singleEstimateMOdelForm = SingleEstimateMOdelForm()
        form = SingleEstimateMOdelForm()
        context = {
            'form' : form
        }
        return render(request, 'estimate/input.html', context)
