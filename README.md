# Song-Language-Predictor

AI project capable of predicting the language of any song.

## Installation
1. Clone repo
2. Create a new virtual environment
3. In the new virtual env install requirements ```pip install requirements.txt```
4. Run ```python detector_application.py```
5. You should have the app running

<img src="https://github.com/EduardoVaca/Song-Language-Predictor/blob/master/Img/app_running.png" width="600" height="490">

You can search for any song to predict the language.

Activate "Show Snippets" to see which part of the lyrics was used for prediction:

<img src="https://github.com/EduardoVaca/Song-Language-Predictor/blob/master/Img/app_searching.png" width="600" height="600">

## Models
This project has two models to choose from:
- **Logistic Regression** (default)

Has 98% accuracy with the following confussion matrix:

<img src="https://github.com/EduardoVaca/Song-Language-Predictor/blob/master/Img/logistic_regression.png" width="650" height="500">

- **Multinominal Naive Bayes**

Has 93% accuracy with the following confussion matrix:

<img src="https://github.com/EduardoVaca/Song-Language-Predictor/blob/master/Img/naive_bayes.png" width="650" height="500">

## Supporting new languages
Due to the dataset is generated using Wikipedia, you can support any language you want:
1. Add the the words in the language you want to support to the search dictionaries at ```fetch_data_wikipedia.py```
```
love = {
    'en': 'Love',
    'fr': 'Amour',
    'es': 'Amor',
    'de': 'Liebe',
    'it': 'Amore',
    'nl': 'Liefde'
}

person = {
    'en': 'Person',
    'fr': 'Nom (grammaire)',
    'es': 'Persona',
    'de': 'Person',
    'it': 'Persona fisica',
    'nl': 'Mens'
}

world = {
    'en': 'World',
    'fr': 'Monde (univers)',
    'es': 'Mundo',
    'de': 'Welt',
    'it': 'Mondo',
    'nl': 'Aarde (planeet)'
}
```
2. Run ```python fetch_data_wikipedia.py``` to generate the new dataset
3. Run ```python train_model.py``` to train the model with new data
