"""
weighted_recommendation.py

Task:
Given a (newline-delimited JSON) file of data, investigate correlation(s)
between the score and the rest of the attributes. Think in the context of
preparing a report for a gummy worm factory trying to decided how to tweak
their next production run. How many of each type should be produced in order to
saturate the market without oversupplying? (Ratios between attributes are fine;
no need to figure out how many units need to be produced.)

Solution:

"""
from __future__ import print_function, division
import sys
import getopt
import pandas as pd
import json
import math


ATTRIBUTES = ['size', 'flavour', 'composition', 'colour-count']


def calculate_weight(score, average_score, total_combinations):
    """
    Calculates a new ratio, weight for the attribute combination
    based on score, average of the scores, and total number of
    combinations of given attribtues.
    """
    average_percentage = 100.0 / total_combinations
    print("\tAve Percent: %f" % average_percentage)

    diff_from_average_score = score - average_score
    print("\tDiff from ave: %f" % diff_from_average_score)
    percentage_change = diff_from_average_score * 10
    print("\tPercent change: %f" % percentage_change)

    # add the percentage change to the average percentage
    return average_percentage + (average_percentage * percentage_change)

def find_weights(df, attributes):
    """
    df: DataFrame (pandas) for the loaded data
    attributes: String value of the attribute
    """
    grouped = df.groupby(attributes)
    groupby_mean = grouped.mean().sort('score', ascending=False)
    generator_rows = groupby_mean.iterrows()
    rows = [row for row in generator_rows]
    total_scores = sum(float(x[1].values[0]) for x in rows)
    average_score = total_scores / len(rows)

    result = {}
    for row in rows:
        #result[row[0]] = math.abs(row[1].values[0] - average_score)
        print(row[0])
        print("\tWeight: %f" % calculate_weight(float(row[1].values[0]), average_score, len(rows)))


def main(argv):
    scores = [json.loads(line) for line in open('../data/cleaned_scores.json')]
    df = pd.DataFrame(scores)
    find_weights(df, ATTRIBUTES)

if __name__ == '__main__':
    main(sys.argv[1:])
