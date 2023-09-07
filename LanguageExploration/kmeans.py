from sklearn.cluster import KMeans

from parse import *

num_clusters = 8
mode = "bert"

if mode == "glove":
	words, vectors = load_glove_vectors()
elif mode == "bert":
	words, vectors = load_bert_embeddings()
kmeans = KMeans(n_clusters=num_clusters, max_iter=1000, random_state=0)
labels = kmeans.fit_predict(vectors) # (vocab_size)
distances = kmeans.transform(vectors)**2 # (vocab_size, cluster_size)

labels_to_words = {}
labels_to_averages = {}
for cluster in range(num_clusters):
	labels_to_words[cluster] = []
	sum = 0
	for j in range(len(labels)):
		if labels[j] == cluster:
			labels_to_words[cluster].append(words[j])
			sum += distances[j][cluster]
	labels_to_averages[cluster] = sum / len(labels_to_words[cluster])

print(labels_to_averages)

for cluster in range(num_clusters):
	print("Cluster #%d" % cluster)
	print("Length = %d" % len(labels_to_words[cluster]))
	print("Avg. dist. = %.5f" % labels_to_averages[cluster])
	print(labels_to_words[cluster][:100])