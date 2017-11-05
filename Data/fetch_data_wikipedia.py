"""
Script to generate dataset for language detector
Data obtained from wikipedia
Author: Eduardo Vaca
"""
import os
import wikipedia
import numpy as np

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

TEXT_FOLDER = 'paragraphs'
SHORT_TEXT_FOLDER = 'sentences'
SHORT_TEXT_WORDS = 5

for searchs in [love, person, world]:
    for lang, search in searchs.items():
        
        # Create folder of current lang class for paragraphs
        text_lang_folder = os.path.join(TEXT_FOLDER, lang)
        if not os.path.exists(text_lang_folder):
            os.makedirs(text_lang_folder)

        # Create folder of current lang class for sentences
        short_lang_folder = os.path.join(SHORT_TEXT_FOLDER, lang)
        if not os.path.exists(short_lang_folder):
            os.makedirs(short_lang_folder)

        print('Getting {} in {} from wikipedia...'.format(search, lang))
        wikipedia.set_lang(lang)
        search_page = wikipedia.page(search)
        paragraphs = search_page.content.split('\n')
        
        i = 0
        for paragraph in paragraphs:
            if len(paragraph) < 100 or '==' in paragraph or '===' in paragraph:
                continue

            text_filename = os.path.join(text_lang_folder, '{}_{}_{}'.format(lang, search.split(' ')[0],i))
            open(text_filename, 'w').write(paragraph)
            i += 1

            # Split words for sentences folder
            words = paragraph.split(' ')
            n_groups = len(words)/SHORT_TEXT_WORDS
            if n_groups < 1:
                continue
            
            groups = np.array_split(words, n_groups)

            j = 0
            for group in groups:                
                sentence = ' '.join(group)
                short_text_filename = os.path.join(short_lang_folder, '{}_{}_{}_{}'.format(lang, search.split(' ')[0], i, j))
                open(short_text_filename, 'w').write(sentence)
                j += 1
                if j >= 1000:
                    break