import quopri
import base64
import mimetypes

def decode_filename(val, charset, cte, cty):

    ret = val
    if ret.count("=?ISO-2022-JP?B?") > 0:
        ret = ret.replace("=?ISO-2022-JP?B?", "")
        ret = ret.rstrip("?=")
        # ret = base64.b64decode(ret + '=' * (-len(ret)% 4)).decode('iso-2022-jp')
        ret = base64.b64decode(ret + '=' * (-len(ret)% 4))
        # ret = decode_contentTransferType(ret + '=' * (-len(ret)% 4), cte.lower())
        ret = ret.decode('iso-2022-jp')
        ret = ret + get_contentType(cty)
    return ret

def decode_contentTransferType(val, cte, cty):

    if cte == "base64":
        ret = base64.b64decode(val)
    elif cte == "quoted-printable":
        ret = quopri.decodestring(val, header=False)
    else:
        ret = val
    return ret

def get_contentType(cty):
    extention = ""
    for contentType, contentTypeVal in mimetypes.types_map.items():
        if contentTypeVal == cty:
            extention = contentType
            break
    return extention