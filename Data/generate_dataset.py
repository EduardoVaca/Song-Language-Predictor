"""
Script to generate dataset for language detector
Data obtained from wikipedia
Author: Eduardo Vaca
"""

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

ds_file = open("languages_data.txt", "w")
for searchs in [love, person, world]:
    for lang, search in searchs.items():
        print('Getting {} in {} from wikipedia...'.format(search, lang))
        wikipedia.set_lang(lang)
        search_page = wikipedia.page(search)
        sentences = search_page.content.split('\n')
        print('Writing...')
        for sentence in sentences:
            if '==' not in sentence and '===' not in sentence and sentence and (len(sentence) > 30 or ':' not in sentence):
                ds_file.write('{}-->{}\n'.format(lang, sentence))
ds_file.close()

