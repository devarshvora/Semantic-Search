import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

# Connect to Elasticsearch
username = "devarsh"
password = "devarsh"
es = Elasticsearch(["http://localhost:9200"], basic_auth=(username, password))
index_name = "1000_topmovies"

# Load the pre-trained model
model_name = "all-mpnet-base-v2"
model = SentenceTransformer(model_name)

# Function to perform semantic search
def semantic_search(query, es, model):
    # Embed the query
    query_embedding = model.encode([query])[0]
    
    # Search similar embeddings
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": query_embedding.tolist()}
            }
        }
    }
    
    # Search with custom scoring
    results = es.search(index=index_name, body={"size": 5, "query": script_query})
    
    return results['hits']['hits']

# Function to display results
def display_results(results):
    st.subheader("Search Results:")
    for i, result in enumerate(results):
        text = result['_source']['text']
        series_title, genre, overview, director = text.split('\n')
        
        # Display information
        st.write("Result", i + 1)
        st.write("Series Title:", series_title)
        st.write("Genre:", genre)
        st.write("Overview:", overview)
        st.write("Director:", director)
        
        if i != len(results) - 1:
            st.write("---")

# Set page config
st.set_page_config(
    page_title="Semantic Search App",
    page_icon=":mag:",
    layout="wide"
)


# Custom CSS for design
st.markdown("""
    <style>
        body {
            color: #FFFFFF;
            background-color: #000000; /* Set a fallback background color */
            font-size: 24px; /* Adjust font size */
        }
        .stApp {
            background-color: transparent; /* Remove default background color */
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
            font-size: 24px; /* Adjust font size */
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        #video-background {
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%; 
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -1000;
            background-size: cover;
            transition: 1s opacity;
        }
        .content {
            position: fixed;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            width: 100%;
            padding: 20px;
            text-align: center;
            font-size: 28px; /* Adjust font size */
            text-shadow: 0px 0px 5px rgba(255, 255, 255, 0.5); /* Add glow effect */
        }
    </style>
""", unsafe_allow_html=True)

# Video background
st.markdown("""
    <video autoplay loop muted id="video-background">
        <source src="https://videos.pexels.com/video-files/7988642/7988642-uhd_4096_2160_25fps.mp4">
        Your browser does not support the video tag.
    </video>
""", unsafe_allow_html=True)

# Title and description
st.title("🔍 Semantic Search App")
st.markdown("Welcome to the Semantic Search App! Enter your query below and get relevant results.")

# Input query
query = st.text_input("Enter your query:", "")

# Button to perform search
if st.button("Search", key="search_button"):
    if query:
        # Perform semantic search
        results = semantic_search(query, es, model)
        # Display results
        display_results(results)

# Footer
st.markdown("<hr class='footer'>", unsafe_allow_html=True)
st.markdown("Created with ❤️ by Devarsh")
