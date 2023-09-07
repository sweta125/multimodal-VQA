import numpy as np
import json
import pickle

def get_all_questions():
	json_file = "train_task_1.json"
	with open(json_file) as f:
		all_data = json.load(f)
		data = all_data["data"]
		all_questions = []
		count = 0
		word_set = {"what", "where", "how", "which", "who"}
		for line in data:
			question = line["question"]
			question = question.lower()
			"""if question.startswith("why"):
				count += 1"""
			if question.split()[0] not in word_set:
				count += 1
			# append a space when necessary
			if question[-1] == "?":
				question = question[:-1] + " ?"
			all_questions.append(question)
	print(count)
	print(count / len(all_questions))
	print("length = %d" % len(all_questions))

	corpus_file = "corpus.txt"
	with open(corpus_file, "w", encoding="utf-8") as f:
		for question in all_questions:
			f.write(question + "\n")

	return all_questions

def load_glove_vectors():
	vector_file = "vectors.txt"
	words = []
	vectors = []
	with open(vector_file) as f:
		for line in f:
			tokens = line.split()
			words.append(tokens[0])
			vector = [float(tokens[i]) for i in range(1, len(tokens))]
			vectors.append(vector)
	return words, vectors

def load_bert_embeddings():
	file = "bert_embeddings.pkl"
	with open(file, "rb") as f:
		(all_questions, all_embeddings) = pickle.load(f)
	return all_questions, all_embeddings

if __name__ == '__main__':
	get_all_questions()
	# load_glove_vectors()