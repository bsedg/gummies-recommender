gummies-recommender/data
===================

### Data
The original data file is located here in **scores.json**.  The data model has only 5 fields:

```javascript
{
    'score': Number,
    'size': String, // small, medium, large
    'flavour': String, // sweet, sour
    'composition': String, // marshmallow, gummy, jube-jube
    'colour-count': Number // 1, 2, 4
}
```

There are 1,000,000 data objects with the above data model in the given data set.  Below is the head and tail of the file, **scores.json**.  All data objects in the data set have all the attributes defined, so there is no need to fill in default data for fields.


```javascript
{'score':0.578125, 'size':medium, 'flavour':sweet, 'composition':marshmallow, 'colour-count':4}
{'score':0.609821, 'size':large, 'flavour':sweet, 'composition':marshmallow, 'colour-count':2}
{'score':0.523088, 'size':small, 'flavour':sweet, 'composition':jube-jube, 'colour-count':2}
...
{'score':0.648594, 'size':large, 'flavour':sweet, 'composition':gummy, 'colour-count':2}
{'score':0.536298, 'size':large, 'flavour':sour, 'composition':jube-jube, 'colour-count':2}
{'score':0.55518, 'size':medium, 'flavour':sour, 'composition':marshmallow, 'colour-count':1}
```

### Data Normalizaton Script
Since the data file contains parts that are not normalized json (quoted strings), there is a simple shell script that uses *sed* to replace the un-quoted strings to quoted strings in **normalize_data.sh**.

#### Normalized Data
Below is the head and tail of the produced file from the normalization script, **normalize_data.sh**.

```javascript
{"score":0.578125, "size":"medium", "flavour":"sweet", "composition":"marshmallow", "colour-count":4}
{"score":0.609821, "size":"large", "flavour":"sweet", "composition":"marshmallow", "colour-count":2}
{"score":0.523088, "size":"small", "flavour":"sweet", "composition":"jube-jube", "colour-count":2}
...
{"score":0.648594, "size":"large", "flavour":"sweet", "composition":"gummy", "colour-count":2}
{"score":0.536298, "size":"large", "flavour":"sour", "composition":"jube-jube", "colour-count":2}
{"score":0.55518, "size":"medium", "flavour":"sour", "composition":"marshmallow", "colour-count":1}
```
