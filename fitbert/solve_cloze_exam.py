
from fitbert import FitBert
from tools import split_to_sentences

# currently supported models: bert-large-uncased and distilbert-base-uncased
# this takes a while and loads a whole big BERT into memory
from tools.split_to_sentences import split_into_sentences

mask = '***mask***'
masked_string = '''Mr. Heikke gets up very early ***mask*** day. He washes his face and takes a quick shower ***mask*** the mornings. His best friend, Bobby, also wakes up very early. Mr. Heikke ***mask*** the breakfast for both. They both ***mask*** like drinking milk but they love eating meat. Then, Mr. Heikke ***mask*** bobby out to park. Mr. Heikke ***mask*** a graphic designer'''
sentences = split_into_sentences(masked_string)
print(sentences)

word_file = open("words-1000.txt", "r")
words = word_file.readlines()

resolved = ""

fb = FitBert()

for masked_sentence in sentences:
    masked_text = resolved + masked_sentence
    if mask not in masked_text:
        continue
    print(masked_text)
    filled_in = fb.fitb(masked_text, options=words)
    print(filled_in)
    resolved = filled_in

# or

print(resolved)

