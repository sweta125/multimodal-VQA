import torch
from transformers import BertModel, BertTokenizer
import pickle
from tqdm import tqdm

from parse import *

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def run_bert():
	# load data
	all_questions = get_all_questions()
	all_embeddings = []

	tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
	model = BertModel.from_pretrained('bert-base-uncased', output_hidden_states=True)
	model = model.to(device)
	model.eval()

	for question in tqdm(all_questions):
		token_ids = tokenizer.encode(question)
		token_ids = torch.LongTensor(token_ids)
		token_ids = token_ids.unsqueeze(0) #(num_sent, tokens)
		token_ids = token_ids.to(device)

		with torch.no_grad():
		    out = model(input_ids=token_ids) # tuple with 3 elements

		last_hidden_state = out[0] # (num_sent=1, tokens, hidden_dim=768)
		# take the embedding for the [CLS] token
		sentence_embedding = last_hidden_state[0][0] # (hidden_dim)

		all_embeddings.append(sentence_embedding.tolist())

	return all_questions, all_embeddings

def print_to_file(all_questions, all_embeddings):
	file = "bert_embeddings.pkl"
	with open(file, "wb") as f:
		pickle.dump((all_questions, all_embeddings), f)

if __name__ == '__main__':
	all_questions, all_embeddings = run_bert()
	print_to_file(all_questions, all_embeddings)