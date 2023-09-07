"""
Footnotes 2 and 6 in M4C paper explain how the evaluation metrics are calculated:

TextVQA: 

https://visualqa.org/evaluation

https://github.com/GT-Vision-Lab/VQA/blob/master/PythonEvaluationTools/vqaEvalDemo.py



STVQA: 

https://rrc.cvc.uab.es/?ch=11&com=tasks

TextVQA Evaluation Metric

Code: #https://github.com/GT-Vision-Lab/VQA/blob/master/PythonEvaluationTools/vqaEvaluation/vqaEval.py
"""

import sys
import re

manualMap = {'none': '0', 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10'}
articles = ['a', 'an', 'the']
periodStrip  = re.compile("(?!<=\d)(\.)(?!\d)")
commaStrip   = re.compile("(\d)(\,)(\d)")
punct = [';', r"/", '[', ']', '"', '{', '}', '(', ')', '=', '+', '\\', '_', '-', '>', '<', '@', '`', ',', '?', '!']
contractions = {"aint": "ain't", "arent": "aren't", "cant": "can't", "couldve": "could've", "couldnt": "couldn't", \
		"couldn'tve": "couldn't've", "couldnt've": "couldn't've", "didnt": "didn't", "doesnt": "doesn't", "dont": "don't", "hadnt": "hadn't", \
		"hadnt've": "hadn't've", "hadn'tve": "hadn't've", "hasnt": "hasn't", "havent": "haven't", "hed": "he'd", "hed've": "he'd've", \
		"he'dve": "he'd've", "hes": "he's", "howd": "how'd", "howll": "how'll", "hows": "how's", "Id've": "I'd've", "I'dve": "I'd've", \
		"Im": "I'm", "Ive": "I've", "isnt": "isn't", "itd": "it'd", "itd've": "it'd've", "it'dve": "it'd've", "itll": "it'll", "let's": "let's", \
		"maam": "ma'am", "mightnt": "mightn't", "mightnt've": "mightn't've", "mightn'tve": "mightn't've", "mightve": "might've", \
		"mustnt": "mustn't", "mustve": "must've", "neednt": "needn't", "notve": "not've", "oclock": "o'clock", "oughtnt": "oughtn't", \
		"ow's'at": "'ow's'at", "'ows'at": "'ow's'at", "'ow'sat": "'ow's'at", "shant": "shan't", "shed've": "she'd've", "she'dve": "she'd've", \
		"she's": "she's", "shouldve": "should've", "shouldnt": "shouldn't", "shouldnt've": "shouldn't've", "shouldn'tve": "shouldn't've", \
		"somebody'd": "somebodyd", "somebodyd've": "somebody'd've", "somebody'dve": "somebody'd've", "somebodyll": "somebody'll", \
		"somebodys": "somebody's", "someoned": "someone'd", "someoned've": "someone'd've", "someone'dve": "someone'd've", \
		"someonell": "someone'll", "someones": "someone's", "somethingd": "something'd", "somethingd've": "something'd've", \
		"something'dve": "something'd've", "somethingll": "something'll", "thats": "that's", "thered": "there'd", "thered've": "there'd've", \
		"there'dve": "there'd've", "therere": "there're", "theres": "there's", "theyd": "they'd", "theyd've": "they'd've", \
		"they'dve": "they'd've", "theyll": "they'll", "theyre": "they're", "theyve": "they've", "twas": "'twas", "wasnt": "wasn't", \
		"wed've": "we'd've", "we'dve": "we'd've", "weve": "we've", "werent": "weren't", "whatll": "what'll", "whatre": "what're", \
		"whats": "what's", "whatve": "what've", "whens": "when's", "whered": "where'd", "wheres": "where's", "whereve": "where've", \
		"whod": "who'd", "whod've": "who'd've", "who'dve": "who'd've", "wholl": "who'll", "whos": "who's", "whove": "who've", "whyll": "why'll", \
		"whyre": "why're", "whys": "why's", "wont": "won't", "wouldve": "would've", "wouldnt": "wouldn't", "wouldnt've": "wouldn't've", \
		"wouldn'tve": "wouldn't've", "yall": "y'all", "yall'll": "y'all'll", "y'allll": "y'all'll", "yall'd've": "y'all'd've", \
		"y'alld've": "y'all'd've", "y'all'dve": "y'all'd've", "youd": "you'd", "youd've": "you'd've", "you'dve": "you'd've", \
		"youll": "you'll", "youre": "you're", "youve": "you've"}
		
def evaluate(labels, preds):
	assert(len(labels) == len(preds))
	accuracies = []
	for resAns in preds:
	    resAns      = resAns.replace('\n', ' ')
		resAns      = resAns.replace('\t', ' ')
		resAns      = resAns.strip()
		resAns      = processPunctuation(resAns)
		resAns      = processDigitArticle(resAns)

	process_labels = []
	for list_answers in labels:
		process_labels.append([processPunctuation(item) for item in list_answers])

	for i in range(len(process_labels)):
		list_answers = labels[i]
		incorrect = [item for item in list_answers if item!=preds[i]]
		correct = [item for item in list_answers if item==preds[i]]
		acc = min(1, float(len(matchingAns))/3)
		accuracies.append(acc)
	
	avg_acc = float(sum(accuracies))/len(accuries)
	assert(len(accuracies) == len(preds) == len(process_labels))
	return(accuracies, avg_acc)

def processPunctuation(inText):
	outText = inText
	for p in punct:
		if (p + ' ' in inText or ' ' + p in inText) or (re.search(commaStrip, inText) != None):
			outText = outText.replace(p, '')
		else:
			outText = outText.replace(p, ' ')	
			outText = periodStrip.sub("",
				outText,
				re.UNICODE)
	return outText

def processDigitArticle(inText):
	outText = []
	tempText = inText.lower().split()
	for word in tempText:
		word = manualMap.setdefault(word, word)
		if word not in articles:
			outText.append(word)
		else:
	    	pass
	for wordId, word in enumerate(outText):
		if word in contractions: 
			outText[wordId] = contractions[word]
			outText = ' '.join(outText)
	return outText