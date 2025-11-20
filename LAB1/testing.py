from tokenizer import word_tokenizer

text="भारत, संस्कृत| यह एक अद्भुत देश है।  http://www.gggg.com"
sentences = word_tokenizer(text)
print(sentences)