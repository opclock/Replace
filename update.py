# -*- coding: UTF-8 -*-
import Functions, ConfigReader
import os, sys, time, commands
from Client import Client

#1.校验tar包MD5码

client = ConfigReader.getClient(sys.argv[1])

tarFileMD5 = Functions.getFileMd5(Client.tarFilePath)

if Client.MD5==tarFileMD5:

  #2.校验成功后解压
  Functions.extract(Client.tarFilePath, Client.tempDirPath)
  #3.停止tomcat服务
  (shutresult, shutreturn) = commands.getstatusoutput(Client.tomcatPath+"/bin/shutdown.sh")
  print("shutresult-------->"+str(shutresult))
  # print("shutreturn-------->"+shutreturn)
  (status, pid) = commands.getstatusoutput("pidof java")
  if(status == 0):
    Functions.killProcess()

  #4.替换程序
  print("文件夹路径:"+Client.folderPath)
  (cpresutl, cpreturn) = commands.getstatusoutput("cp -rf "+Client.folderPath+" "+Client.tomcatPath+"/webapps")
  print("cpresutl-------->" + str(cpresutl))
  #5.删除临时文件
  (rmresult, rmreturn) = commands.getstatusoutput("rm -rf "+Client.tempDirPath)
  print("rmresult-------->" + str(rmresult))
  #6.启动tomcat服务
  (startresult, startreturn) = commands.getstatusoutput(Client.tomcatPath+"/bin/startup.sh")
  print("startresult-------->" + str(startresult))
  #7.验证tomcat是否启动成功



else:
  print("MD5校验失败!")