_user_id = 't_iwamoto'
_user_name = 'テスト'

# グローバル変数として取得
def user_info(request):
    return {
        'user_id'  : _user_id,
        'user_name': _user_name,
    }

# グローバル変数をセットする
def set_user_info(user_id, user_name, self):
    _user_id = user_id
    _user_name = user_name
