# import string
# from nltk.tokenize import sent_tokenize
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# from nltk.tag import pos_tag


# class unstructuredPreprocessing():
#     """ all the steps for preprocessing unstructured data. """
    
#     def text_into_list(self, text : str) -> list:
#         tokenized_list = sent_tokenize(text)
#         return tokenized_list

    
#     def strip_whitespace(self,text : list) -> list:
#         striped_list = [string.strip() for string in text]
#         return striped_list

    
#     def remove_noice(self,text : list) -> list:
#         no_punc = "".join({char for char in text if char not in string.punctuation})
#         return no_punc    

    
#     def capitalizer(text: list) -> list:
#         return text.upper()    

    
#     def tokenization(self, text : list) -> list:
#         tokenized_list = word_tokenize(text)
#         return tokenized_list

    
#     def remove_stopwords(self, text : list) -> list:
#         stopwords = stopwords.words('english')
#         text_without_stopwords = "".join({word for word in text if word not in stopwords})
#         return text_without_stopwords
    
    
#     def lemmatize_sentence(self, text : list) -> list:
#         lemmatizer = WordNetLemmatizer()
#         lemmatized_sentence = []
#         for word, tag in pos_tag(text):
#             if tag.startswith('NN'):
#                 pos = 'n'
#             elif tag.startswith('VB'):
#                 pos = 'v'
#             else:
#                 pos = 'a'
#             lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
#         return lemmatized_sentence 


# import nltk
# from nltk.tokenize import sent_tokenize
# nltk.download('punkt')
# nltk.download('stopwords')

# from nltk.tokenize import sent_tokenize
# tokenized_text=sent_tokenize(text)
# print(tokenized_text)

# from nltk.tokenize import word_tokenize
# tokenized_word=word_tokenize(text)
# print(tokenized_word)

# Lowercase = []
# for lowercase in tokenized_word:
#     Lowercase.append(lowercase.lower())
# print(Lowercase)

# from nltk.probability import FreqDist
# fdist = FreqDist(tokenized_word)
# print(fdist)

# from nltk.corpus import stopwords
# stop_words=set(stopwords.words("english"))
# print(stop_words)

# filtered_sent=[]
# for w in tokenized_word:
#     if w not in stop_words:
#         filtered_sent.append(w)
# print("Tokenized Sentence:",tokenized_word)
# print("Filterd Sentence:",filtered_sent)

# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize

# ps = PorterStemmer()

# stemmed_words=[]
# for w in filtered_sent:
#     stemmed_words.append(ps.stem(w))

# print("Filtered Sentence:",filtered_sent)
# print("Stemmed Sentence:",stemmed_words)

import spacy
from profanity_filter import ProfanityFilter
#import en_core_web_sm


class detection():
      
      #nlp = spacy.load("en_core_web_lg")
      #nlp = spacy.load('en')
      #nlp = en_core_web_sm.load()

      def profanity(text):
      #text = "scrapped text"
            tokenn=[]
            censored=[]
            profane=[]
            original_profane=[]
            nlp = spacy.load('en')

            profanity_filter = ProfanityFilter(nlps={'en': nlp})
            nlp.add_pipe(profanity_filter.spacy_component, last=True)

            doc = nlp(text)
            doc._.is_profane      
            for token in doc:
                  tokenn.append(token)
                  censored.append(token._.censored)
                  profane.append(token._.is_profane)
                  original_profane.append(token._.original_profane_word)
          
            return (f'{token}: '
                        f'censored={censored}, '
                        "\n"f'is_profane={profane}, '
                        f'original_profane_word={original_profane}'    
                  )        
                  #  return (f'{token}: '
                  #       f'censored={token._.censored}, '
                  #       "\n"f'is_profane={token._.is_profane}, '
                  #       f'original_profane_word={token._.original_profane_word}'    
                  # )        