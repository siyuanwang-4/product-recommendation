# Product Recommendation System

## Update Log

### Phase 1
- Initial repository setup
- Added sales data file (sales.xlsx)
- Implemented Word2Vec model loading (w2v.py) - using pre-trained model

### Phase 2
- Implemented similarity calculation module (similarity.py)
  - Added cosine similarity calculation function
  - Supports finding top N most similar items based on vector representations
  - Includes comprehensive documentation and example usage

### Phase 3
- Implemented collaborative filtering module (CollaborativeFiltering.py)
  - Integrated Word2Vec and similarity calculation to provide product recommendations
  - Added find_similar_items function to find similar items based on product names and categories
  - Combined product names and categories for better recommendation accuracy

## Project Overview
This is a product recommendation system based on natural language processing and collaborative filtering. By analyzing sales data and product descriptions, the system recommends relevant products to users using similarity-based methods.

## Project Structure
The repository currently contains the following files:
- `sales.xlsx`: Product sales data file containing product IDs, names, sales volume, and other information
- `w2v.py`: Word2Vec model script for learning vector representations of product names
- `similarity.py`: Module for calculating similarity between product vectors using cosine similarity
- `CollaborativeFiltering.py`: Collaborative filtering module for finding similar products based on vector representations

## Implemented Features
1. **Data Preprocessing**: Loading and processing product sales data from Excel files
2. **Word2Vec Model**: Training word vector representations for product names to prepare for subsequent similarity calculations
3. **Similarity Calculation**: Computing cosine similarity between product vectors to find similar items
4. **Collaborative Filtering**: Finding similar items based on product names and categories using vector representations

## Technology Stack
- Python
- pandas (for data processing)
- gensim (for Word2Vec model)
- numpy (for vector operations and similarity calculations)

## Usage Instructions
1. Ensure the required dependencies are installed:
   ```
   pip install pandas gensim numpy text2vec torch 
   ```
2. Run the `w2v.py` script to train the Word2Vec model:
   ```
   python w2v.py
   ```
3. Use the similarity module to find similar products:
   ```python
   from similarity import calculate_similarity
   # Example usage
   similar_items = calculate_similarity(target_vector, other_vectors, other_items, top_n=10)
   ```
4. Use the collaborative filtering module to find similar items:
   ```python
   from CollaborativeFiltering import find_similar_items
   # Example usage
   similar_items = find_similar_items('西装 男', model, other_items, top_n=10)
   ```

## Future Plans
- **Intelligent Recommendation Agent**: Implement an AI-powered recommendation agent that can understand user preferences and provide personalized recommendations. This would improve the system by moving beyond simple similarity-based recommendations to more contextual and user-aware suggestions.

