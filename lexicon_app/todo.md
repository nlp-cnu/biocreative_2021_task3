## GOAL:To evaluate the lexicon approach with all generated lexicons, all combinations parameters, using
##both the Training task and Validation task datasets.

Evaluation: Evaluation will score by 3 metrics
 - F1:
 - Precision:
 - Recall:


Parameters: Predictions will be collected WITH and WITHOUT both parameters

- Stopwords: The words "pill", "shot" and "shots" appear frequently in drug lexicons, but
not all tweets containing these words are drug related, so Stopwords will modify the lexicon to
include these words.

- Subwords: Searching for strings within words, eg. "pill" in "pillow", can create false positives
in predictions, so Subwords will modify the predictions to pop on these sub-string positives.


##Last known errors:
"The number of tweets loaded in the gold standard 88987 is not the
same than the number of tweets loaded in the predictions 88988" -eval script error

Either bug in eval script that is misreading certain prediction files, or lexicon_app
is creating the wrong number of tweets.

evalFix: run score_task in separate by feeding it gold_std and pred files manually, figure
out why its getting the wrong number of tweets
