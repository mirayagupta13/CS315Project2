import pandas as pd
import numpy as np
from openai import OpenAI
from cs315project2datacollection.download_videos import download_tiktok_mp3s

def generate_video_id_list():
    # Read the CSV file containing cosine similarities
    df = pd.read_csv("./cosineSimilarites.csv")
    df = df[df['score_news'].notnull()]
    # Pandas DF Cols: video id, description, similarities
    df = df.sort_values(by=['score_news'], ascending=False)

    # sort by cosine similarity, in order of greatest similarity
    files_to_transcribe = df.iloc[:10]['video_id']
    # print(files_to_transcribe)
    return files_to_transcribe.values.tolist(), df

def transcribe(video_ids=[]):
    filenames = [f"share_video_{id}_.mp3" for id in video_ids]

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
    files, df = generate_video_id_list()
    for file in files:
        print(type(file))
        print(int(file))
    # download_tiktok_mp3s(files)
    # responses = transcribe([])
    # print(responses)

# Usage: python whisper_stats.py