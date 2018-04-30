import grammar_check

tool = grammar_check.LanguageTool('en-GB')
text = 'This are bad.'
matches = tool.check(text)
# len(matches)
print(grammar_check.correct(text, matches))
