'''
pip3 install beautifulsoup4  # 安装bs4
pip3 install lxml  # 下载lxml解析器
'''

# 调用BeautifulSoup实例化得到一个soup对象
# 参数一: 解析文本
# 参数二:
# 参数二: 解析器（html.parser、lxml...）

from bs4 import BeautifulSoup
soup = BeautifulSoup(open('C:/Users/风吹屁屁凉/Desktop/test1.html', encoding="utf-8"), 'html.parser')

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
# print(soup.p)  # 查找第一个p标签
# print(soup.a)  # 查找第一个a标签

# 2、获取标签的名称
# print(soup.head.name)  # 获取head标签的名称

# 3、获取标签的属性
# print(soup.a.attrs)  # 获取a标签中的所有属性
# print(soup.a.attrs['href'])  # 获取a标签中的href属性

# 4、获取标签的内容
# print(soup.p.text)  # $37

# 5、嵌套选择
# print(soup.html.head)

# 6、子节点、子孙节点
# print(soup.body.children)  # body所有子节点，返回的是迭代器对象
# print(list(soup.body.children))  # 强转成列表类型
print("---------------------------------------------")
# print(soup.body.descendants)  # 子孙节点
# print(list(soup.body.descendants))  # 子孙节点
print("---------------------------------------------")
#  7、父节点、祖先节点
# print(soup.p.parent)  # 获取p标签的父亲节点
print("---------------------------------------------")
# 返回的是生成器对象
# print(soup.p.parents)  # 获取p标签所有的祖先节点
# print(list(soup.p.parents))
print("---------------------------------------------")

# 8、兄弟节点
# 找下一个兄弟
# print(soup.p.next_sibling)
print("---------------------------------------------")
# 找下面所有的兄弟，返回的是生成器
# print(soup.p.next_siblings)
# print(list(soup.p.next_siblings))
print("---------------------------------------------")

# 找上一个兄弟
# print(soup.a.previous_sibling)  # 找到第一个a标签的上一个兄弟节点
print("---------------------------------------------")
# 找到a标签上面的所有兄弟节点
# print(soup.a.previous_siblings)  # 返回的是生成器
# print(list(soup.a.previous_siblings))
print("---------------------------------------------")



'''
搜索文档树:
    find()  找一个  
    find_all()  找多个
标签查找与属性查找:
    标签:
            name 属性匹配
            attrs 属性查找匹配
            text 文本匹配
        - 字符串过滤器   
            字符串全局匹配
        - 正则过滤器
            re模块匹配
        - 列表过滤器
            列表内的数据匹配
        - bool过滤器
            True匹配
        - 方法过滤器
            用于一些要的属性以及不需要的属性查找。
    属性:
        - class_
        - id
'''

# # 字符串过滤器
# name
p_tag = soup.find(name='p')
print(p_tag)  # 根据文本p查找某个标签
print("---------------------------------------------")
# # 找到所有标签名为p的节点
tag_s1 = soup.find_all(name='p')
print(tag_s1)
print("---------------------------------------------")


# # attrs
# # 查找第一个class为sister的节点
p = soup.find(attrs={"class": "sister"})
# print(p)
# # 查找所有class为sister的节点
tag_s2 = soup.find_all(attrs={"class": "sister"})
print(tag_s2)

# text
text = soup.find(text="$37")
print(text)
#
#
# # 配合使用:
# # 找到一个id为link2、文本为Lacie的a标签
a_tag = soup.find(name="a", attrs={"id": "link2"}, text="Lacie")
print(a_tag)

# # 正则过滤器
import re

# name
p_tag = soup.find(name=re.compile('p'))
print(p_tag)

# 列表过滤器
import re

# name
tags = soup.find_all(name=['p', 'a', re.compile('html')])
print(tags)

# - bool过滤器
# True匹配
# 找到有id的p标签
p = soup.find(name='p', attrs={"id": True})
print(p)


# 方法过滤器
# 匹配标签名为a、属性有id没有class的标签
def have_id_class(tag):
    if tag.name == 'a' and tag.has_attr('id') and tag.has_attr('class'):
        return tag


tag = soup.find(name=have_id_class)
print(tag)