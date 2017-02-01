def buildDatabase(supportThreshold, inputFileName):
	transactions = list()
	itemsetCount = dict()
	frequentItemset = set()
	inputFile = open(inputFileName)
	for transaction in inputFile:
		transaction = transaction.strip()
		transactionList = transaction.split(',')
		for item in transactionList:
			itemsetCount[item] = itemsetCount.get(item, 0) + 1
			if itemsetCount[item] >= supportThreshold:
				frequentItemset.add(item)
		transactions.append(transactionList)
	return transactions, frequentItemset

# Takes in an itemset (list of string) and returns List<String> of all subsets that can be created
def makeSubsets(itemSet):
	maxLength = len(itemSet)
	retList = list()
	if maxLength > 1:
		for i in range(0, len(itemSet)):
			retList.append(itemSet[:i] + itemSet[(i+1):])
	return retList

# @param: singleFrequentItems : Set of all single frequent itemsets
# @param: previousItemSetSet : Set of all itemsets of length k
# Return a set of strings with k+1 supersets
# Example: Given {'a','b','c'}, return {'ab','ac', 'bc'}
def makeNextSuperset(singleFrequentItems, previousItemSetSet):
	retVal = list()
	for itemSet in previousItemSetSet:
		for addedItem in singleFrequentItems:
			if addedItem not in itemSet:
				newItemSet = ''.join(sorted(itemSet + addedItem))
				if newItemSet not in retVal:
					retVal.append(newItemSet)
	return retVal
# @param: database : List<List<String>> of all transactions
# @param: frequentItemset : Set<String> of all frequent itemsets
# @param: supportThreshold : Int representing the support threshold 
# @return: returns all frequentItemsets appearing in the database
def findAllFrequentItemsets(database, frequentItemset, supportThreshold):
	singleFrequentItems = list(frequentItemset)
	currentList = frequentItemset
	previousList = frequentItemset

	# stop when current list is empty (no more supersets were created)
	while(len(currentList) > 0):
		# current list = makeNextSuperset()
		intermediateList = list()
		currentList = makeNextSuperset(singleFrequentItems, previousList)
		# check that all subsets of each superset exist in previous list
		for newSuperSet in currentList:
			# if there are itemsets which have subsets that do not exist, prune them
			subsets = makeSubsets(newSuperSet)
			okToAdd = True
			for subset in subsets:
				if subset not in previousList:
					okToAdd = False
			# add all of the non-pruned current list to the frequent itemset
			if okToAdd and isFrequentInDatabase(database, newSuperSet, supportThreshold):
				frequentItemset.add(newSuperSet)
				intermediateList.append(newSuperSet)
		previousList = currentList
		currentList = intermediateList
	return frequentItemset
# @param: database : 
def isFrequentInDatabase(database, itemSet, supportThreshold):
	currentCount = 0
	for transaction in database:
		found = True
		for item in itemSet:
			if item not in transaction:
				found = False
				break
		if found:
			currentCount += 1
		if currentCount == supportThreshold:
			return True
	return False

supportThreshold = int(input('Enter the support threshold \n'))
inputFileName = input('Enter the name of the file \n')
database, frequentItemset = buildDatabase(supportThreshold, inputFileName);
sortedFrequentItemsets = sorted(findAllFrequentItemsets(database, frequentItemset, supportThreshold))
print(sortedFrequentItemsets)