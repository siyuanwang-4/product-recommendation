from CollaborativeFiltering import find_similar_items
from agent import agent
from w2v import get_model
import pandas as pd

def recommend_products(user_like, file):
    """
    Recommend similar products
    Args:
        file (str): Sales records
        user_like (str): Products liked by the user
    Returns:
        str: Recommendation results
    """

    previous_output = ""
    
    # Load product data sales.xlsx
    sales_file= file
    if not sales_file:
        yield "Please upload a file first."
        return
    items = pd.read_excel(sales_file)
    # Combine product_name and product_category columns, connect with space, generate new column new_product_category
    items['new_product_category'] = items['product_name'] + ' ' + items['product_category']

    # Get all product names
    other_items = [str(x) for x in items['new_product_category'].tolist()]

    # Find products most similar to user_like
    similar_items = find_similar_items(user_like, model, other_items, top_n=10)

    for i in agent(similar_items, user_like):
        previous_output = previous_output + i
        yield previous_output


if __name__ == '__main__':
    model = get_model()
    # Recommend suits, streaming output
    for i in recommend_products(user_like = "suit", 
                                file = "sales.xlsx"):
        print("\r" + i, end="")


    