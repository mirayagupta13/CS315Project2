# CS315Project2
### Abstract
##### Though TikTok’s primary purpose is as an entertainment platform, about a third of its adult users regularly use it as a source of news. Prior research has found a lack of news-related recommendations made by TikTok’s algorithm. These explorations used accounts made from scratch, which do not measure the longitudinal behavior of the algorithm as seen with real users. In this paper, we analyze user exposure to and engagement with news content on TikTok using data collected via data donation from real users. Our study analyzed 17,299 browsed videos from 4 participants to categorize news content with the help of the New York Times API, conducted cosine similarity analysis on each, and used K-means clustering to understand the distribution of videos across different NYT news categories. Our results show that <0.01% of browsed videos were from verified news accounts and the videos with highest cosine similarity to news articles belong to culture and style sections. This study provides insight into how real TikTok users engage with news content on the platform. 

###### File Details
Clustering_code_final.ipynb - Embeds all video descriptions with cosine similarity > 0.55 from the cosine similarity results CSV files
~ Uses K-means clustering to cluster the video descriptions based on embedding similarity

Whisper_transcribe.py - Visualizes the results of the clustering in a color-coded TSNE graph
~ Downloads videos according to cosine similarities, taken from data found in the cosine_data subfolder
~ Runs videos through OpenAI’s Whisper transcription service to create a dictionary with video name mapping to transcript
~Transcript dictionary is saved to a JSON file and processed by other files


Whisper_statistics.ipynb - Similar to cosine_nyt.ipynb, whisper_statistics ultimately computes cosine similarities for a set of videos
~ Code to access the New York Times Archive API first downloads the archive from 2023 and up to March 2024 to JSON files
~ A function to retrieve the articles given a month and year is defined to allow time-wise comparison of TikTok video transcription to New York Times articles published in the same month
~ Transcription data from running `python whisper_transcribe.py` is loaded from the file transcripts.json
~ The Sent2Vec Python library is loaded and a vectorizer is instantiated
~ The vectorizer is then run on each transcript, then on each set of headlines whose month corresponds to the video publication date
~ The maximum cosine similarity between transcript and headline is recorded in a Pandas DataFrame
~ The DataFrame containing the original cosine similarities, relevant metadata such as video description, and the transcription cosine similarity is saved into a .csv file called transcript_similarities.csv

Other files are detailed in the paper linked below:
[final research paper](https://docs.google.com/document/d/1aOvFnE1fKoCGNP9J-o_ROTLtc4zRh_13V3N31wnRFtU/edit?usp=sharing)
