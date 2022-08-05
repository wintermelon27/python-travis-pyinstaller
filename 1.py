# -*- coding: utf-8 -*-
import sys
import urllib
import urlparse


# 精简参数
def beauty(web_url):
    query = dict(urlparse.parse_qs(urlparse.urlsplit(web_url).query))
    web_url_str = str(web_url)
    split_idx = web_url_str.find('?')
    res = web_url_str[0:split_idx]
    c = 0
    for (k, v) in query.items():
        str_k = str(k)
        if str_k.startswith('refer') or str_k.startswith('ref') or str_k.startswith('_') or str_k.startswith('__'):
            continue
        if c == 0:
            res += '?' + str_k + '=' + str(v).replace('[', '').replace(']', '').replace('\'', '')
        else:
            res += '&' + str_k + '=' + str(v).replace('[', '').replace(']', '').replace('\'', '')
        c += 1
    return res


def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    print('******小程序活动页精简******')
    print('1、小程序活动页路径精简, eg: package_c/web/index?src=xxx')
    print('2、原始活动页精简，组装成小程序路径, eg: https://mobile.yangkeduo.com/promotion_op.html?xxx')
    print('3、原始活动页精简, eg: https://mobile.yangkeduo.com/promotion_op.html?xxx')
    while True:
        print('输入想要使用的功能(输入1/2/3):')
        op = raw_input()
        if op == '1':
            print('输入需要精简的小程序活动页路径:')
            input_path = raw_input()
            if input_path.find('package_c/web/index?') == -1 or input_path.find('src=') == -1:
                print('输入错误!!!')
                continue
            input_path_query = dict(urlparse.parse_qs(urlparse.urlsplit(input_path).query))
            input_path_src = str(input_path_query['src'])[2:]
            print('处理结果:')
            try:
                print('package_c/web/index?src=' + urllib.quote(beauty(input_path_src))
                      + '&_ex_src=vip_gmv&_ex_campaign=script_tool&_ex_sid=manual')
            except:
                print('输入有误!!!')
        elif op == '2':
            print('输入原始活动页:')
            input_url = raw_input()
            print('处理结果:')
            try:
                print('package_c/web/index?src=' + urllib.quote(beauty(input_url))
                      + '&_ex_src=vip_gmv&_ex_campaign=script_tool&_ex_sid=manual')
            except:
                print('输入有误!!!')
        elif op == '3':
            print('输入原始活动页:')
            input_url = raw_input()
            print('处理结果:')
            try:
                print(beauty(input_url) + '&_ex_src=vip_gmv&_ex_campaign=script_tool&_ex_sid=manual')
            except:
                print('输入有误!!!')
        else:
            print('选择有误，请重新输入')


if __name__ == "__main__":
    main()
