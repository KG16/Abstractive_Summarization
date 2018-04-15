# import grammar_check
import fuzzywuzzy as fuzz

# # tool = grammar_check.LanguageTool('en-GB')
# text = 'This are bad.'
# matches = tool.check(text)
# len(matches)
# grammar_check.correct(text, matches)


fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
