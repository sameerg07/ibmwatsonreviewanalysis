import ast

fp = open('negReviewsRest.txt')
negResDict = ast.literal_eval(fp.readlines()[0])

# emptyValsKeys = []

# for key,val in negResDict.items():
# 	if(len(val) == 0):
# 		emptyValsKeys.append(key)

for key,val in negResDict.items():
	try:
		negResDict[key] = val[0]
	except:
		pass

finalResDict = {}

for key,val in negResDict.items():
	try:
		if(val[4][0]<0):
			finalResDict[key] = val
	except:
		pass
		
finalDict = {}
for key,val in finalResDict.items():
	finalDict[key] = []
	temp =[]
	try:
		for ele in val[4]:
			if(ele<-0.4):
				temp.append([ele,val[1][val[4].index(ele)]])
		finalDict[key] = temp
	except:
		pass

print(finalDict)

# print(finalResDict) 