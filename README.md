
# Movie Semantic Search with Elasticsearch and Streamlit App 🔎

This project implements semantic search functionality using Elasticsearch and Sentence Transformers. Semantic search enables the retrieval of results based on the meaning and context of the query rather than just matching keywords. Specifically, in this project:

## Features

- **Semantic Search**: Indexes movie-related text data along with their embeddings generated using Sentence Transformers to understand the semantic meaning of the text.
  
- **Search Capability**: Searches through the indexed data and retrieves relevant results based on the semantic similarity between the query and the indexed text embeddings.
  
- **Movie Keyword Search**: Retrieves not only exact matches but also related movies based on semantic similarity.
  
- **Enhanced Accuracy**: Ensures relevant and related movies are returned even if they do not contain exact matching keywords.

## Flow of the Code

1. **Importing Libraries**: Necessary libraries are imported and authenticated with Kaggle API for dataset access.
  
2. **Data Preprocessing**: Dataset is downloaded and extracted from Kaggle, then read into a Pandas DataFrame. Data preprocessing steps such as selecting desired columns and cleaning the data are applied.
  
3. **Embedding and Indexing**: DataFrame is converted to a Hugging Face dataset for compatibility with NLP models. Text is embedded using Sentence Transformers to generate semantic representations. Embeddings along with corresponding text are stored in Elasticsearch for efficient semantic search capabilities.
  
4. **Semantic Search Functionality**: Functions for semantic search and printing search results are defined to check accuracy and correctness.
  
5. **Streamlit Setup**: Streamlit page configuration and custom CSS for design are set up.
  
6. **Streamlit App Creation**: Streamlit app is created with a video background, title, input query field, search button, and footer.

## Execution Instructions

### For "Elastic Search" (Main Code) File:

1. Ensure all required libraries are installed on your system along with necessary packages mentioned in the code.
  
2. Confirm that Elasticsearch is running locally on http://localhost:9200.
  
3. Before running the code, replace the Elasticsearch authentication credentials (username: devarsh and password: devarsh).
  
4. Elasticsearch will store the embeddings. Execute the last part of the code and write any query you want to search (under #Example Usage) to check if it is correctly working.

### For "Searchapp.py" File:

5. Open "Searchapp.py".
  
6. Run it with the following command:
   ```
   streamlit run Filelocation/Searchapp.py
   ```

## Output

As shown in the output, entering keywords like "Student Life" will give results of all Series Titles related to it.
![image](https://github.com/devarshvora/Semantic-Search/assets/60837459/48f91800-529f-4e7e-8812-5ed629064be9)



![image](https://github.com/devarshvora/Semantic-Search/assets/60837459/de449164-ff18-4645-9767-46a8bf97ce94)


