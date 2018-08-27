#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Phrase generator.

Naively iterates through string templates and interpolates keywords.

The algorithm doesn't know how to allow keywords to respond to other keywords, such as informing nouns that follow numbers to convert to a plural form.
"""

import random


def main():
  tmp = random.choice(templates)
  while containsKeyword(tmp):
    keyword = getKeyword(tmp)
    item = getRandomCategoryItem(keyword)
    tmp = insertItem(item, tmp)
  print(tmp)


def containsKeyword(string):
  return string.find('#') > 0


def getKeyword(string):
  if containsKeyword(string):
    (start, keyword, end) = string.split('#', 2)
    return keyword;
  else:
    return ''


def getRandomCategoryItem(category):
  if category in atlas:
    categoryList = atlas[category]
    return random.choice(categoryList)
  else:
    return ''


def insertItem(item, string):
  if containsKeyword(string):
    (start, keyword, end) = string.split('#', 2)

    if wordRequiresNewArticle(item):
      start = rectifyLastArticle(start)

    return start+item+end


def rectifyLastArticle(phrase):
  """ changes a phrase ending in ' a' to end in ' an' """
  if phrase[len(phrase)-3:len(phrase)] == ' a ':
    #...
    return phrase[:len(phrase)-3] + ' an '
  else:
    return phrase
  

def wordRequiresNewArticle(word):
  """ word that starts with a vowel or otherwise requires an 'an' """
  vowels = ['a', 'e', 'i', 'o', 'u']
  return word[0] in vowels


nouns = ['joker', 'cow', 'toaster oven', 'idiot', 'octopus']
locations = ['bathtub', 'very small #noun#']
adjectives = ['beautiful', 'purple']
past_verbs = ['destroyed']
numbers = ['six', 'one hundred']

templates = [
  'Once upon a time there was a #noun# who lived in a #location#.',
  'A #adjective# #noun# at the #location# once #past verb# a #noun#.'
]

atlas = {
  'noun': nouns,
  'location': locations,
  'adjective': adjectives,
  'past verb': past_verbs,
  'number': numbers,
}


main()
