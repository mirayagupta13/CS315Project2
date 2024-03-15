import pandas as pd
import numpy as np
from openai import OpenAI

# Read the CSV file containing cosine similarities
df = pd.read_csv("cosine_similarities.csv")

# Pandas DF Cols: video id, description, similarities
df.sort_values(by=['similarities'], ascending=False)
# sort by cosine similarity, in order of greatest similarity
files_to_transcribe = df.iloc[:300]['video_id']


def transcribe(video_ids=[]):
    filenames = [f"share_video_{id}_.mp4" for id in video_ids]

    client = OpenAI(api_key='my-api-key-here')

    responses = {}

    for filename in filenames:
        audio = open(filename, "rb")
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
        responses[filename] = transcription

    return responses

if __name__ == "__main__":
    responses = transcribe([])