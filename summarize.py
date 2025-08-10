from transformers import pipeline

class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        print("Loading summarization model... (this may take a minute on first run)")
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, length="medium"):
        """Summarize text based on desired length."""
        if length == "short":
            min_len, max_len = 30, 80
        elif length == "medium":
            min_len, max_len = 80, 150
        else:  # long
            min_len, max_len = 150, 250

        return self.summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )[0]['summary_text']
