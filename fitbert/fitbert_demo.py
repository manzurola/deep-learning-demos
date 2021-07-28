from fitbert import FitBert


# currently supported models: bert-large-uncased and distilbert-base-uncased
# this takes a while and loads a whole big BERT into memory
fb = FitBert()

masked_string = "Why Bert, you're looking ***mask*** today!"
options = ['buff', 'handsome', 'strong']

ranked_options = fb.rank(masked_string, options=options)
print(ranked_options)
# >>> ['handsome', 'strong', 'buff']

# or
filled_in = fb.fitb(masked_string, options=options)
print(filled_in)

# >>> "Why Bert, you're looking handsome today!"
