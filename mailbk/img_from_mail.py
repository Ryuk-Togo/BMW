 #!python

'''to save all attached image files in a mailbox'''


import imaplib, email.parser, email.header, os, os.path

HOST='mail.a.org'
USER='x'
PW='q1!!!'

MBOX='INBOX'

IMG_DIR = 'img'

class MailLoad(object):
    
    subject = None
    receive_date = None
    to_address = None
    cc_address = None
    from_address = None
    body = []
    attach_file_list = []

    def __init__(self, mail_file_path):
        self.mail_file_path = mail_file_path
        # emlファイルからemail.message.Messageインスタンスの取得
        try:
            with open(mail_file_path, 'rb') as email_file:
                self.email_message = email.message_from_bytes(email_file.read())
        except Exception as e:
            print(e)
        
        print(self.email_message)
        self.subject = None
        self.to_address = None
        self.cc_address = None
        self.from_address = None
        self.receive_date = None
        self.body = ""
        # 添付ファイル関連の情報

        # {name: file_name, data: data}
        self.attach_file_list = []

        self.subject = self._get_decoded_header("Subject")
        self.receive_date = self._get_decoded_header("Date")
        self.to_address = self._get_decoded_header("To")
        self.cc_address = self._get_decoded_header("Cc")
        self.from_address = self._get_decoded_header("From")



    def _get_decoded_header(self, key_name):
        """
        ヘッダーオブジェクトからデコード済の結果を取得する
        """
        # 該当項目がないkeyは空文字を戻す
        raw_obj = self.email_message.get(key_name)
        print(key_name)
        print(raw_obj)

        if raw_obj is None:
            return ""
