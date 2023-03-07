import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Define a set of reference texts to compare the input text to
reference_texts = [
    "This is the first reference text.",
    "Here is the second reference text.",
    "And here is a third reference text."
]

# Define a function to preprocess the input text (tokenize, remove stopwords, and stem)
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Stem the remaining words
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

    # Return the preprocessed text as a string
    return ' '.join(stemmed_tokens)

# Get input text from the user
input_text = input("Enter your text: ")

# Preprocess the input text
preprocessed_input_text = preprocess_text(input_text)

# Check for plagiarism by comparing the preprocessed input text to each reference text
for reference_text in reference_texts:
    preprocessed_reference_text = preprocess_text(reference_text)

    # Calculate the Jaccard similarity coefficient between the preprocessed input text and reference text
    intersection = set(preprocessed_input_text.split()) & set(preprocessed_reference_text.split())
    union = set(preprocessed_input_text.split()) | set(preprocessed_reference_text.split())
    jaccard_similarity = len(intersection) / len(union)

    # If the Jaccard similarity coefficient is above a certain threshold, consider it plagiarism
    if jaccard_similarity >= 0.5:
        print("Plagiarism detected!")
        break
else:
    print("No plagiarism detected.")
