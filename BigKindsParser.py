
import pandas as pd

def press_counter(text_df):
    freq = text_df['언론사'].value_counts() #언론사 별 보도 빈도 카운트
    brod_df = pd.DataFrame(freq).reset_index() # 데이터 프레임 제작  + 인덱스 초기화
    brod_df.rename(columns = {'index':'언론사', '언론사':'기사'}, inplace = True) #칼럼 이름 설정
    return brod_df

def keywords_list(series):
    return series.values.tolist()

def keyword_parser(text_list):
    news_key = []
    for word in text_list:
        word = word.split(',') #',' 기점으로 스트링 분리
        news_key.append(word) #분리된 단어들을 리스트에 새로 정렬
    return news_key

def duplication_remover(news_key):
    news_value = []
    for j in news_key:
      j = list(set(j)) #중복 제거
      news_value.append(j) #제거된 리스트를 새로운 리스트에 삽입
    return news_value

def word_counter(news_value):
    key_words = {}
    for k in range(len(news_value)):
          for i in news_value[k]:
              if i not in key_words:
                  key_words[i] = 1 #최초 언어
              elif i in key_words:
                  key_words[i] += 1 #중복 언어
    return key_words

def counter_to_DataFrame(key_words):
    word_df = pd.DataFrame(key_words.items())
    word_df.columns = ['단어', '빈도']
    word_df = word_df.sort_values(['빈도'],ascending = False).reset_index(drop = True) #내림차순 정렬
    return word_df


def press_keywords_analysis(df, press_name): #pipeline
    press_df = df[df['언론사'] == press_name]
    press_df = press_df['키워드']
    press_key = keywords_list(press_df)
    press_words = keyword_parser(press_key)
    press_words = duplication_remover(press_words)
    press = word_counter(press_words)
    press = counter_to_DataFrame(press)
    return press
    
