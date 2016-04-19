# -*- coding: UTF-8 -*-
import ConfigParser,os,sys
from Client import Client

abspath = os.path.abspath(sys.argv[0])
abspath = os.path.dirname(abspath) + "/"

def getClient(tempDir):
  parser = ConfigParser.ConfigParser()
  parser.read(abspath + "ProjectConfigs.properties")
  Client.tempPath = parser.get("project", "temppath") #客户端的temp文件夹路径
  Client.tomcatPath = parser.get("project", "tomcatpath") #客户端的tomcat路径
  Client.tempDirPath = Client.tempPath + "/" +tempDir #temp文件夹下此次更新的文件夹路径
  Client.tarFileName = getUpdateInfos(Client.tempDirPath + "/updateinfo", "file")
  Client.tarFilePath = Client.tempDirPath + "/" + Client.tarFileName
  Client.folderPath = Client.tarFilePath[:Client.tarFilePath.rindex(".tar.bz2")]
  Client.folderName = Client.folderPath[Client.folderPath.rindex("/")+1:]
  Client.MD5 = getUpdateInfos(Client.tempDirPath + "/updateinfo", "MD5")


def getUpdateInfos(filePath, option):
  parser = ConfigParser.ConfigParser()
  parser.read(filePath)
  return parser.get("updateinfo", option)
