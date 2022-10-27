import logging
from gensim.models import word2vec

def main():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	sentences = word2vec.LineSentence("./wiki.txt")
	model = word2vec.Word2Vec(sentences, vector_size=100, min_count=15, window=15)
	model.save("w2v.model")

if __name__ == "__main__":
	main()
