__author__ = 'chenjianguo'
# -*- coding:utf-8 -*-

from pyquery import PyQuery
import re


def parse(response):
    """
    抓取美食tab 列表： https://www.meishij.net/chufang/diy/
    返回列 大 tab 信息
    :param:response
    :return
    """
    jpy = PyQuery(response.text)

    tr_list = jpy('#listnav_ul > li').items()

    result = dict()  #result为set集合（不允许重复元素）
    for tr in tr_list:

        url = tr('a').attr('href')  #爬取美食tab的url
        text = tr('a').text()
        if url and 'https://www.meishij.net' not in url:
            url = 'https://www.meishij.net' + url
        if url and 'shicai' not in url and 'pengren' not in url:
            result[text]=url
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
    result = dict()  # result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr('a').attr('href')  #爬取家常菜小 tab的url
        text = tr('a').text()
        result[text] = url
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
    result = dict()  # result为set集合（不允许重复元素）
    for tr in tr_list:
        url = tr('a').attr('href')  # 爬取家常菜小 tab的url
        text = tr('a').text()
        result[text] = url
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
        url = tr('a').attr('href')  #爬取菜品的url
        result.add(url)
    # print(result,len(result))
    return result

def Dishes_Details(response):
    '''
    菜品的详细信息 https://www.meishij.net/zuofa/nanguaputaoganfagao_2.html
    返回 主要就是菜名、图片、用料、做法
    :param response:
    :return:
    '''

    jpy = PyQuery(response.text)
    result = {'用料':{},'统计':{},'做法':{}}

    result['主图'] =jpy('body > div.main_w.clearfix > div.main.clearfix > div.cp_header.clearfix > div.cp_headerimg_w > img').attr('src')
    result['菜名']=jpy('#tongji_title').text()

    tongji = jpy('body > div.main_w.clearfix > div.main.clearfix > div.cp_header.clearfix > div.cp_main_info_w > div.info2 > ul > li').items()
    for i in tongji:
        result['统计'][i('strong').text()]=i('a').text()
    
    Material = jpy('body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.materials > div > div.yl.zl.clearfix > ul').items()
    temp,tag = '',''
    for i in Material:
        temp =(i('li > div > h4 > a').text()).replace(' ','#').split('#')
        tag = (i('li > div > h4 > span').text()).replace(' ','#').split('#')
    for k,v in enumerate(temp):
        result['用料'][v]=tag[k]
    k = jpy('body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.materials > div > div.yl.fuliao.clearfix > ul > li > h4 > a').text()
    v = jpy('body > div.main_w.clearfix > div.main.clearfix > div.cp_body.clearfix > div.cp_body_left > div.materials > div > div.yl.fuliao.clearfix > ul > li > span').text()
    result['用料'][k]=[v]

    #Practice = jpy('div.measure > div > p').items() or jpy('div.measure > div > div > em').items()

    Practice = jpy("em.step").items()
    text =[]
    count =1
    for i in Practice:
        if i.parent().is_("div"):
            text = i.text() + i.parent()("p").text()
            img = (i.parent()('img').attr('src'))
            # result['做法'][text] = img
            result['做法']['step_'+str(count)] = [text,img]
            count +=1

        elif i.parent().is_("p"):
            text =i.parent()("p").text()
            img =(i.parent().parent()('p')('img').attr('src'))
            # result['做法'][text] = img
            result['做法']['step_' + str(count)] = [text, img]
            count += 1
        else:
            pass
    # print(result, len(result))
    return result


if __name__ == '__main__':
    import requests
    # r = requests.get('https://www.meishij.net/zuofa/youmenchunsun_15.html')
    r = requests.get('https://www.meishij.net/zuofa/nanguaputaoganfagao_2.html')
    Dishes_Details(r)

