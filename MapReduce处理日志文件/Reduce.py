# coding : utf-8
#file: Reduce.py

import os,os.path,re

def Reduce(sourceFoler,targetFile):
	tempData = {}										#缓存列表
	p_re = re.compile(r'(.*?)(\d{1,}$)',re.IGNORECASE)	#用正则表达式解析数据
	for root,dirs,files in os.walk(sourceFolder):
		for fil in files:
			if fil.endswith('_map.txt'):				#判断是reduce文件
				sFile = open(os.path.abspath(os.path.join(root,fil)),'r')
				dataLine = sFile.readline()
				
				while dataLine:							#当有数据时
					subdata = p_re.findall(dataLine)	#用空格分割数据
					if subdata[0][0] in tempData:
						tempData[subdata[0][0]] += int(subdata[0][1])
					else:
						tempData[subdata[0][0]] = int(subdata[0][1])
					dataLine = sFile.readline()			#读入下一行数据
					
				sFile.close()
				
	tList = []
	for key,value in sorted(tempData.items(),key = lambda k:k[1],reverse = True):
		tList.append(key + ' ' + str(value) + '\n' )
		
	tFilename = os.path.join(sourceFolder,targetFile + '_reduce.txt')
	tFile = open(tFilename,'a+')						#创建小文件
	tFile.writelines(tList)								#将列表保存到文件中
	tFile.close()
		
if __name__ == '__main__':
	Reduce ('access','access')