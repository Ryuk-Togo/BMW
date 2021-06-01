from django.shortcuts import render, get_object_or_404, redirect
from bmwsys.models import MsysVal
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils import timezone
from bmw import context_processors as cnxt
from datetime import datetime

from django.contrib import auth
from todo.models import (
    TTodo,
    TDo,
    COMPLETE,
)
from todo.forms import (
    InpuDoForm,
    NowTodoModelFormSet,
    InputTodoModelFormSet,
)

# Create your views here.
# メイン画面
def index(request):
    nowTodoModelFormSet = None
    user_id = cnxt.user_info(request)['user_id']
    if request.method == 'GET':
        nowTodoModelFormSet = _get_today_todo(user_id)
    else:
        pass

    context = {
        'title':'今日も一日平和でありますように・・・',
        'message':'',
        'todo_list':nowTodoModelFormSet,
        'todo_day': timezone.now,
    }
    return render(request, 'todo/calendar.html', context) 

# DOとTODOを登録
def dotodo(request):
    nowTodoModelFormSet = None
    user_id = cnxt.user_info(request)['user_id']
    if request.method == 'GET':
        nowTodoModelFormSet = _get_today_todo(user_id)
        inpuDoForm = InpuDoForm()
        inputTodoModelFormSet = InputTodoModelFormSet()
        context = {
            'title':'今日も一日平和でありますように・・・',
            'message':'',
            'todo_list':nowTodoModelFormSet,
            'todo_day': timezone.now,
            'input_do_form':inpuDoForm, 
            'input_todo_formset':inputTodoModelFormSet, 
        }
        return render(request, 'todo/dotodo.html', context) 
    else:
        inpuDoForm = InpuDoForm(request.POST or None)
        inputTodoModelFormSet = InputTodoModelFormSet(request.POST or None)

        # Doフォーム登録
        if inpuDoForm.is_valid():

            do_id = request.POST['id']

            if do_id is None or do_id == "":
                tdo = TDo()
                tdo.complete       = '0'
                tdo.user_id        = user_id
                tdo.create_date    = datetime.now()
                tdo.create_pg_id   = 'DOTODO'
                tdo.create_user_id = user_id
            else:
                tdo = get_object_or_404(TDo,id=int(do_id))

            tdo.delivery_date  = inpuDoForm.cleaned_data['delivery_date']
            tdo.do             = inpuDoForm.cleaned_data['do']
            tdo.update_date    = datetime.now()
            tdo.update_pg_id   = 'DOTODO'
            tdo.update_user_id = user_id
            tdo.save()
        else:
            context = {
                'title':'今日も一日平和でありますように・・・',
                'message':'DO登録処理で問題がありました。',
                'todo_list':nowTodoModelFormSet,
                'todo_day': timezone.now,
                'input_do_form':inpuDoForm, 
                'input_todo_formset':inputTodoModelFormSet, 
            }
            return render(request, 'todo/dotodo.html', context) 



        # TODOフォーム登録
        if inputTodoModelFormSet.is_valid():
            for inputTodoForm in inputTodoModelFormSet:
                if inputTodoForm.is_valid():

                    todo_id = inputTodoForm.cleaned_data['id']

                    ttodo = TTodo()
                    if do_id is None or do_id == "":
                        ttodo.complete       = '0'
                        ttodo.user_id        = user_id
                        ttodo.create_date    = datetime.now()
                        ttodo.create_pg_id   = 'DOTODO'
                        ttodo.create_user_id = user_id
                    else:
                        ttodo = get_object_or_404(TTodo,id=int(todo_id))

                    ttodo.work_date = None
                    ttodo.work_time = None
                    ttodo.todo = inputTodoForm.cleaned_data['todo']
                    ttodo.do_key = tdo.id
                    ttodo.update_date    = datetime.now()
                    ttodo.update_pg_id   = 'DOTODO'
                    ttodo.update_user_id = user_id
                    ttodo.save()

        else:
            context = {
                'title':'今日も一日平和でありますように・・・',
                'message':'TODO登録処理で問題がありました。',
                'todo_list':nowTodoModelFormSet,
                'todo_day': timezone.now,
                'input_do_form':inpuDoForm, 
                'input_todo_formset':inputTodoModelFormSet, 
            }
            return render(request, 'todo/dotodo.html', context) 

        
        return redirect('/todo/dotodo/')

# １日のTODOを登録
def daytodo(request):
    nowTodoModelFormSet = None
    user_id = cnxt.user_info(request)['user_id']
    if request.method == 'GET':
        nowTodoModelFormSet = _get_today_todo(user_id)
    else:
        pass
    context = {
        'title':'今日も一日平和でありますように・・・',
        'message':'',
        'todo_list':nowTodoModelFormSet,
        'todo_day': timezone.now,
    }
    return render(request, 'todo/daytodo.html', context) 

# DOとTODOの一覧を表示
def todoval(request):
    user_id = cnxt.user_info(request)['user_id']
    if request.method == 'GET':
        do_todo_list = _get_todo_val(user_id)
        return HttpResponse(do_todo_list)


# ユーザ情報を検索する
def _get_user_info(user_id):
    authUserModel = auth.get_user_model()
    admin_uers = authUserModel.fiiller(username=user_id)
    users = []
    for admin_user in admin_uers:
        users.append(admin_user)
    
    return users

# 日付でtodoを取得
def _get_todo_by_day(user_id, work_date_today):
    # todos = TTodo.objects.filter(work_date=work_date).filter(user_id=user_id).order_by('work_time')
    todos = TTodo.objects.filter(user_id=user_id).filter(work_date__isnull=False).filter(work_date=work_date_today).order_by('work_time')
    todos = TTodo.objects.filter(user_id=user_id,work_date=work_date_today)
    return todos

# TODO未完了を取得
def _get_no_complete_todos(dokey):
    todos = TTodo.objects.filter(dokey=dokey).filter(compile=COMPLETE.未完了).order_by('work_time')
    return todos

# カレンダ用DO取得
def _get_do_delevery_date(delivery_date):
    dos = TDo.objects.filter(delivery_date=delivery_date)
    return dos

# DOからtODOを取得
def _get_todo_by_do(do):
    todos = TDo.objects.filter(dokey=do.dokey).order_by('work_time')
    return todos

def _get_today_todo(user_id):
    todo_data = _get_todo_by_day(user_id,datetime.now())
    today_todo = []
    for todo in todo_data:
        today_todo.append({
            'work_time':todo.work_time,
            'todo'     :todo.todo,
            'complete' :todo.complete,
        })
        
    return NowTodoModelFormSet(initial=today_todo)

def _get_todo_val(user_id):
    do_list = TDo.objects.filter(user_id=user_id, complete='9').order_by('delevery_date')
    do_todo_list = []
    for do_data in do_list:
        todo_list = _get_todo_by_do(do_data.do_key)
        do_todo_list.append({
            'do': do_data,
            'todo': todo_list,
        })

    return do_todo_list