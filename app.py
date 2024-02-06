import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """"you are a youutbe video transcript summarizer. you will be taking the video transcript data and summarizing the entire video and providing the important summary in points within 250 words. Please provide the summary of the text given here:"""


def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    except Exception as e:
        raise e


def generateai_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript_text)
    return response.text


st.title("YouTube transcript to notes converter")
youtube_link = st.text_input("enter YouTube video link: ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get detailed notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generateai_content(transcript_text, prompt)
        st.markdown("Detailed Notes:")
        st.write(summary)