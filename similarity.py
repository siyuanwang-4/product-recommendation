import numpy as np
from numpy.linalg import norm

def calculate_similarity(target_word_vector, other_word_vectors, other_words=None, top_n=10):
    """
    Calculate cosine similarity between target word and other words

    Parameters:
    target_word_vector -- Vector of the target word (numpy array)
    other_word_vectors -- List of vectors for other words (list of numpy arrays or 2D numpy array)
    other_words -- List of other words (list of strings), optional. If provided, will return a dictionary of words with their similarity scores
    top_n -- Number of most similar words to return, optional. Default is 10

    Returns:
    If other_words is provided, returns the top 10 most similar words and their similarity scores
    Otherwise, returns the similarity list
    """
    # Ensure inputs are numpy arrays
    target_word_vector = np.array(target_word_vector)
    other_word_vectors = np.array(other_word_vectors)

    # Calculate cosine similarity
    # Use dot product to calculate similarity and normalize
    dot_product = np.dot(other_word_vectors, target_word_vector)
    norm_target = norm(target_word_vector)
    norm_others = norm(other_word_vectors, axis=1)

    # Avoid division by zero
    similarity = dot_product / (norm_target * norm_others + 1e-10)

    # Determine return format based on whether word list is provided
    if other_words is not None:
        if len(other_words) != len(other_word_vectors):
            raise ValueError("Word list and vector list length do not match")
        # Select the top_n most similar words
        top_indices = similarity.argsort()[-top_n:][::-1]
        top_words = [other_words[i] for i in top_indices]
        return top_words
    else:
        return similarity


if __name__ == "__main__":
    # Example usage
    target_word_vector = [0.1, 0.2, 0.3]
    other_word_vectors = [[0.4, 0.5, 0.6], [0.7, 0.8, 0.9], [0.1, 0.2, 0.3]]
    other_words = ["word1", "word2", "word3"]
    print(calculate_similarity(target_word_vector, other_word_vectors, other_words))