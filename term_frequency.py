sentences = nltk.sent_tokenize(text)
sentence_scores = {}
for x in sentences:
    if len(x.split(' ')) < 30:
        for word in nltk.word_tokenize(x.lower()):
            if word in frequency.keys():
                if x not in sentence_scores.keys():
                    sentence_scores[x] = frequency[word]
                else:
                    sentence_scores[x] += frequency[word]

summary_sentences = heapq.nlargest(27, sentence_scores, key=sentence_scores.get)

questions = '\n\n'.join(summary_sentences[:12])

summary = '\n\n'.join(summary_sentences[12:])

viz_words = [x for x in words if x not in nltk.corpus.stopwords.words('english')]
viz_words = [x for x in viz_words if x not in ['thing', 'min', 'really', 'wanted', 'way', 'want', 'going']]
viz_frequency = nltk.FreqDist(viz_words)
cloud = heapq.nlargest(40, viz_frequency, key=viz_frequency.get)

def plot_cloud(wordcloud):
    plt.figure(figsize=(20, 15))
    plt.imshow(wordcloud) 
    plt.axis("off")
    plt.savefig('wordcloud.png');

wordcloud = WordCloud(width=3000, height=2000, random_state=1, 
                      background_color='#f7f0ee', colormap='binary_r', 
                      collocations=False, stopwords=STOPWORDS).generate(' '.join(cloud))

plot_cloud(wordcloud)