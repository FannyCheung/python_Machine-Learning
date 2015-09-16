# coding:utf-8
#file:FileSplit.py

import os,os.path,time

def FileSplit(sourceFile,targetFolder):
	sFile = open(sourceFile,'r')
	number = 100000							#每个小文件中保存100000条数据
	dataLine = sFile.readline()
	tempData = []							#缓存列表
	fileNum = 1 
	if not os.path.isdir(targetFolder):		#如果目标目录不存在，则创建
		os.mkdir(targetFolder)
	while dataLine:							#有数据
		for row in range(number):
			tempData.append(dataLine)		#将一行数据添加到列表中
			dataLine = sFile.readline()
			if not dataLine:				#如果没有数据需要保存
				break
		tFilename = os.path.join(targetFolder,os.path.split(sourceFile)[1] + str(fileNum) + '.txt')
		tFile = open(tFilename,'a+')		#创建小文件
		tFile.writelines(tempData)			#将列表保存到文件中
		tFile.close()
		tempData = []						#清空缓存列表
		print(tFilename + u'创建于:' + str(time.ctime()))
		fileNum += 1						#文件编号
		
	sFile.close()	
	
if __name__ == '__main__':
		FileSplit('access.log','access')