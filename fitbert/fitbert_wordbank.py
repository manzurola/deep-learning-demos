from fitbert import FitBert

def replace_mask(s):
    mask = '***mask***'
    placeholder = '___'
    return s.replace(placeholder, mask)


sentence_file = open("examples/cloze_esl_lounge.txt", "r")
sentences = map(replace_mask, sentence_file.readlines())
print(sentences)

word_file = open("words-10k.txt", "r")
words = word_file.readlines()

fb = FitBert()

for masked_sentence in sentences:
    filled_in = fb.fitb(masked_sentence, options=words)
    print(filled_in)
