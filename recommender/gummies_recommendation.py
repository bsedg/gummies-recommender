"""
gummies_recommendation.py

Given a (newline-delimited JSON) file of data, investigate correlation(s)
between the score and the rest of the attributes. Think in the context of
preparing a report for a gummy worm factory trying to decided how to tweak
their next production run. How many of each type should be produced in order to
saturate the market without oversupplying? (Ratios between attributes are fine;
no need to figure out how many units need to be produced.)
"""
from __future__ import print_function, division
import sys
import getopt
import pandas as pd
import json


ATTRIBUTES = ['size', 'flavour', 'composition', 'colour-count']


def find_ratios_for_attributes(df, attributes):
    """
    df: DataFrame (pandas) for the loaded data
    attributes: String value of the attribute
    """
    grouped = df.groupby(attributes)
    groupby_mean = grouped.mean().sort('score', ascending=False)
    generator_rows = groupby_mean.iterrows()
    rows = [row for row in generator_rows]
    total_scores = sum(x[1].values[0] for x in rows)
    
    result = {}
    for row in rows:
        result[row[0]] = row[1].values[0] / total_scores

    print(repr(result))

'''
def main():
    scores = [json.loads(line) for line in open('../data/cleaned_scores.json')]
    df = pd.DataFrame(scores)
    
    for attribute in ATTRIBUTES:
        find_ratios_for_attribute(df, [attribute])
'''

def main(argv):
    all_attributes = False

    try:
        opts, args = getopt.getopt(argv,"all",["all"])
    except getopt.GetoptError:
        print('gummies_recommendation.py --all')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '--all':
            all_attributes = True

    scores = [json.loads(line) for line in open('../data/cleaned_scores.json')]
    df = pd.DataFrame(scores)

    if all_attributes:
        find_ratios_for_attribute(df, ATTRIBUTES)
    else:
        for attribute in ATTRIBUTES:
            print(attribute)
            find_ratios_for_attribute(df, [attribute])
            print


if __name__ == '__main__':
    main(sys.argv[1:])
