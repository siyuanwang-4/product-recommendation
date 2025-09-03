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

### Phase 4
- Implemented intelligent recommendation agent (agent.py)
  - Integrated ZhipuAI GLM-4.5-Flash model for intelligent product recommendations
  - Added agent function to process similar items and generate personalized recommendations
  - Implemented streaming response for real-time recommendation generation
- Enhanced main recommendation system (main.py)
  - Updated recommend_products function to use the intelligent agent
  - Improved user experience with streaming output of recommendations
  - Translated all Chinese text to English for better international accessibility

## Project Overview
This is a product recommendation system based on natural language processing, collaborative filtering, and AI-powered agents. By analyzing sales data and product descriptions, the system recommends relevant products to users using similarity-based methods and intelligent reasoning.

## Project Structure
The repository currently contains the following files:
- `sales.xlsx`: Product sales data file containing product IDs, names, sales volume, and other information
- `w2v.py`: Word2Vec model script for learning vector representations of product names
- `similarity.py`: Module for calculating similarity between product vectors using cosine similarity
- `CollaborativeFiltering.py`: Collaborative filtering module for finding similar products based on vector representations
- `agent.py`: Intelligent recommendation agent using ZhipuAI GLM-4.5-Flash model
- `main.py`: Main recommendation system that integrates all components

## Implemented Features
1. **Data Preprocessing**: Loading and processing product sales data from Excel files
2. **Word2Vec Model**: Training word vector representations for product names to prepare for subsequent similarity calculations
3. **Similarity Calculation**: Computing cosine similarity between product vectors to find similar items
4. **Collaborative Filtering**: Finding similar items based on product names and categories using vector representations
5. **Intelligent Recommendation Agent**: Using AI model to analyze user preferences and generate personalized recommendations
6. **Streaming Output**: Providing real-time recommendation results to enhance user experience

## Technology Stack
- Python
- pandas (for data processing)
- gensim (for Word2Vec model)
- numpy (for vector operations and similarity calculations)
- ZhipuAI GLM-4.5-Flash (for intelligent recommendations)

## Usage Instructions
1. Ensure the required dependencies are installed:
   ```
   pip install pandas gensim numpy text2vec torch zai 
   ```
2. Set API keys for ZhipuAI in the `agent.py` file:

3. Use the main recommendation system with intelligent agent:
   ```python
   python main.py
   ```

## Future Plans
- **User Preference Learning**: Implement a system to learn and remember user preferences over time for increasingly personalized recommendations
- **Multi-modal Recommendations**: Extend the system to incorporate product images and descriptions for more comprehensive recommendations
- **Performance Optimization**: Optimize the recommendation engine for faster response times and better scalability

