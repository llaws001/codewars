def reverse_words(text):
    return " ".join([i[::-1] for i in text.split(" ")])
reverse_words('this is a test')