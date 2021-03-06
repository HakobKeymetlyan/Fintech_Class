# Correlating Returns

In this activity, you will create a sentiment index from News API headlines and correlate it to Apple (`AAPL`) daily returns, looking for text topics that generate the highest correlation.

## Instructions

1. Download returns data for the past month for `AAPL` using the Alpaca API.

2. Get news headlines for three topics of your choice and apply sentiment analysis to the headlines.

3. Correlate the headlines sentiment to S&P 500 returns for each topic. Which one had the highest correlation?

## Hints

* In order to correlate sentiment and returns, we need to make sure that they're grouped in the same unit—in this case, trading days.

* The function that you need to download news headlines is already defined. You'll need to modify it to get headlines for the days you want to include.

## Troubleshooting Notes

The VADER sentiment library may need to have the input text converted to plain ASCII text. The following code can be used to convert a string or byte to plain ASCII text.

```python
plain_ascii = raw_text.encode('utf-8', 'ignore').decode('ascii', 'ignore')
```

If the `headline_sentiment_summarizer_avg` function does not work, try using the following version of the function instead:

```python
def headline_sentiment_summarizer_avg(headlines):
    sentiment = []
    for day in headlines:
        day_score = []
        for h in day:
            h = h.encode('utf-8', 'ignore').decode('ascii', 'ignore')
            if h == None:
                continue
            else:
                day_score.append(sid.polarity_scores(h)["compound"])
        sentiment.append(sum(day_score) / len(day_score))
    return sentiment
```

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
