## BioCreative Task III Lexicon Approach

**This project represents the first approach to creating an accurate tweet parser that pings
tweets with mentions of pharmaceutical drugs. Below is the directory map:**
***

* config - used for debugging the implementation and evaluation process, using dummy lexicon. Can be modified
<p>&nbsp;</p>

* eval - provided by BioCreative. Evaluates the prediction results compared to gold standard.
<p>&nbsp;</p>

* evalFix - EvalFix.py imports the functions from eval and calls them manually, to avoid the
command line issue with the original script. Resuls are written to score_log.txt
<p>&nbsp;</p>

* gold_std - provided gold standard files with the correctly pinged tweets from the given datasets.

<p>&nbsp;</p>

* includes
  * Tweet.py - class containing an individual tweet, which "pops" if parser determines that it contains drug
mentions.
  * Dataset.py - class containing a list of tweet objects, the lexicon being compared with,
and relevant functions including check() which performs the lexicon parse.
  * implementation.py - **poorly named, should be changed.** This function accepts
a series of strings that indicate which dataset is being parsed, which dictionary is being used, and
other params such as stop words or subwords.  
<p>&nbsp;</p>
  
* lexicons - CSVs containing the 3 used lexicons:
  * Training_only: list of drugs pulled from the positive results of the given datasets
  * RXNORM_only: list of drugs pulled from the RXNORM national library of medicine
  * Training_and_RXNORM: the above two combined
<p>&nbsp;</p>
  
* misc_scripts - unused scripts
<p>&nbsp;</p>

* predictions - contains all permutations of prediction files in current iteration, across 3 lexicons,
4 parameter combinations, and 2 datasets.
<p>&nbsp;</p>
~~~~~~~~
