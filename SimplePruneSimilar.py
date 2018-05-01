import difflib

fn1 = 'protein tyrosine phosphatase activity'
fn2 = 'protein-tyrosine phosphatase'
score = difflib.SequenceMatcher(None, fn1.lower(), fn2.lower()).ratio()
print(score)
