from openai import OpenAI


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
    responses = transcribe(['7264854465667288362','7276331462708743466'])