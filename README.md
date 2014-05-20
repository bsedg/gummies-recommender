gummies-recommender
===================

Given a set of data points for gummi worms tasting, find a recommendation of ratios of attributes for those gummi worms. 


### Problem:
Gummy worms come in a wide variety and some are more delicious than others.
Tastes are subjective so any given gummy worm probably has someone who likes
it, but focusing on more popular variations would be more cost-effective.

### Task:
Given a (newline-delimited JSON) file of data, **investigate correlation(s)**
*between the score and the rest of the attributes*. Think in the context of
preparing a report for a gummy worm factory trying to decided how to tweak
their next production run. How many of each type should be produced in order to
saturate the market without oversupplying? (Ratios between attributes are fine;
no need to figure out how many units need to be produced.)

### Facts:
Each worm
- has a size; one of
 * small
 * medium
 * large
- has a taste; one of
 * sweet 
 * sour
- has a composition; one of
 * gummy
 * marshmallow 
 * jube-jube
- has a colour scheme; one of
 * 1 colour
 * 2 colours 
 * 4 colours

#### The data was generated as follows:
1. A population of 10,000 volunteers were selected.
2. One million gummy worms were produced with random attributes.
3. For each gummy worm, a focus group was assembled from a sample of the population.
4. The sample group deliberated on the finer points, qualities and faults of the gummy worm in question.
5. The sample group assigned the worm a score from 0 to 1 based on the results of their deliberations.

## Solution
The solution is broken down into three areas:

1. The Data *[/data](./data)*
2. Some Exploration of the Data *[/explore](./explore)*
3. Code and Result for Recommendation Solution *[/recommender](./recommender)*

### [Data](./data)
The original data file is located here, [data file](./data/scores.json).

### [Data Exploration](./explore)
Exploration of the data and some summaries to describe the current data set.

### [Recommendation](./recommender)
Recommendation summary and code to make the recommendation.
