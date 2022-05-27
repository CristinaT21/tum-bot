import nltk

from scrapper_module import InfoPageScrapper
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download("punkt")

scrapper = InfoPageScrapper("https://en.wikipedia.org/wiki/Cosine_similarity")

data_text = scrapper.get_paragraphs_text()
data_sentences = nltk.sent_tokenize(data_text)


def chatbot_response(current_user_request):

    # Add the user request to the list of sentences.
    data_sentences.append(current_user_request)

    # Create an instance of TF-IDF vectorizer and the sentence vectors.
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(data_sentences)

    # Measure the similarity with the sentences from the corpus.
    # Take the second most similar sentence (the most similar is the request itself).
    vector_values = cosine_similarity(sentence_vectors[-1], sentence_vectors)
    response = data_sentences[vector_values.argsort()[0][-2]]

    input_check = vector_values.flatten()
    input_check.sort()

    if input_check[-2] == 0:
        return "Please try again..."
    else:
        return response


print("Hello,\nI'm a chatbot. What would you like to know about cosine similarity?\n")

while True:
    user_request = input().lower()

    if user_request not in ["bye", "ciao", "good bye", "take care"]:
        print(chatbot_response(user_request))
        data_sentences.remove(user_request)
    else:
        print("See you again...")
