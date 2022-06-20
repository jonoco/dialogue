#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Phrase generator.

Naively iterates through string templates and interpolates keywords.

The algorithm doesn't know how to allow keywords to respond to other keywords,
 such as informing nouns that follow numbers to convert to a plural form.
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
    return keyword
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
  """ changes a phrase ending in 'a' to end in 'an' """
  if phrase[len(phrase)-3:len(phrase)] == ' a ':
    return phrase[:len(phrase)-3] + ' an '
  else:
    return phrase
  

def wordRequiresNewArticle(word):
  """ word that starts with a vowel or otherwise requires an 'an' """
  vowels = ['a', 'e', 'i', 'o', 'u']
  return word[0].lower() in vowels if len(word) else False


nouns = ['joker', 'cow', 'toaster oven', 'idiot', 'octopus']
locations = ['in the bathtub', 'by a very small #noun#', 'underneath the #noun#', 'at the market']
adjectives = ['beautiful', 'purple', 'heavy', 'light', 'unbelievably #adjective#']
past_verbs = ['destroyed', 'murdered', 'pickled', 'yeeted', 'sat on', 'enslaved']
numbers = ['six', 'one hundred', 'eleventeen']
pronouns = ['he', 'she', 'they']

templates = [
  'Once upon a time there was a #noun# who lived #location#.',
  'A #adjective# #noun# #location# once #past verb# a #noun#.',
  'Because, a #noun# tastes good with a #adjective# #noun#.',
  'I never knew any #noun#s, but I once knew #numbers# #adjective# #noun#',
  'The last #noun# who moves gets a face full of #adjective# #noun# in their #location#',
  'But #pronoun# is an #adjective#',
]

atlas = {
  'noun': nouns,
  'location': locations,
  'adjective': adjectives,
  'past verb': past_verbs,
  'number': numbers,
  'pronoun': pronouns,
}


main()
