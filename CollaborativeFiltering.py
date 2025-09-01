import numpy as np
import pandas as pd
from collections import defaultdict
from w2v import get_model, compute_emb
from similarity import calculate_similarity


def find_similar_items(item_name, model, other_items, top_n=10):
    """
    Find the most similar items to the given product

    Parameters:
    item_name -- Target product name
    model -- Trained Word2Vec model
    top_n -- Return the top n most similar products
    other_items -- List of other products

    Returns:
    A list of (product name, similarity) tuples, sorted by similarity in descending order
    """
    # Get the vector representation of the target product
    item_emb = compute_emb(model, [item_name])[0]

    # Get the vector representations of other products
    other_items_emb = compute_emb(model, other_items)

    # Get the similarity of all products similar to the target product
    similar_items = calculate_similarity(item_emb, other_items_emb, other_items, top_n = top_n)

    return similar_items


if __name__ == '__main__':
    # Load the trained Word2Vec model
    model = get_model()

    # Load product data from sales.xlsx
    items = pd.read_excel('sales.xlsx')
    # Combine product_name and category columns with a space to create a new product_category column
    items['product_category'] = items['product_name'] + ' ' + items['category']

    # Get all product names
    other_items = items['product_category'].tolist()

    # Find the most similar products to "西装 男"
    similar_items = find_similar_items('西装 男', model, other_items, top_n=10)
    print(similar_items)
