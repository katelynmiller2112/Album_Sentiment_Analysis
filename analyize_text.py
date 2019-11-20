import numpy as np
import pandas as pd
import re
from textblob import TextBlob
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
initial_list = []
# for line in open('C:\\Users\\Miller Katelyn\\Desktop\\sentiment_analysis.txt', 'r'):
#     initial_list.append(line.rstrip())


# # print(initial_list)
# # for line in initial_list:
# #     re.compile()"(|,"


# # words = ' '.join(initial_list)
# # # print(words)
# # blob = TextBlob(words)

# # blob.tags
# # blob.noun_phrases
# # x = []
# # for sentence in blob.sentences: 
# #     x.append(sentence.sentiment.polarity)

# # cheese_list = []
# # for line in open('C:\\Users\\Miller Katelyn\\Desktop\\text_to_analyze.txt', 'r'):
# #     cheese_list.append(line.rstrip())


# # # print(initial_list)
# # # for line in initial_list:
# # #     re.compile()"(|,"


# # words = ' '.join(cheese_list)
# # print(words)
# # blob = TextBlob(words)

# # blob.tags
# # blob.noun_phrases
# # y = []
# # for sentence in blob.sentences: 
# #     y.append(sentence.sentiment.polarity)

# # print('Potion Approching',x,'Ultracheese',y)



# meeting_list = []
# for line in open('C:\\Users\\Miller Katelyn\\Desktop\\meeting_place.txt', 'r'):
#     meeting_list.append(line.rstrip())


# words = ' '.join(meeting_list)
# print(words)
# blob = TextBlob(words)

# blob.tags
# blob.noun_phrases
# x = []
# for sentence in blob.sentences: 
#     x.append(sentence.sentiment.polarity)


# arabella_list = []
# for line in open('C:\\Users\\Miller Katelyn\\Desktop\\arabella.txt', 'r'):
#     arabella_list.append(line.rstrip())

# words = ' '.join(arabella_list)
# print(words)
# blob = TextBlob(words)

# blob.tags
# blob.noun_phrases
# y = []
# for sentence in blob.sentences: 
#     y.append(sentence.sentiment.polarity)

# print('Meeting Place',x,'Arabella',y)

# Take album name
# use to navigate to web page. 
# For each song take a text file and write lyrics to it
#naming convention seems to be first letter captialized and none after and spaces filled in with a '-'


def get_album(artist_name,album_name):
    url = 'https://genius.com/albums/' + artist_name + '/' + album_name
    try:
        with closing(get(url,stream = True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                print('fail')
                return None
    
    except RequestException as e:
        # log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200
           and content_type is not None
           and content_type.find('html') > -1)


name = str(input('What is the artists name?'))
album = str(input('What is the album name?'))
clean_name = re.sub(r' ','-',name)
clean_album = re.sub(r' ','-',album)
album_html = get_album(clean_name, clean_album)

# to get the link to the lyrics, going to use the div class "chart row content and the a ng-href" to get the string for the lyrics link. 


plain_html = BeautifulSoup(album_html, 'html.parser')

song_list = []

for a in plain_html.find_all('a',class_='u-display_block',href = True):
    song_list.append(a['href'])


# print(song_list)
# print(display_block)

# display_block.find_all('a',href = True)

# for i in song_list:
#      try:
#         with closing(get(i,stream = True)) as resp:
#             if is_good_response(resp):
#                 content = resp.content
#             else:
#                 print('fail')
#                 return None

#     open()


try:
    with closing(get(song_list[10],stream = True)) as resp:
        if is_good_response(resp):
            content =  resp.content
        else:
            print('fail')
            # return None
except RequestException as e:
    print('fail')
song_html = BeautifulSoup(content,'html.parser')
# print(song_html)

lyrics = []
x = song_html.find('p').getText()
# print(x)
# for i in song_html.find_all('a', class_='referent',string = True):
#     print(a[string])

for song in song_list:
    try:
        with closing(get(song,stream = True)) as resp:
            if is_good_response(resp):
                content =  resp.content
            else:
                print('fail')
                # return None
    except RequestException as e:
        print('fail')
    song_html = BeautifulSoup(content,'html.parser')
    # file_name = song_html.find('title') + '.txt'
    song = song_html.find('title').getText()
    # song = song.strip()
    # song = song.replace('|','')
    # song = song.replace(' – ',' ')
    # song = song.replace(' Genius' ,'')
    # song = song.replace(' Lyrics' ,'')
    print(song)

# maybe it would be best to get the artist and album name and menually put it in the correct format for latter usedsafd
