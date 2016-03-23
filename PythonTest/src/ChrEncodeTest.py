# coding:utf-8
'''
Created on 2016/03/01

@author: JUN_AKAGI
'''
import sys
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

jtext = "どかーんどかーん"

print (jtext)
#print "どかーんどかーん"

