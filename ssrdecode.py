#encoding:utf-8
import base64


def base64_decode(base64_encode_str):
    """ 利用 base64.urlsafe_b64decode 对字符串解码 """
    
    if base64_encode_str:
        need_padding = len(base64_encode_str) % 4
        if need_padding != 0:
            missing_padding = 4 - need_padding
            base64_encode_str += '=' * missing_padding
        return base64.urlsafe_b64decode(base64_encode_str).decode('utf-8')
    return base64_encode_str

def parse(ssrUrl):
    """ 解析ssr链接 
    args: 
        ssrUrl: SSR 链接
    return: 
        ssr_result: SSR链接解析结果
    """

    ssr_result = {}

    decode_str = base64_decode(ssrUrl)
    parts = decode_str.split(':')
    if len(parts) != 6:
        print('不能解析SSR链接: %s' % ssrUrl)
        return
    
    server = parts[0]
    port = parts[1]
    protocol = parts[2]
    method = parts[3]
    obfs = parts[4]

    password_and_params = parts[5]
    password_and_params = password_and_params.split("/?")
    password = base64_decode(password_and_params[0])
    if len(password_and_params) == 1:
        obfsparam = ""
        protoparam = ""
        remarks = ""
        group = ""
    else:
        param_dic = {}
        param_parts = password_and_params[1].split('&')
        for part in param_parts:
            key_and_value = part.split('=')
            param_dic[key_and_value[0]] = key_and_value[1]

        obfsparam = base64_decode(param_dic.get('obfsparam', ""))
        protoparam = base64_decode(param_dic.get('protoparam', ""))
        remarks = base64_decode(param_dic.get('remarks', ""))
        group = base64_decode(param_dic.get('group', ""))
        
    ssr_result['server']=server
    ssr_result['port']=port
    ssr_result['protocol']=protocol
    ssr_result['method']=method
    ssr_result['password']=password
    ssr_result['obfs']=obfs
    ssr_result['obfsparam']=obfsparam
    ssr_result['remarks']=remarks
    ssr_result['group']=group
    ssr_result['protoparam']=protoparam

    return ssr_result


if __name__ == "__main__":
    test_ssrUrl_list = [
        "ssr://MTQ5LjEyOS4xMTEuMjE4OjU5ODE5OmF1dGhfY2hhaW5fYTpub25lOmh0dHBfc2ltcGxlOk9UVTFPRGRtWVRVLz9vYmZzcGFyYW09WW1sdVp5NWpiMjAmcmVtYXJrcz01ckM0NVlpcDVhU3A1TGlMTFRFd01qbnBwcG5tdUs5R051aUtndWVDdVMxUlVUTXlOamcyTmpZeU16QSZncm91cD1VQ0J5SUc4Z1ppQnBkQ0F1SUZBZ1lTQnlJSElnYnlCMElGTWdaU0JqSUM0Z1l5QnU"
    ]
    print("解析结果:\n*===========================*")
    for url in test_ssrUrl_list:
        ssr = parse(url[6:])
        print(' server: %s\n port: %s\n 协议: %s\n 加密方法: %s\n 密码: %s\n 混淆: %s\n 混淆参数: %s\n 协议参数: %s\n 备注: %s\n 分组: %s'
          % (ssr["server"], ssr["port"], ssr["protocol"], ssr["method"], ssr["password"], ssr["obfs"], ssr["obfsparam"], ssr["protoparam"], ssr["remarks"], ssr["group"]))
        print("*===========================*")