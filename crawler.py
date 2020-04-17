# -*- coding: utf-8 -*-
# author = 'dingzr'
import urllib

import bs4
import requests
from bs4 import BeautifulSoup

# http://kaijiang.zhcw.com/zhcw/html/ssq/list_11.html

# http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum=20



# site = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_11.html"
# html = urllib.request.urlopen(site)
# soup =bs4.BeautifulSoup(html)
# print(soup.prettify())

soup = BeautifulSoup(open('C:/Users/风吹屁屁凉/Desktop/test.html', encoding="utf-8"), 'html.parser')
# print(soup.prettify())

'''
遍历文档树：
    1、直接使用
    2、获取标签的名称
    3、获取标签的属性
    4、获取标签的内容
    5、嵌套选择
    6、子节点、子孙节点
    7、父节点、祖先节点
    8、兄弟节点
'''

# 1、直接使用
# print(soup.td)  # 查找第一个p标签

# 2、获取标签的名称
# print(soup.td.name)  # 获取td标签的名称

# 3、获取标签的属性
# print(soup.td.attrs)  # 获取td标签中的所有属性
# print(soup.td.attrs['align'])  # 获取td标签中的align属性

# 4、获取标签的内容
# print(soup.td.text)  # $37

# 5、嵌套选择
# print(soup.html.head)

# 6、子节点、子孙节点
# print(soup.td.children)  # body所有子节点，返回的是迭代器对象
# print(list(soup.td.children))  # 强转成列表类型

# print(soup.body.descendants)  # 子孙节点
# print(list(soup.tbody.descendants))  # 子孙节点

#  7、父节点、祖先节点
# print(soup.p.parent)  # 获取p标签的父亲节点
# 返回的是生成器对象
# print(soup.p.parents)  # 获取p标签所有的祖先节点
# print(list(soup.p.parents))

# 8、兄弟节点
# 找下一个兄弟
# print(soup.td.next_sibling)
# 找下面所有的兄弟，返回的是生成器
# print(soup.p.next_siblings)
# print(list(soup.td.next_siblings))

# 找上一个兄弟
# print(soup.a.previous_sibling)  # 找到第一个a标签的上一个兄弟节点
# 找到a标签上面的所有兄弟节点
# print(soup.a.previous_siblings)  # 返回的是生成器
# print(list(soup.a.previous_siblings))

# tag_s1 = soup.find_all(name='td')
# print(tag_s1)

tag_s1 = soup.find_all(name='tr')
# print(tag_s1)

# print(list(soup.find_all(name='tr')))

for child in tag_s1:
    # print(child)
    # print(child.find_all(name='td'))
    print("------------")
    num = child.find_all(name='td', attrs={"align": "center"})

    for child1 in num:
        print(child1.text.string)
        print(child1.find_all(name='em'))
        # num2 = child1.find_all(name='em')
        # for child2 in num2:
        #     print(child2.em.text)

