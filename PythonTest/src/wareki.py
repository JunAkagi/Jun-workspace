# coding:utf-8
'''
Created on 2016/03/01

@author: JUN_AKAGI
'''
import sys
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)


year = int(input(u"西暦："))

if year == 1868:
    print u"明治元年"
elif year < 1912:
    print u"明治",year - 1867,u"年"
elif year == 1912:
    print u"大正元年"
elif year > 1912 and year < 1926:
    print u"大正",year - 1911,u"年"
elif year == 1926:
    print u"昭和元年"
elif year > 1926 and year < 1989:
    print u"昭和",year - 1925,u"年"
elif year == 1989:
    print u"平成元年"
elif year > 1989:
    print u"平成",year - 1988,u"年"
    
if year == 1991:
    print u"この年に生まれました。"