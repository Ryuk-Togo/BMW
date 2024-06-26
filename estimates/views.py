from django.shortcuts import render, redirect
from .forms import SingleEstimateMOdelForm
from .models import Estimate


# Create your views here.
def index(request,url=None):
    if request.method == 'GET':
        estimates = Estimate.objects.filter(inspection_date__isnull=True)

        context = {
            'message' : "",
            'estimates' : estimates
        }
        return render(request, 'estimate/index.html', context)

def input(request,url=None):
    if request.method == 'GET':
        # singleEstimateMOdelForm = SingleEstimateMOdelForm()
        form = SingleEstimateMOdelForm()
        context = {
            'message' : "",
            'form' : form
        }
        return render(request, 'estimate/input.html', context)
    else:
        form = SingleEstimateMOdelForm(request.POST, request.FILES)

        if form.is_valid():
            estimate = Estimate()

            estimate.rouph_estimate_name = form.cleaned_data['rouph_estimate_name']
            estimate.rouph_estimate_files = request.FILES['rouph_estimate_files']
            estimate.save()
            return redirect('/estimate/')
        
def modify(request,id,url=None):
    if request.method == 'GET':
        if id:
            estimate_result = Estimate.objects.get(pk=id)
            form = SingleEstimateMOdelForm(instance=estimate_result)
        context = {
            'message' : "",
            'form' : form
        }
        return render(request, 'estimate/input.html', context)
    
    else:
        form = SingleEstimateMOdelForm(request.POST, request.FILES)

        if form.is_valid():
            estimate = Estimate.objects.get(pk=id)

            estimate.rouph_estimate_name = form.cleaned_data['rouph_estimate_name']
            # estimate.rouph_estimate_files = request.FILES['rouph_estimate_files']
            rouph_estimate_files = request.FILES['rouph_estimate_files']
            estimate.save()
            return redirect('/estimate/')

def delete(request,id,url=None):
    if request.method == 'GET':
        estimate = Estimate.objects.get(pk=id)
        estimate.delete()
        return redirect('/estimate/')

def _upload_file(f):
    with open('test/概算見積書/test.txt','wb+') as estimate_file:
        for chunk in f.chunks():
            estimate_file.write(chunk)
