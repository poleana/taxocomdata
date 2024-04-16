pip install -U autophrasex

CHARACTERS = set('!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c，。？：“”【】「」')

class MyNgramFilter(AbstractNgramFiter):

    def apply(self, ngram, **kwargs):
        if any(x in CHARACTERS for x in ngram):
            return True
        return False

autophrase2 = AutoPhrase(
    reader=DefaultCorpusReader(tokenizer=JiebaTokenizer()),
    selector=DefaultPhraseSelector(),
    extractors=[
        NgramsExtractor(N=4, ngram_filters=[MyNgramFilter()]),
        IDFExtractor(ngram_filters=[MyNgramFilter()]),
        EntropyExtractor(ngram_filters=[MyNgramFilter()]),
    ]
)

from autophrasex import *

autophrase = AutoPhrase(
    reader=DefaultCorpusReader(tokenizer=JiebaTokenizer()),
    selector=DefaultPhraseSelector(),
    extractors=[
        NgramsExtractor(N=4),
        IDFExtractor(),
        EntropyExtractor()
    ]
)

predictions = autophrase.mine(
    corpus_files=['DBLP.5K.txt'],
    quality_phrase_files='wiki_quality.txt',
    callbacks=[
        LoggingCallback(),
        ConstantThresholdScheduler(),
        EarlyStopping(patience=2, min_delta=3)
    ])

for pred in predictions:
    print(pred)