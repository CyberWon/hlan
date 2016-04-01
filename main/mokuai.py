#!/usr/bin/python
#coding:utf-8
import json,yaml
def module_json():
    with open('../conf/module.json','r') as f:
        s=json.load(f)
    print s['ip'][0]
def module_yaml():
    with open('../conf/module.yml','r') as f:
        s=yaml.load(f)
    print s
def server_yaml():
    with open('../conf/server.yml','r') as f:
        s=yaml.load(f)
    print s
server_yaml()