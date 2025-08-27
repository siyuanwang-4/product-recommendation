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

## Project Overview
This is a product recommendation system based on natural language processing. By analyzing sales data and product descriptions, the system recommends relevant products to users.

## Project Structure
The repository currently contains the following files:
- `sales.xlsx`: Product sales data file containing product IDs, names, sales volume, and other information
- `w2v.py`: Word2Vec model script for learning vector representations of product names
- `similarity.py`: Module for calculating similarity between product vectors using cosine similarity

## Implemented Features
1. **Data Preprocessing**: Loading and processing product sales data from Excel files
2. **Word2Vec Model**: Training word vector representations for product names to prepare for subsequent similarity calculations
3. **Similarity Calculation**: Computing cosine similarity between product vectors to find similar items

## Technology Stack
- Python
- pandas (for data processing)
- gensim (for Word2Vec model)
- numpy (for vector operations and similarity calculations)

## Usage Instructions
1. Ensure the required dependencies are installed:
   ```
   pip install pandas gensim numpy text2vec
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

## Future Plans
- Implement collaborative filtering module (CollaborativeFiltering.py)
  - Will integrate Word2Vec and similarity calculation to provide product recommendations
  - Will include functions to find similar items based on product names and categories
- Develop recommendation algorithms
- Build a recommendation system interface
