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
                    'filename' : email,
                    'subject' : subject,
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


# def makeMailDoc(mailFile):
#     result = {}

#     FROM = 'From: '
#     TO = 'To: '
#     CC = 'Cc: '
#     SUBJECT = 'Subject: '
#     CHARSET = 'Content-Type: text/plain; charset='
#     DISCRIPT = 'Content-Transfer-Encoding: ' # 後の行
#     ATACHMENT = 'Content-Disposition: ' # 添付ファイルがある事を意味し、以降が添付ファイルのバイナリデータ
#     FILE_NAME = 'Content-Disposition: attachment; filename=' # 添付ファイルの名前
#     m_from = ''
#     to = []
#     cc = []
#     subject = ''
#     chaset = ''
#     discript = []
#     atachment = []
#     isDisc = False
#     isAtach = False
    
#     for line in mailFile:

#         if FROM in line:
#             m_from = line.replace(FROM,'')

#         if TO in line:
#             to.append(line.replace(TO,''))

#         if CC in line:
#             cc.append(line.replace(CC,''))

#         if SUBJECT in line:
#             subject = line.replace(SUBJECT,'')

#         if CHARSET in line:
#             chaset = line.replace(CHARSET,'')

#         if DISCRIPT in line:
#             isDisc = True
#             isAtach = False
#         if isDisc:
#             discript.append(line)

#         # if ATACHMENT in line:
#         #     isDisc = False
#         #     isAtach = True
#         # if isAtach:
#         #     atachment.append(line)

#         # if FILE_NAME in line:
#         #     chaset = line.replace(FILE_NAME,'')
#         #     isDisc = False
#         #     # 添付ファイル
#         #     isAtach = True
#         # if isAtach:
#         #     atachment.append(line)

#     result = {
#         'charset' : chaset,
#         'from' : m_from.encode(chaset),
#         'to' : to,
#         'cc' : cc,
#         'subject' : subject.encode('shift-jis'),
#         'discript' : discript,
#         # 'atachment' : atachment,
#     }
#     return result
