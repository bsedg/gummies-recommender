gummies-recommender/explore
===================

Exploration of the data and some summaries to describe the current data set.


### Preparing the data

1. Clone repository
2. Run the **normalize_data.sh** script from the /data directory (only one data set is in the repo for size considerations)
3. Run **data_explore.py** and view the results

*Setting up the python script:*

```python
"""
Using Pandas, look through the data and find
any relevant statistics or correlations.
"""
import numpy as np
import pandas as pd
import json
```

### Data Summary
As shown below, all the attributes are almost evenly distributed as seen to be about **50%, 50%** split for two types of the attribute and about **33%, 33%, 33%** split for three types of the attribtue.

```python
scores = [json.loads(line) for line in open('../data/cleaned_scores.json')]
df = pd.DataFrame(scores)

# counts for each attribute
flavour_counts = df['flavour'].value_counts()
size_counts = df['size'].value_counts()
composition_counts = df['composition'].value_counts()
colour_counts = df['colour-count'].value_counts()
```

* Flavour:
 * sour: 500588
 * sweet: 499412
* Size: 
 * small: 333693
 * medium: 333192
 * large: 333115
* Composition: 
 * gummy: 332676
 * marshmallow: 332780
 * jube-jube: 334544
* Colour Count: 
 * 1: 333478
 * 2: 333698
 * 4: 332824

**Score Breakdown**

```python
print "Score breakdown:"
print df.describe()['score']
```

| Statistic | Value    |
|:---------:|:--------:|
| count     | 1000000  |
| mean      | 0.562416 |
| std       | 0.042380 |
| min       | 0.450052 |
| 25%       | 0.532173 |
| 50%       | 0.563113 |
| 75%       | 0.592831 |
| max       | 0.689527 |


#### Group by data attribtues, find mean score for each combination, sort by score
As shown in the data summary below, the highest scoring combinations include large size and sweet flavour while sour flavour and jube-jube composition had some of the lowest scoring. A quick eye test comparison shows that it appears that the scores min, max, mean, and quartiles all seem to be almost identical in attribute combination score order.

```python
grouped = df.groupby(['size', 'flavour', 'composition', 'colour-count'])
print grouped.mean().sort('score', ascending=False)
```
                                            
|size   |flavour |composition |colour-count  |score
| ----- | ------ | ---------- | ------------ | ------   
|large  |sweet   |gummy       |1             |0.659869
|       |        |marshmallow |1             |0.637743
|       |        |gummy       |2             |0.636223
|       |        |            |4             |0.630573
|medium |sweet   |gummy       |1             |0.622481
|large  |sour    |gummy       |1             |0.617401
|       |sweet   |marshmallow |2             |0.614145
|       |        |            |4             |0.608395
|       |        |jube-jube   |1             |0.602973
|small  |sweet   |gummy       |1             |0.600937
|medium |sweet   |marshmallow |1             |0.600355
|       |        |gummy       |2             |0.598938
|large  |sour    |marshmallow |1             |0.595261
|       |        |gummy       |2             |0.593780
|medium |sweet   |gummy       |4             |0.593221
|large  |sour    |gummy       |4             |0.588081
|medium |sour    |gummy       |1             |0.580002
|large  |sweet   |jube-jube   |2             |0.579359
|small  |sweet   |marshmallow |1             |0.578841
|       |        |gummy       |2             |0.577337
|medium |sweet   |marshmallow |2             |0.576651
|large  |sweet   |jube-jube   |4             |0.573635
|small  |sweet   |gummy       |4             |0.571623
|large  |sour    |marshmallow |2             |0.571542
|medium |sweet   |marshmallow |4             |0.571055
|large  |sour    |marshmallow |4             |0.565894
|medium |sweet   |jube-jube   |1             |0.565575
|large  |sour    |jube-jube   |1             |0.560469
|small  |sour    |gummy       |1             |0.558465
|medium |sour    |marshmallow |1             |0.557831
|       |        |gummy       |2             |0.556269
|small  |sweet   |marshmallow |2             |0.555185
|medium |sour    |gummy       |4             |0.550679
|small  |sweet   |marshmallow |4             |0.549420
|       |        |jube-jube   |1             |0.544014
|medium |sweet   |jube-jube   |2             |0.541895
|large  |sour    |jube-jube   |2             |0.536729
|small  |sour    |marshmallow |1             |0.536321
|medium |sweet   |jube-jube   |4             |0.536251
|small  |sour    |gummy       |2             |0.534735
|medium |sour    |marshmallow |2             |0.534109
|large  |sour    |jube-jube   |4             |0.531074
|small  |sour    |gummy       |4             |0.529081
|medium |sour    |marshmallow |4             |0.528581
|       |        |jube-jube   |1             |0.523052
|small  |sweet   |jube-jube   |2             |0.520385
|       |        |            |4             |0.514743
|       |sour    |marshmallow |2             |0.512672
|       |        |            |4             |0.506971
|       |        |jube-jube   |1             |0.501528
|medium |sour    |jube-jube   |2             |0.499388
|       |        |            |4             |0.493666
|small  |sour    |jube-jube   |2             |0.477826
|       |        |            |4             |0.472160
