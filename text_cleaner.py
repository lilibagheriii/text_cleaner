import string

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

if __name__ == "__main__":
    sample_text = "Hello, World! This is a sample text with punctuation."
    cleaned = clean_text(sample_text)
    print("Original:", sample_text)
    print("Cleaned:", cleaned)
