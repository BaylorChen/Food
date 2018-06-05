__author__ = 'chenjianguo'
# -*- coding:utf-8 -*-

from pyquery import PyQuery


def parse(response):
    """
    抓取美食tab 列表： https://www.meishij.net/chufang/diy/
    返回列 大 tab 信息
    :param:response
    :return
    """
    jpy = PyQuery(response.text)

    tr_list = jpy('#listnav_ul > li').items()

    result = set()  #result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr('a').attr('href')  #爬取各个小区的url
        if  url and 'https://www.meishij.net' not in url:
            url = 'https://www.meishij.net' + url
        result.add(url)
    return result

def Home_cooking(response):
    '''
    家常菜的小tab列表 家常菜的页面元素与其他大tab 不一样需要特殊处理 https://www.meishij.net/chufang/diy/
    返回小tab 列表信息
    :param response:
    :return:
    '''
    jpy = PyQuery(response.text)
    tr_list = jpy('#listnav_con_c > dl.listnav_dl_style1.w990.bb1.clearfix > dd').items()
    result = set()  # result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr('a').attr('href')  #爬取各个小区的url
        result.add(url)
    return result

def othe_cooking(response):
    '''
    其他菜的小tab列表  https://www.meishij.net/china-food/caixi/
    返回小tab 列表信息
    :param response:
    :return:
    '''
    jpy = PyQuery(response.text)
    tr_list = jpy('#listnav > div > dl > dd').items()
    result = set()  # result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr('a').attr('href')  #爬取各个小区的url
        result.add(url)
    return result


def Dishes(response):
    '''
    菜品列表  https://www.meishij.net/chufang/diy/jiangchangcaipu/
    返回菜品信息
    :param response:
    :return:
    '''
    jpy = PyQuery(response.text)
    tr_list = jpy('#listtyle1_list > div').items()
    result = set()  # result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr('a').attr('href')  #爬取各个小区的url
        result.add(url)
    print(result,len(result))
    return result

def Dishes_Details(response):
    '''
    菜品的详细信息 https://www.meishij.net/zuofa/nanguaputaoganfagao_2.html
    返回 主要就是菜名、图片、用料、做法
    :param response:
    :return:
    '''
    jpy = PyQuery(response.text)
    result = dict()  # result为set集合（不允许重复元素）
    result['img'] =jpy('body > div.main_w.clearfix > div.main.clearfix > div.cp_header.clearfix > div.cp_headerimg_w > img').attr('src')
    result['name']=jpy('#tongji_title').text()
    # result['']=jpy('')
    # result['']=jpy('')
    # result['']=jpy('')
    print(result, len(result))
    return result


if __name__ == '__main__':
    import requests
    r = requests.get('https://www.meishij.net/zuofa/nanguaputaoganfagao_2.html')
    Dishes_Details(r)
