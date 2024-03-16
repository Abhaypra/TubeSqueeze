!pip install -q transformers
!pip install youtube-transcript-api
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
youtube_video = "https://www.youtube.com/watch?v=FnaOb4wtJDk"
video_id = youtube_video.split("v=")[1]
transcript = YouTubeTranscriptApi.get_transcript(video_id)
result = ""
for entry in transcript:
    result += ' ' + entry['text']
summarizer = pipeline("summarization")
num_iters = int(len(result) / 1000)
summarized_text = []
for i in range(0, num_iters + 1):
    start = i * 1000
    end = (i + 1) * 1000
    out = summarizer(result[start:end])
    out = out[0]
    out = out['summary_text']
    summarized_text.append(out)
final_summary = ' '.join(summarized_text)
print(final_summary)
