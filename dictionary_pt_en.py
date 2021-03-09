#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:41:10 2021

@author: Eduardo
"""
# Templates to construct the dictionary

template = """
    We are intelligent
    She is beautiful
    It is easy
    I am happy
    He sat under a tree
    The book is on the table
    A gang stood in front of me
    The castle was heavily bombed during a war
    He works at a hotel
    I tripped over the cat
    I really appreciate your help
    You dropped your wallet
    I am not sure
    I am learning English
    See you tomorrow
    """

template_translation = """
    Nós somos inteligentes
    Ela é bonita
    Isto é fácil
    Eu sou feliz
    Ele sentou sob um árvore
    O livro está sobre a mesa
    Uma gangue ficou em frente de mim
    O castelo foi pesadamente bombardeado durante a guerra
    Ele trabalha em um hotel
    Eu tropecei sobre o gato
    Eu realmente aprecio sua ajuda
    Você derrubou sua carteira
    Eu não estou certo
    Eu estou aprendendo inglês
    Vejo você amanhã
    """

# Construct the dictionary

dictionary = {}

for word, translation in zip(template.split(), template_translation.split()):
    dictionary[word.lower()] = translation.lower()
