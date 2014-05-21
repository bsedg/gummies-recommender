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
    diff_from_average_score = score - average_score
    percentage_change = diff_from_average_score

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
        result[row[0]] = {
            "weight": calculate_weight(float(row[1].values[0]), average_score, total_scores)
        }

    return result

def find_biased_distribution(weighted_ratios):
    """
    Unlike the fair distribution, this approach uses an unbounded knapsack
    inspired algorithm to calculate the highest score to be placed in the
    distribution based on the calculated weight.
    """

def find_fair_distribution(weighted_ratios):
    """
    A fair distribution calcuation provides a 'safer' recommendation without
    the chance of eliminating any attribute combinations.
    """
    ratio_sum = sum(weighted_ratios[key]['weight'] for key in weighted_ratios.keys())
    print("| Combination | Percentage |")
    for key in weighted_ratios.keys():
        print("| %s | %f |" % (key, (weighted_ratios[key]['weight'] / ratio_sum)))

def main(argv):
    # arbitrary defaults chosen if input parameters are not provided
    all_attributes = True
    attribute = 'size'
    file_name = '../data/cleaned_scores.json'
    strategy = 'fair'

    try:
        opts, args = getopt.getopt(argv,"hf:a:t:",["file=", "attributes=", "type="])
    except getopt.GetoptError:
        print('weighted_recommendation.py -a [size,flavour,colour-count,composition] -f ../data/cleaned_scores.json -t [fair, biased]')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--file"):
            file_name = arg
        elif opt in ("-a", "--attribute"):
            if arg in ATTRIBUTES:
                all_attributes = False
                attribute = arg
        elif opt in ("-t", "--type"):
            if arg in ["fair", "biased"]:
                strategy = arg

    scores = [json.loads(line) for line in open(file_name)]
    df = pd.DataFrame(scores)

    weighted_ratios = find_weights(df, ATTRIBUTES if all_attributes else [attribute])

    if strategy == 'fair':
        find_fair_distribution(weighted_ratios)
    else:
        find_biased_distribution(weighted_ratios)


if __name__ == '__main__':
    main(sys.argv[1:])
