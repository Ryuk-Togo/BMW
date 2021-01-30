from django.shortcuts import render
from bmwsys.models import MsysVal
from django.http import HttpResponse
from django.http.response import JsonResponse
import os
import glob
from mailbk.eml import MailParser

# from pysmb

# Create your views here.
def index(request,url=None):
    if request.method == 'GET':
        # メールフォルダのディレクトリを構築
        mailDir = []
        mailDir.append(
        {
            'folder' : 'mail',
            'path' : 'mail',
            'next' : getDir('mail','mail'),
        })

        mailList = []
        if url:
            # URLのスラッシュをpythonファイルパスのスラッシュに変換
            dirpath = './' + os.path.join(*url.split('\\')) + '/*.eml'
            mailFileList = glob.glob(dirpath)

            # メールファイルのリストを作成
            for email in mailFileList:
                # mailData = {}
                # try:
                #     # メールファイルを開く
                #     with open(email, mode='r', encoding='utf-8') as fin:
                #         # メールファイルのタイトルを取得する
                #         mailData = makeMailDoc(fin)
                #         fin.close()
                # except Exception as e:
                #     return HttpResponse(e)
                
                subject = ''
                try:
                    mailpas = MailParser(email)
                    mailpas.get_attr_data()
                    # return HttpResponse(result)
                    subject = mailpas.subject
                except Exception as e:
                    subject = e

                mailList.append({
                    'filename' : 'mail/' + email.replace('/','%5c'),
                    'subject' : subject,
                    # 'filePath' : url + '%5c' + email
                    # 'subject' : mailData['subject']
                })

        context = {
            'folders' : mailDir,
            'mails' : mailList,
        }
        return render(request, 'mailbk/index.html', context)

def getDir(path,folderName):

    structList = []

    for fileName in list(os.listdir(path=path)):
        dirPath = path + '/' + fileName
        if os.path.isdir(dirPath):
            struct = {
                'folder' : fileName,
                'path' : dirPath,
                'next' : getDir(dirPath,fileName),
            }
            structList.append(struct)

    return structList

def mail(request,url):
    if request.method == 'GET':
        # メールファイルを開く
        mailpas = MailParser(os.path.join(*url.split('\\')))
        try:
            mailpas.get_attr_data()
        except Exception as e:
            mailpas.subject = e
        
        # メールファイルのデータを出力
        context = {
            'subject' : mailpas.subject,
            'from' : mailpas.from_address,
            'to' : mailpas.to_address,
            'cc' : mailpas.cc_address,
            'disc' : mailpas.body.splitlines(),
            'atach' : mailpas.attach_file_list,
            'back' : url,
        }
        return render(request, 'mailbk/mail.html', context)


