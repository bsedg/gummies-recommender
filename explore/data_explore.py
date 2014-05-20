"""
Using Pandas, look through the data and find
any relevant statistics or correlations.
"""
import numpy as np
import pandas as pd
import json

scores = [json.loads(line) for line in open('../data/cleaned_scores.json')]
df = pd.DataFrame(scores)

# counts for each attribute
flavour_counts = df['flavour'].value_counts()
size_counts = df['size'].value_counts()
composition_counts = df['composition'].value_counts()
colour_counts = df['colour-count'].value_counts()


print "\n---------------------------------------"
print "General Statistics of Attribtues, Values"
print "---------------------------------------"

print "Flavour: \n\tsour: %d\n\tsweet: %d" % \
    (flavour_counts['sour'], flavour_counts['sweet'])
print "Size: \n\tsmall: %d\n\tmedium: %d\n\tlarge: %d" % \
    (size_counts['small'], size_counts['medium'], size_counts['large'])
print "Composition: \n\tgummy: %d\n\tmarshmallow: %d\n\tjube-jube: %d" % \
    (composition_counts['gummy'],
        composition_counts['marshmallow'],
        composition_counts['jube-jube'])
print "Colour Count: \n\t1: %d\n\t2: %d\n\t4: %d" % \
    (colour_counts[1], colour_counts[2], colour_counts[4])

print "Score breakdown:"
print df.describe()['score']

print "\n---------------------------------------"
print "Group By Attributes, Sort by Mean Score"
print "---------------------------------------"
grouped = df.groupby(['size', 'flavour', 'composition', 'colour-count'])
print grouped.mean().sort('score', ascending=False)
