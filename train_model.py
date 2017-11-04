from sklearn.datasets import load_files
from sklearn import feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import linear_model
from sklearn import metrics
from sklearn import pipeline

# Get the data from data set
dataset = load_files('Data/paragraphs')

# Split train and test data
print("Splitting data...")
train_count = round(dataset.filenames.shape[0]*8/10)

train_files = [open(f).read() for f in dataset.filenames[:train_count]]
test_files = [open(f).read() for f in dataset.filenames[train_count:]]

y_train = dataset.target[:train_count]
y_test = dataset.target[train_count:]

# Create model
print("Creating model...")
vectorizer = feature_extraction.text.TfidfVectorizer(ngram_range=(1, 6),
                             analyzer='char',)
pipe = pipeline.Pipeline([
    ('vec', vectorizer),
    ('clf', linear_model.LogisticRegression())
])

# Train model
print("Training model...")
pipe.fit(train_files, y_train)

# Obtain metrics
y_predicted = pipe.predict(test_files)
print(metrics.classification_report(y_test, y_predicted, target_names=dataset.target_names))

sentences = [
    'Je ne dis pas ce que je faisais',
    'Ich habe nich erzahlt was ich gemacht habe',
    'Yo no dije lo que hice',
    'I did not say what I have done',
    'We zijn beiden beter gescheiden, maar mijn hart zal altijd van jou zijn',
    'Non ho detto quello che ho fatto'
]

predicted = pipe.predict(sentences)
for s, p in zip(sentences, predicted):
    print ('The language of {} is --> {}'.format(s, dataset.target_names[p]))