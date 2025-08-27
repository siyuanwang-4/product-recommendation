
from text2vec import Word2Vec

def get_model(name = "w2v-light-tencent-chinese"):
    return Word2Vec(name)

def compute_emb(model, sentences):
    # Embed a list of sentences
    # sentences = [
    #     'card',
    #     'bank card',
    #     'how to change Huabei binding bank card',
    #     'Huabei change binding bank card',
    #     'This framework generates embeddings for each input sentence',
    #     'Sentences are passed as a list of string.',
    #     'The quick brown fox jumps over the lazy dog.',
    #     'The agile brown fox jumps over the lazy dog',
    # ]
    sentence_embeddings = model.encode(sentences, show_progress_bar=True, normalize_embeddings=True)
    return sentence_embeddings


if __name__ == "__main__":
    # Chinese word vector model (word2vec), suitable for Chinese literal matching tasks and cold start
    w2v_model = get_model()
    print(compute_emb(w2v_model, ["银行卡"]))