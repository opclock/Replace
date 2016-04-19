# -*- coding: UTF-8 -*-
import tarfile, os, commands
import hashlib


def isSubString(SubStrList, Str):
  flag = True
  for substr in SubStrList:
    if not (substr in Str):
      flag = False
  return flag


# 获取指定目录下所有文件夹及文件(目录名, 关键字)
def getFileList(FindPath, FlagStr=[]):
  import os
  FileList = []
  FileNames = os.listdir(FindPath)
  if (len(FileNames) > 0):
    for fn in FileNames:
      if (len(FlagStr) > 0):
        # 返回指定类型的文件名
        if (isSubString(FlagStr, fn)):
          fullfilename = os.path.join(FindPath, fn)
          FileList.append(fullfilename)
      else:
        # 默认直接返回所有文件名
        fullfilename = os.path.join(FindPath, fn)
        FileList.append(fullfilename)
  # 对文件名排序
  if (len(FileList) > 0):
    FileList.sort()
  return FileList


# 将指定文件夹打包成tar
def mak_tar(foldername, dest_folder, compression='bz2'):
  if compression:
    dest_ext = '.' + compression
  else:
    dest_ext = ''
  arcname = os.path.basename(foldername)
  dest_name = '%s.tar%s' % (arcname, dest_ext)
  dest_path = os.path.join(dest_folder, dest_name)
  if compression:
    dest_cmp = ':' + compression
  else:
    dest_com = ''
  out = tarfile.TarFile.open(dest_path, 'w' + dest_cmp)
  out.add(foldername, arcname)
  out.close()
  return dest_path

def extract(tar_path, target_path):
  try:
    tar = tarfile.open(tar_path, "r:bz2")
    file_names = tar.getnames()
    for file_name in file_names:
      tar.extract(file_name, target_path)
    tar.close()
  except:
    print("解压失败!")


def getFileMd5(strFile):
  file = None
  bRet = False
  strMd5 = ""

  try:
    file = open(strFile, "rb")
    md5 = hashlib.md5()
    strRead = ""

    while True:
      strRead = file.read(8096)
      if not strRead:
        break
      md5.update(strRead)
    # read file finish
    bRet = True
    strMd5 = md5.hexdigest()
  except:
    bRet = False
  finally:
    if file:
      file.close()

  return strMd5

def killProcess():
  (status, pid) = commands.getstatusoutput("pidof java")
  if (status == 0):
    os.system("kill "+str(pid))
    killProcess()