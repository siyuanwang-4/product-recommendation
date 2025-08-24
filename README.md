# Product Recommendation System

## Update Log

### Phase 1
- Initial repository setup
- Added sales data file (sales.xlsx)
- Implemented Word2Vec model loading (w2v.py) - using pre-trained model

## Project Overview
This is a product recommendation system based on natural language processing. By analyzing sales data and product descriptions, the system recommends relevant products to users.

## Project Structure
The repository currently contains the following files:
- `sales.xlsx`: Product sales data file containing product IDs, names, sales volume, and other information
- `w2v.py`: Word2Vec model script for learning vector representations of product names

## Implemented Features
1. **Data Preprocessing**: Loading and processing product sales data from Excel files
2. **Word2Vec Model**: Training word vector representations for product names to prepare for subsequent similarity calculations

## Technology Stack
- Python
- pandas (for data processing)
- gensim (for Word2Vec model)

## Usage Instructions
1. Ensure the required dependencies are installed:
   ```
   pip install pandas gensim
   ```
2. Run the `w2v.py` script to train the Word2Vec model:
   ```
   python w2v.py
   ```

## Future Plans
- Implement product similarity calculation module
- Develop recommendation algorithms
- Build a recommendation system interface
