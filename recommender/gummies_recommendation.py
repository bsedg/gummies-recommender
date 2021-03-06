"""
gummies_recommendation.py

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
import operator


ATTRIBUTES = ['size', 'flavour', 'composition', 'colour-count']
OUTPUT_TYPES = ['markdown', 'json']


def calculate_weight(score, average_score, total_combinations, bias=1.0):
    """
    Calculates a new ratio, weight for the attribute combination
    based on score, average of the scores, and total number of
    combinations of given attribtues.
    """
    average_percentage = 100.0 / total_combinations
    diff_from_average_score = score - average_score
    percentage_change = diff_from_average_score * bias

    # add the percentage change to the average percentage
    return average_percentage + (average_percentage * percentage_change)

def find_weights(df, attributes, bias=1.0):
    """
    df: DataFrame (pandas) for the loaded data
    attributes: String value of the attribute
    bias: A coefficient to create more skewed percentages
        for each attribute combination (1 is default).
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
            "weight": calculate_weight(float(row[1].values[0]), average_score, len(rows), bias)
        }

    return result


def get_combination_display_string_markdown(combination_tuple, is_all=True):
    """
    For all the attribtues, the string in the tuple from
    the dataframe is (u'small', u'sour', u'jube-jube', 4)
    """
    if is_all:
        return "%s, %s, %s, %s colours" % (combination_tuple[0], combination_tuple[1], combination_tuple[2], combination_tuple[3])
    else:
        return "%s" % (combination_tuple)

def get_combination_display_string_json(combination_tuple, attribute, is_all=True):
    """
    For all the attribtues, the string in the tuple from
    the dataframe is (u'small', u'sour', u'jube-jube', 4)
    """
    output = {}
    if is_all:
        output['size'] = combination_tuple[0]
        output['flavour'] = combination_tuple[1]
        output['composition'] = combination_tuple[2]
        output['colour-count'] = combination_tuple[3]
        return output
    else:
        return { attribute: combination_tuple }


def find_biased_distribution(weighted_ratios, output, attribute, is_all=True):
    """
    Unlike the fair distribution, this approach uses an unbounded knapsack
    inspired algorithm to calculate the highest score to be placed in the
    distribution based on the calculated weight.
    """
    sorted_weights = sorted(weighted_ratios.iteritems(), key=operator.itemgetter(1), reverse=True)

    total_ratio = 0.0
    if output == 'markdown':
        print('| %s | Percentage |' % ('Attribute Combination' if is_all else attribute))
        print('| ----- | ------ |')

    for sorted_weight in sorted_weights:
        total_ratio_remaining_after_add = 100.0 - sorted_weight[1]['weight']
        total_ratio += sorted_weight[1]['weight']

        if output == 'markdown':
            print("| %s | %f |" % (get_combination_display_string_markdown(sorted_weight[0], is_all), sorted_weight[1]['weight']))
        else:
            output_json = { 
                "ratio": sorted_weight[1]['weight'],
                "attributes": get_combination_display_string_json(sorted_weight[0], attribute, is_all)
            }
            print(json.dumps(output_json))


def find_fair_distribution(weighted_ratios, output, attribute, is_all=True):
    """
    A fair distribution calcuation provides a 'safer' recommendation without
    the chance of eliminating any attribute combinations.
    """
    ratio_sum = sum(weighted_ratios[key]['weight'] for key in weighted_ratios.keys())
    sorted_weights = sorted(weighted_ratios.iteritems(), key=operator.itemgetter(1), reverse=True)

    if output == 'markdown':
        print('| %s | Percentage |' % ('Attribute Combination' if is_all else attribute))
        print('| ----- | ------ |')

    for sorted_weight in sorted_weights:
        if output == 'markdown':
            print("| %s | %f |" % (get_combination_display_string_markdown(sorted_weight[0], is_all), (sorted_weight[1]['weight'] / ratio_sum)))
        else:
            output_json = { 
                "ratio": (sorted_weight[1]['weight'] / ratio_sum),
                "attributes": get_combination_display_string_json(sorted_weight[0], attribute, is_all)
            }
            print(json.dumps(output_json))


def main(argv):
    # arbitrary defaults chosen if input parameters are not provided
    all_attributes = True
    attribute = 'size'
    file_name = '../data/cleaned_scores.json'
    strategy = 'fair'
    bias_coefficient = 10.0
    output = 'json'

    try:
        opts, args = getopt.getopt(argv,"hf:a:t:b:o:",["file=", "attributes=", "type=", "bias=", "output="])
    except getopt.GetoptError:
        print('gummies_recommendation.py')
        print('\t-a,--attribute [size,flavour,colour-count,composition]')
        print('\t-f,--file ../data/cleaned_scores.json -t [fair, biased]')
        print('\t-o,--output [markdown, json]')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-f", "--file"):
            file_name = arg
        elif opt in ("-a", "--attribute"):
            if arg in ATTRIBUTES:
                all_attributes = False
                attribute = arg
        elif opt in ("-t", "--type"):
            if arg in ["fair", "biased"]:
                strategy = arg
        elif opt in ("-b", "--bias"):
            try:
                bias_value = float(arg)
                bias_coefficient = bias_value
            except:
                pass
        elif opt in ("-o", "--output"):
            if arg in OUTPUT_TYPES:
                output = arg

    scores = [json.loads(line) for line in open(file_name)]
    df = pd.DataFrame(scores)

    if strategy == 'fair':
        weighted_ratios = find_weights(df, ATTRIBUTES if all_attributes else [attribute])
        find_fair_distribution(weighted_ratios, output, attribute, all_attributes)
    else:
        weighted_ratios = find_weights(df, ATTRIBUTES if all_attributes else [attribute], bias_coefficient)
        find_biased_distribution(weighted_ratios, output, attribute, all_attributes)


if __name__ == '__main__':
    main(sys.argv[1:])
