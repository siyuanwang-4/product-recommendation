
from text2vec import Word2Vec

def get_model(name = "w2v-light-tencent-chinese"):
    return Word2Vec(name)

def compute_emb(model, sentences):
    # Embed a list of sentences
    # sentences = [
    #     '卡',
    #     '银行卡',
    #     '如何更换花呗绑定银行卡',
    #     '花呗更改绑定银行卡',
    #     'This framework generates embeddings for each input sentence',
    #     'Sentences are passed as a list of string.',
    #     'The quick brown fox jumps over the lazy dog.',
    #     '敏捷的棕色狐狸跳过了懒狗',
    # ]
    sentence_embeddings = model.encode(sentences, show_progress_bar=True, normalize_embeddings=True)
    return sentence_embeddings


if __name__ == "__main__":
    # 中文词向量模型(word2vec)，中文字面匹配任务和冷启动适用
    w2v_model = get_model()
    compute_emb(w2v_model, ["银行卡"])