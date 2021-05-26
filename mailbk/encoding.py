import quopri
import base64
import mimetypes

def decode_filename(val, charset, cte, cty):

    # ret = val
    ret = decode_contentTransferType(val, cte, cty)
    if ret.upper().count("=?ISO-2022-JP?B?") > 0:
        try:
            ret = ret.upper().replace("=?ISO-2022-JP?B?", "")
            ret = ret.rstrip("?=")
            ret = base64.b64decode(ret + '=' * (-len(ret)% 4))
            ret = ret.decode('iso-2022-jp')
            ret = ret + get_contentType(cty)
        except:
            if charset == "utf-8":
                ret = ret.decode('utf-8', "ignore")
            else:
                ret = ret.decode("ascii", "ignore")
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