from django.shortcuts import render, get_object_or_404
from bmwsys.models import MsysVal
from .models import TmpFile
from .forms import TmpFileModelFormSet
from django.http import HttpResponse
from django.http.response import JsonResponse
import os
import glob
from mailbk.eml import MailParser
# from pathlib import Path
import mimetypes
import shutil
from  mailbk import encoding

# from pysmb

# Create your views here.
def index(request,url=None):
    if request.method == 'GET':
        # メールフォルダのディレクトリを構築
        mailDir = []
        mailDir.append(
        {
            'folder' : 'mail',
            'path' : 'maild',
            'next' : _getDir('mail','mail'),
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

def mail(request,url):
    if request.method == 'GET':
        # メールファイルを開く
        mailpas = MailParser(os.path.join(*url.split('\\')))
        try:
            mailpas.get_attr_data()
        except Exception as e:
            mailpas.subject = e

        dirpath = os.path.dirname(os.path.join(*url.split('\\')))
        # for attachFile in mailpas.attach_file_list:
        #     return HttpResponse(encoding.check_encoding(attachFile["path"]))
        attachFileList = _getAttachFileList(mailpas.attach_file_list, dirpath)

        # メールファイルのデータを出力
        # for attach in attachFileList:
        #     ret = encoding.decode_filename(attach['name'])
        #     return HttpResponse(ret)
    
        context = {
            'subject' : mailpas.subject,
            'from' : mailpas.from_address,
            'to' : mailpas.to_address,
            'cc' : mailpas.cc_address,
            'disc' : mailpas.body.splitlines(),
            'attach' : attachFileList,
            # 'attach' : mailpas.attach_file_list,
            'back' : url,
        }
        return render(request, 'mailbk/mail.html', context)

def download(request,url):
    if request.method == 'GET':
        # メールファイルを開く
        tempFilePath = os.path.join(*url.split('\\'))
        tempFileName = url.split('\\')[-1]
        tempFile = None

        # 添付ファイルを開く
        try:
            with open(tempFilePath, 'rb') as tempFileReader:
                tempFile = tempFileReader.read()
        except Exception as e:
            tempFile = e

        # ファイル名からmimetypeを推測。拡張子がないファイル等は、application/octet-stream
        response = HttpResponse(tempFile,content_type=mimetypes.guess_type(tempFilePath) or 'application/octet-stream')

        # Content-Dispositionでダウンロードの強制
        response['Content-Disposition'] = 'filename=%s' % tempFileName
        return response

def _getDir(path,folderName):
    
    structList = []

    for fileName in list(os.listdir(path=path)):
        dirPath = path + '/' + fileName
        if os.path.isdir(dirPath):
            struct = {
                'folder' : fileName,
                'path' : dirPath,
                'next' : _getDir(dirPath,fileName),
            }
            structList.append(struct)

    return structList

def _getAttachList(attachFile,path):

    if type(decode_header(attachFile["name"])[0][0]) == bytes:
        file_name = path + decode_header(attachFile["name"])[0][0].decode(decode_header(attachFile["name"])[0][1])
    else:
        file_name = path + decode_header(attachFile["name"])[0][0]

    with open(path + file_name,mode="bw") as f:
        f.write(attachFile["data"])

def _getAttachFileList(attachFileList, url):
    
    attachFileNameList = []

    for attachFile in attachFileList:
        with open(url + '/' + attachFile["name"],mode="bw") as f:
            f.write(attachFile["data"])

        attachFileName = {
            'path' : url.replace('/','%5c') + '%5c' + attachFile["name"],
            'name' : attachFile["name"],
        }
        attachFileNameList.append(attachFileName)

    return attachFileNameList

# def _getAttachFileList(attachFileList, request):
    
#     tmpFiles = []

#     for attachFile in attachFileList:
#         # tmpFile = get_object_or_404(TmpFile)
#         tmpFile = TmpFile()
#         tmpFile.fileName = attachFile["name"]
#         tmpFile.attach = attachFile["data"]
#         tmpFile.save()
#         tmpFiles.append(tmpFile)

#         # initial = {
#         #     'fileName' : attachFile["name"],
#         #     'attach' : attachFile["data"],
#         # }
#         # tmpFiles.append(initial)


#     # return TmpFileModelFormSet(files=request.FILES or None, initial=tmpFiles)
#     return tmpFiles
