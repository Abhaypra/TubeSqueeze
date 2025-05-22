# 📺 TubeSqueeze: YouTube Transcript Summarizer

TubeSqueeze is a Python-based tool that automatically fetches the transcript of a YouTube video and generates a concise summary using state-of-the-art natural language processing (NLP) models from Hugging Face’s Transformers library.

## ✨ Features

* 📤 Fetches YouTube video transcripts using `youtube-transcript-api`
* 🧠 Summarizes long transcripts using Hugging Face's transformer models
* 🔍 Automatically handles large transcripts by splitting them into manageable chunks
* 📃 Generates a concise, readable summary of the entire video content

## 🛠️ Installation

Make sure you have Python 3.7 or higher installed. Then, install the required libraries:

```bash
pip install youtube-transcript-api transformers torch
```

> Note: `torch` is required for most transformer models to work properly.

## 📝 How It Works

1. **Transcript Extraction:**
   Retrieves the full transcript using `YouTubeTranscriptApi`.

2. **Concatenation & Chunking:**
   Merges the transcript and splits it into chunks (default 1000 characters) for model input limits.

3. **Summarization:**
   Uses Hugging Face’s transformer-based summarization pipeline to process each chunk.

4. **Final Output:**
   Combines all summarized chunks into a single, coherent summary.

## 🧪 Example Output

**Input Video:** "How GPT-4 Works"
**Output Summary:**

> GPT-4 is a large multimodal model developed by OpenAI. It can accept both text and image inputs and generate human-like text outputs. The model demonstrates improved performance, reasoning, and contextual understanding over previous versions...

## 🔧 Configuration

* Customizable chunk size to fit various transformer models.
* Option to switch summarization models from Hugging Face Model Hub.

## 📌 Limitations

* Only works for videos with available transcripts.
* Summarization quality depends on the selected model and transcript clarity.
* Processing long videos may require more time and memory.

## 📚 Dependencies

* `youtube-transcript-api`
* `transformers`
* `torch`

## 💡 Future Enhancements

* Add a graphical interface (GUI) using Streamlit or Tkinter
* Support exporting summaries to `.txt` or `.pdf`
* Enable multi-language transcript support
* Integrate with YouTube API for fetching video metadata

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

