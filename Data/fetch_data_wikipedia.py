"""
Script to generate dataset for language detector
Data obtained from wikipedia
Author: Eduardo Vaca
"""
import os
import wikipedia

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

text_folder = 'paragraphs'

for searchs in [love, person, world]:
    for lang, search in searchs.items():
        
        # Create folder of current lang class
        text_lang_folder = os.path.join(text_folder, lang)
        if not os.path.exists(text_lang_folder):
            os.makedirs(text_lang_folder)

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