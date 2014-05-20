gummies-recommender/explore
===================

Exploration of the data and some summaries to describe the current data set.


### Preparing the data

1. Clone repository
2. Run the *normalize_data.sh* script from the /data directory (only one data set is in the repo for size considerations)
3. Run *data_explore.py* and view the results

### Data Summary
As shown below, all the attributes are almost evenly distributed as seen to be about 50%, 50% split for two types of the attribute and about 33%, 33%, 33% split for three types of the attribtue.

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
