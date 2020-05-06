import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np

# https://www.datacamp.com/community/tutorials/wordcloud-python

# Start with one review:
text = "Hobbits are an unobtrusive but very ancient people, more numerous formerly than they are today; for they love peace and quiet and good tilled earth: a well-ordered and well-farmed countryside was their favourite haunt. They do not and did not understand or like machines more complicated than a forge-bellows, a water-mill, or a hand-loom, though they were skilful with tools. Even in ancient days they were, as a rule, shy of 'the Big Folk', as they call us, and now they avoid us with dismay and are becoming hard to find. They are quick of hearing and sharp-eyed, and though they are inclined to be fat and do not hurry unnecessarily, they are nonetheless nimble and deft in their movements. They possessed from the first the art of disappearing swiftly and silently, when large folk whom they do not wish to meet come blundering by; and this an they have developed until to Men it may seem magical. But Hobbits have never, in fact, studied magic of any kind, and their elusiveness is due solely to a professional skill that heredity and practice, and a close friendship with the earth, have rendered inimitable by bigger and clumsier races."

# Create and generate a word cloud image:

stopwords = list(STOPWORDS)
extra_stopwords = ["https", "co", "ly", "&amp;"]
for s in extra_stopwords:
    stopwords.append(s)

stopwords = set(stopwords)


def make_wordcloud(text, path, show=False):

    wordcloud = WordCloud(
        width=600,
        height=600,
        stopwords=stopwords,
        max_font_size=50,
        max_words=100,
        background_color="white").generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    if show == True:
        plt.show()
    wordcloud.to_file(path)

# make_wordcloud(text, "test.png", show=True)