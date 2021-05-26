from todo.models import COMPLETE
from django.shortcuts import render
from django.contrib import auth
from todo.modules import (
    TTodo,
    TDo,
)


# Create your views here.




# ユーザ情報を検索する
def _get_user_info(user_id):
    authUserModel = auth.get_user_model()
    admin_uers = authUserModel.fiiller(username=user_id)
    users = []
    for admin_user in admin_uers:
        users.append(admin_user)
    
    return users

# 日付でtodoを取得
def _get_todo_by_day(user_id, work_date):
    todos = TTodo.object.filter(work_date=work_date).filter(user_id=user_id).order_by('work_time')
    return todos

# TODO未完了を取得
def _get_no_complete_todos(dokey):
    todos = TTodo.object.filter(dokey=dokey).filter(compile=COMPLETE.未完了).order_by('work_time')
    return todos

# カレンダ用DO取得
def _get_do_delevery_date(delivery_date):
    dos = TDo.object.filter(delivery_date=delivery_date)
    return dos

# DOからtODOを取得
def _get_todo_by_do(do):
    todos = TDo.object.filter(dokey=do.dokey).order_by('work_time')
    return todos

