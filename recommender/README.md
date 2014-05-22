gummies-recommender/recommender
===================

Recommendation summary and code to make the recommendation.

## Recommendation Model, Calculation
The following function is what is called in the recommendation algorithm.  With the bias set at 1.0, it creates a 'fair distribution' otherwise it creates a 'biased distribution'.

#### Biased Distribution Recommendation
Calculation steps for finding the ratios for the distribution recommendation:

##### Attribute combination calculated weight
1. Find average scores per each attribute combination
2. Find average of those scores
3. Iterate through all attribute combination with their average score

    ```python
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
        ...
    ```

4. Calculate difference from current score to average of scores for the *difference*
5. Multiply the *difference* by the *bias* (could be default of just 1.0) for the *percentage change*
6. Find *average percentage* if all combinations were equal
7. Add the *average percentage* to the product of the *percentage change* and the *average percentage*

    ```python
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
    ```

## Attribute Level Distribution Ratios
These calculations show the fair distribution, which does not add extra skew for average scores over or under the average of the scores.

#### Size
These results are a very even distribution, 1/3 each attribute.

| Small | Medium | Large |
| ----- | ------ | ----- |
| 33%   | 33%    | 33%   |

#### Flavour
Mostly comes out to a 50/50 split, but there is some skew towards *sour* flavour.

| Sweet  | Sour    |
| ------ | ------- |
| 49.98% | 50.02%  |


#### Composition
Again, a very even split.

| Gummy | Marshmallow | Jube-Jube |
| ----- | ------ | ----- |
| 33.3%   | 33.3%    | 33.4%   |


#### Colour Count
Still a rather even distribution, but there is some skew toward fewer colour counts.

| 1 | 2 | 4 |
| ----- | ------ | ----- |
| 34.4% | 33.0% | 32.6% |

## Granular Distribution Ratios, With Bias Coefficient
Using a biased recommendation, bias coefficient set to 10.0, the following distribution percentages are shown in the table below.  Attribute combination scores that are above the average of the scores will have greater positive percentage change while the scores below the average will have greater negative percentage changes.

| Attribute Combination | Percentage |
| --------------------- | ---------- |
| large, sweet, gummy, 1 flavours | 3.654840 |
| large, sweet, marshmallow, 1 flavours | 3.245110 |
| large, sweet, gummy, 2 flavours | 3.216953 |
| large, sweet, gummy, 4 flavours | 3.112322 |
| medium, sweet, gummy, 1 flavours | 2.962473 |
| large, sour, gummy, 1 flavours | 2.868407 |
| large, sweet, marshmallow, 2 flavours | 2.808110 |
| large, sweet, marshmallow, 4 flavours | 2.701628 |
| large, sweet, jube-jube, 1 flavours | 2.601220 |
| small, sweet, gummy, 1 flavours | 2.563508 |
| medium, sweet, marshmallow, 1 flavours | 2.552733 |
| medium, sweet, gummy, 2 flavours | 2.526498 |
| large, sour, marshmallow, 1 flavours | 2.458397 |
| large, sour, gummy, 2 flavours | 2.430972 |
| medium, sweet, gummy, 4 flavours | 2.420627 |
| large, sour, gummy, 4 flavours | 2.325436 |
| medium, sour, gummy, 1 flavours | 2.175821 |
| large, sweet, jube-jube, 2 flavours | 2.163915 |
| small, sweet, marshmallow, 1 flavours | 2.154337 |
| small, sweet, gummy, 2 flavours | 2.126470 |
| medium, sweet, marshmallow, 2 flavours | 2.113779 |
| large, sweet, jube-jube, 4 flavours | 2.057931 |
| small, sweet, gummy, 4 flavours | 2.020669 |
| large, sour, marshmallow, 2 flavours | 2.019164 |
| medium, sweet, marshmallow, 4 flavours | 2.010150 |
| large, sour, marshmallow, 4 flavours | 1.914563 |
| medium, sweet, jube-jube, 1 flavours | 1.908660 |
| large, sour, jube-jube, 1 flavours | 1.814113 |
| small, sour, gummy, 1 flavours | 1.776991 |
| medium, sour, marshmallow, 1 flavours | 1.765259 |
| medium, sour, gummy, 2 flavours | 1.736337 |
| small, sweet, marshmallow, 2 flavours | 1.716256 |
| medium, sour, gummy, 4 flavours | 1.632815 |
| small, sweet, marshmallow, 4 flavours | 1.609503 |
| small, sweet, jube-jube, 1 flavours | 1.509380 |
| medium, sweet, jube-jube, 2 flavours | 1.470150 |
| large, sour, jube-jube, 2 flavours | 1.374475 |
| small, sour, marshmallow, 1 flavours | 1.366918 |
| medium, sweet, jube-jube, 4 flavours | 1.365628 |
| small, sour, gummy, 2 flavours | 1.337555 |
| medium, sour, marshmallow, 2 flavours | 1.325958 |
| large, sour, jube-jube, 4 flavours | 1.269764 |
| small, sour, gummy, 4 flavours | 1.232854 |
| medium, sour, marshmallow, 4 flavours | 1.223587 |
| medium, sour, jube-jube, 1 flavours | 1.121208 |
| small, sweet, jube-jube, 2 flavours | 1.071811 |
| small, sweet, jube-jube, 4 flavours | 0.967327 |
| small, sour, marshmallow, 2 flavours | 0.928986 |
| small, sour, marshmallow, 4 flavours | 0.823402 |
| small, sour, jube-jube, 1 flavours | 0.722607 |
| medium, sour, jube-jube, 2 flavours | 0.682972 |
| medium, sour, jube-jube, 4 flavours | 0.577018 |
| small, sour, jube-jube, 2 flavours | 0.283677 |
| small, sour, jube-jube, 4 flavours | 0.178755 |
| Total | 100.000000 |

