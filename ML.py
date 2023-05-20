from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Input data
X = ["This is the first sentence.", "This is the second sentence.", "This is the third sentence."]
y = ["positive", "negative", "neutral"]

# Feature extraction
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
clf = MultinomialNB()
clf.fit(X_vectorized, y)

# Predict using trained model
new_text = ["This is a new sentence."]
new_text_vectorized = vectorizer.transform(new_text)
prediction = clf.predict(new_text_vectorized)
print(prediction)
