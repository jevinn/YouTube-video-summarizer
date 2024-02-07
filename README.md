# YTtranscriber

YTtranscriber is a simple Streamlit web application that converts YouTube video transcripts into summarized notes. It utilizes Google's GenerativeAI API to generate concise summaries of video transcripts.

## Features
- Converts YouTube video transcripts into summarized notes.
- Provides important points from the video transcript within 250 words.

## Installation
1. Clone the repository:

```bash
git clone https://github.com/jevinn/YouTube-video-summarizer.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
1. Ensure you have set up your Google API key and saved it in a `.env` file. You can obtain a Google API key from the Google Cloud Console.
2. Run the Streamlit application:

```bash
streamlit run main.py
```

3. Enter the YouTube video link in the provided text input field.
4. Click the "Get detailed notes" button.
5. The application will display summarized notes extracted from the YouTube video transcript.

## Dependencies
- Streamlit
- dotenv
- google.generativeai
- youtube_transcript_api


## Acknowledgements
- This project utilizes Google's GenerativeAI API and the YouTube Transcript API for transcript extraction.
