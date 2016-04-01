#!/usr/bin/python
#coding:utf-8
from lan import lanMain
import json,sys,yaml

def ReadServer():
    with open('conf/server.yml','r') as f:
        s=yaml.load(f)
    return s
def GetServer(server_group,server):
    for i in server[server_group]:
        server_list=server[server_group][i]
        yield [i,server_list[0],server_list[1]]
def ReadModule():
    #读取模块
    with open('conf/module.yml','r') as f:
        s=yaml.load(f)
    return s
def main():
    #启用日志
    #lanMain.logs(True)
    server_conf=ReadServer()
    for server in GetServer(sys.argv[1], server_conf):
        ssh=lanMain.lianjie(user=server[1],passwd=server[2],host=server[0])
        m=ReadModule()
        try:
            mLen=0
            while mLen <len(m[sys.argv[2]]):
                yield '%s:\n%s'%(server[0],lanMain.mingling(m[sys.argv[2]][mLen], ssh))
                mLen=mLen+1   
        finally:
            ssh.close()
if __name__=='__main__':
     command_out=main()
     for i in command_out:
         print i[:-1]