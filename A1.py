# # import grammar_check
# import fuzzywuzzy as fuzz
#
# # # tool = grammar_check.LanguageTool('en-GB')
# # text = 'This are bad.'
# # matches = tool.check(text)
# # len(matches)
# # grammar_check.correct(text, matches)
#
#
# fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
import language_check

tool = language_check.LanguageTool('en-US')
text = u'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
matches = tool.check(text)
print(language_check.correct(text, matches))
