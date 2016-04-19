class Client(object):
  def __init__(self, tempPath, tomcatPath, tempDirPath, tarFileName, tarFilePath, folderPath, folderName, MD5):
    self.tempPath = tempPath
    self.tomcatPath = tomcatPath
    self.tempDirPath = tempDirPath
    self.tarFileName = tarFileName
    self.tarFilePath = tarFilePath
    self.folderPath = folderPath
    self.folderName = folderName
    self.MD5 = MD5
