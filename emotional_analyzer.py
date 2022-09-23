# import nltk
# nltk.download('vader_lexicon')
# nltk.download('stopwords')
# nltk.download('punkt')
'''
🌞 good mood, ☁️ average,  🌧️ bad mood ,  ⛈️ terrible
'''

class emotion_analyser():

    def built_sentence_set(self) -> list: 
        sentence_list = ['Terrible day',\
                'Oh, that is a cat',\
                'When I woke up, I was late for work, I feel guilty all day.',\
                'Met you is the best thing that i\'ve ever had.',\
                'I don\'t like it.',\
                'I am so happy today.',\
                'I am happy now, but this morning I was sad.',\
                'this morning I was sad, but I am happy now.',\
                'this morning I was happy, but I am sad now.',\
                'I was mad with you, forget it, i\'m alright now.',\
                'I was mad with you, now i\'m eating my dinner and enjoying it.',\
                'let\'s go.']
    
        return sentence_list
    
    def split_sentence(self,each_sentence:str) -> str:
        block = each_sentence.split(',')
        which_block = 'whole'
        for id,one in enumerate(block):
            if 'now' in one and 'but' in one:
                which_block = id
                break
            elif 'now' in one and 'but' not in one:
                which_block = id
                break
            elif 'now' not in one and 'but' in one:
                which_block = id
                break
        
        if which_block == 'whole':
            return each_sentence
        else:
            return block[which_block]
    
    
    def delete_stop_word(self,each_sentence:str) -> str:
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize
        stop_words = set(stopwords.words('english')) 
        word_tokens = word_tokenize(each_sentence)
        filtered_sentence_list = [w for w in word_tokens if not w in stop_words] 
        filtered_sentence = ' '.join(filtered_sentence_list)
    
        return filtered_sentence
    
    
    
    def nltk_emotional_analyzer(self,each_sentence:str) -> dict:
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        sid = SentimentIntensityAnalyzer()
        sentence_score = sid.polarity_scores(each_sentence)
        # for words_score in sentence_score:
        #     print(f'{words_score}:{sentence_score[words_score]}')
        
        return sentence_score
    

ema = emotion_analyser()
sentence_list = ema.built_sentence_set()
for each_se in sentence_list:
    filted_se = ema.delete_stop_word(ema.split_sentence(each_se))
    emotion_score = ema.nltk_emotional_analyzer(filted_se)
    
    if emotion_score['compound'] >= 0.1:
        print(f'{each_se} →  🌞')
    elif 0 <= emotion_score['compound'] < 0.1:
        print(f'{each_se} →  ☁️')
    elif 0 > emotion_score['compound'] >-0.1:
        print(f'{each_se} →  🌧️')
    else:
        print(f'{each_se} →  ⛈️')