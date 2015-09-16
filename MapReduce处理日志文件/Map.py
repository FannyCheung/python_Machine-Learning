# coding:utf-8
#file: Map.py

import os,os.path,re

def Map(sourceFile,targetFolder):
	sFile = open(sourceFile,'r')
	dataLine = sFile.readline()
	tempData = {}							#缓存列表		
	if not os.path.isdir(targetFolder):		#如果目标目录不存在，则创建
		os.mkdir(targetFolder)
	while dataLine:							#如果有数据
		p_re = re.compile(r'(GET|POST)\s(.*?)\sHTTP/1.[01]',re.IGNORECASE)		#用正则表达式解析数据
		match = p_re.findall(dataLine)
		if match:
			visitUrl = match[0][1]
			if visitUrl in tempData:
				tempData[visitUrl] += 1
			else:
				tempData[visitUrl] = 1
		dataLine = sFile.readline()			#读入下一行数据
	sFile.close()
	
	tList = []
	for key,value in sorted(tempData.item(), key = lambda k:k[1],reverse = True):
		tList.append(key + ' ' + str(value) + '\n')
	
	tFilename = os.path.join(targetFolder,os.path.split(sourceFile)[1] + '_map.txt')
	tFile = open(tFilename,'a+')			#创建小文件
	tFile.writelines(tList)					#将列表保存到文件中
	tFile.close()

if __name__ == '__main__':
	Map('access\\access.log1.txt','access')
	Map('access\\access.log2.txt','access')
	Map('access\\access.log3.txt','access')