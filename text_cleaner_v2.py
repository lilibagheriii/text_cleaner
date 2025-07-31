import string

def clean_text(text):
    # Lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

if __name__ == "__main__":
    # Read from sample.txt
    with open("sample.txt", "r") as infile:
        raw_text = infile.read()

    # Clean the text
    cleaned_text = clean_text(raw_text)

    # Save to cleaned.txt
    with open("cleaned.txt", "w") as outfile:
        outfile.write(cleaned_text)

    print("✅ Text cleaned and saved to 'cleaned.txt'")
