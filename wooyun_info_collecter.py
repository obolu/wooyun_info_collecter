#!/usr/bin/python3 
# -*- coding: utf-8 -*-
#coding: UTF-8
#python3 公司名

import requests
import re
import sys
import re

def get_vuln_num(content):
        findenty = re.compile(r'<small>(.*?)</small>')
        enty = re.findall(findenty,content)
        #print r0.text
        num = enty[0]
        #获得漏洞总数，返回公司名：共n条记录
        return num

def wash(content):
        re1 = content.replace("<td><a href=","")
        result = re1.replace("</a></td>","")
        #清洗数据，获得漏洞名，漏洞URL
        return result

def get_totalPages(content):
        findenty = re.compile(r'totalPages: (.*?),',re.DOTALL)
        enty = re.findall(findenty,content)
        #print r0.text
        num = enty[0]
        #获取总页数，方便获得所有漏洞信息
        return num

def get_vuln(content):
        findenty = re.compile(r'target="_blank">(.*?)target="_',re.DOTALL)
        enty = re.findall(findenty,content)
        #print r0.text 
        for i in range(len(enty)):
            r = wash(enty[i])
            print (r)
        #获取给定网页的漏洞信息，格式为漏洞名，漏洞URL

def main(key):
        url1 = 'https://domain/search?keywords='+str(key)+'&content_search_by=by_bugs'
        #proxies = {'http': 'http://127.0.0.1:8080'}
        #r=requests.post(url,data,headers,proxies=proxies)
        #添加代理，测试代码
        r1=requests.get(url1)
        result = str(key)+":"+get_vuln_num(r1.text)
        #返回公司名：共n条记录
        print (result)
        print (get_vuln(r1.text))
        pagenum = get_totalPages(r1.text)
        if int(pagenum)>1:
                    for i in range(1,int(pagenum)+1):
                        url = 'https://domain/search?keywords='+str(key)+'&&page='+str(i)+'&&content_search_by=by_bugs&&search_by_html=False'
                        #print (url)
                        r = requests.get(url)
                        #print (r.text)
                        print (get_vuln(r.text))
        return "Finish!"
    
if __name__ == '__main__':
        url = sys.argv[1]
        print (main(url))
