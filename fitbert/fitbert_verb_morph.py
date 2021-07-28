from fitbert import FitBert


fb = FitBert()

masked_string = "I thought I heard about it ***mask*** week!"
options = open("words-10k.txt", "r").readlines()
# options = ["looks"]
ranks = fb.rank_with_prob(masked_string, options)[0][0:5]
print(ranks)
# filled_in = fb.fitb(masked_string, options=options, delemmatize=True)

# print(filled_in)
