#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:47:11 2021

@author: Eduardo
"""
import dictionary_pt_en as dic


def translate(sentence):
    """Translate words from English to Portuguese.

    Parameters
    ----------
    sentence : str
        The sentence that will be translated.

    Returns
    -------
    str
        The original sentence and its word-by-word translation.

    """
    translated_words = []

    for word in sentence.lower().split():
        translated_words.append(dic.dictionary.get(word, '[no translation]'))

    translation = ' '.join(translated_words)

    print(f'{sentence} -> {translation}')


# Translation examples with different sentences

sentence1 = 'We are happy'
sentence2 = 'I am happy'
sentence3 = 'She is happy'
sentence4 = 'They are happy'

for sentence in [sentence1, sentence2, sentence3, sentence4]:
    translate(sentence)
