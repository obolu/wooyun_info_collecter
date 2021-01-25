# wooyun_info_collecter

## 功能
通过公司名信息收集wooyun历史信息

## 效果

```
$ python3 wooyun_info_collecter.py 华为
华为:共231记录

华为某分站存在SSRF漏洞
"https://www.madebug.net/static/bugs/wooyun-2016-0214331.html"

华为某重要系统存在安全问题已Getshell(泄露敏感信息)
"https://www.madebug.net/static/bugs/wooyun-2016-0211454.html"

华为某站存在SQL注入(17w用户)&amp;任意文件下载
"https://www.madebug.net/static/bugs/wooyun-2016-0205773.html"
```

## 用法
python3 wooyun_info_collecter.py 华为

## 原理
通过公司名收集wooyun历史漏洞信息。测试网站：https://www.madebug.net
