from collections import Counter


scores = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4,
'X': 8, 'Y': 4, 'Z': 10}

# Opens the SOWPODS words file and creates a list of all valid words
# in Scrabble
# File must only contain one word per line
# Removes all '\n' and '\r' characters from each line
def wordList(filename):
	wordList = []
	f = open(filename, 'r')
	word = f.readline()
	while word:
		word = word.strip('\n\r')
		word = word.upper()
		wordList.append(word)
		word = f.readline()
	return wordList

# Asks user to input the letters they have in their rack
# Returns a list, with each element equal to one of the characters the
# user gives
def scrabbleRack():
	userRack = str(raw_input('Enter the letters in your rack: '))
	userRack = userRack.upper()
	userRackList = []
	for x in userRack:
		userRackList.append(x)
	return userRackList

# Given an input of a single word and the list of user letters, this
# will return whether or not the word can be constructed from the
# user's letters they have
def validWord(word, userRackList):
	word2, word1 = Counter(word), Counter(userRackList)
	return all(word2[k] <= word1.get(k, 00) for k in word2)

# Given a list of words and the 
def validWordList(wordList, userRack):
	validWordList = []
	index = 0
	while index < len(wordList):
		if validWord(wordList[index], userRack):
			validWordList.append(wordList[index])
		index = index + 1
	return validWordList

def findScore(wordList, scores):
	scoreList = []
	for word in wordList:
		score = 0
		for letter in word:
			score = score + scores[letter]
		scoreList.append((score, word))
	return sorted(scoreList, reverse = True)

def printScoreList(scoreList):
	for x in scoreList:
		print x


wordList = wordList('sowpods.txt')
userLetters = scrabbleRack()
validWordList = validWordList(wordList, userLetters)
scoreList = findScore(validWordList, scores)
printScoreList(scoreList)
