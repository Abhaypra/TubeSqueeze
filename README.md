
# YouTube Transcript Summarization
This Python script aims to summarize the transcript of a YouTube video using the transformers library for natural language processing tasks and the youtube-transcript-api to fetch the transcript from a YouTube video.

## he script follows these steps:

Fetches the transcript of the YouTube video using the YouTubeTranscriptApi.
Concatenates all the text entries from the transcript into a single string.
Splits the concatenated string into chunks of 1000 characters (since the summarization model has a maximum input length limit).
Uses the Hugging Face summarization pipeline to summarize each chunk of text.
Concatenates the summarized text chunks into a final summary.
