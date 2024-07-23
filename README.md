# Netflix Title Analysis
Welcome to the Netflix Title Analysis project! This repository contains a comprehensive analysis of Netflix titles over the years, focusing on extracting and visualizing the most influential words in titles using TF-IDF. This project showcases how the thematic elements of Netflix titles have evolved over time, providing insights into content trends and changes.

# Overview
This project utilizes natural language processing (NLP) techniques to analyze Netflix titles and visualize key trends. The analysis is performed using TF-IDF to rank words based on their importance in titles for each year. The results are presented as word clouds, which are then combined into an animated GIF to illustrate the evolution of prominent words over time.

# Features
Text Cleaning: Remove numbers, convert text to lowercase, strip punctuation, and exclude specific names.
TF-IDF Analysis: Apply TF-IDF to identify and rank the most significant words in Netflix titles.
Word Clouds: Generate and visualize word clouds to highlight the most relevant words for each year.
Animated GIF: Create a GIF showing how the most important words in Netflix titles have changed from year to year.
# Files
data/netflix_titles.csv: The dataset used for analysis, containing Netflix titles and release years.
notebooks/analysis_notebook.ipynb: Jupyter Notebook with the code for data cleaning, analysis, and visualization.
wordclouds/: Directory where word cloud images are saved.
wordclouds/wordclouds.gif: Animated GIF visualizing word cloud changes over the years.
