import tweepy, csv
from nltk import word_tokenize, pos_tag
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
bearer_token = "YOUR_BEARER_TOKEN" #For Example "AAAAAAAAAAAAAAAAAAAAAIA%2FkgEAAAA..."
client = tweepy.Client(bearer_token=bearer_token)

#User ID for the user 'ΧΧΧΧ' and the name of the CSV file that we want to create.
user_id='ΧΧΧΧΧΧ'#UserID. codeofaninja.com/tools/find-twitter-id/
file_name='FILE_NAME.csv'
#With this function we will take the tweets from the user without replies and retweets.
#Αnd create two columns that contain the id and the text of each tweet.  
def take_tweets():
    
    tweet_fields_to_get=['id','text']

    paginator = tweepy.Paginator(client.get_users_tweets,user_id, 
                                       tweet_fields=tweet_fields_to_get,
                                       exclude=['replies','retweets'],
                                       max_results=100)
    
#We will save the tweets in a CSV file. The max tweets we can take every time is 100
#So we will use paginator to retreive 500 tweets                    
    fw=open(file_name,'w', encoding='utf-8')
    my_writer=csv.writer(fw,lineterminator='\n') 
    my_writer.writerow(tweet_fields_to_get) 
    for tweet in paginator.flatten(limit=500):  
        new_row=[] 
        for field in tweet_fields_to_get:
            new_row.append(tweet[field]) 
    
        my_writer.writerow(new_row) 
        
    fw.close()

take_tweets()
#Since many of the tweets include links/URLs, we need to remove them for better results.
with open(file_name, 'r', encoding='utf-8') as f:
  rows = list(csv.reader(f))
for row in rows:
  for i, cell in enumerate(row):
      row[i] = re.sub(r'http\S+', '', cell)
         
#And then we will save the CSV file again.
with open(file_name, 'w', encoding='utf-8') as f:
  writer = csv.writer(f, lineterminator='\n')
  writer.writerows(rows)

#We will read the CSV file but only 'text' column.
with open(file_name, "r", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    text_tweets=[]
    for row in reader:
        text = row['text']
        text_tweets.append(text)
#We will create the three empty lists that we need (Nouns, Verbs, Adjectives).     
sentences = text_tweets 
nouns = []
verbs = []
adjectives = []
for sentence in sentences:
    sentence=sentence.lower() #We have to make all words lowercase to avoid double words.
    words=word_tokenize(sentence) #Then split all the words for all the tweets.
    tagged_words=pos_tag(words) #Finaly we need to find out what Part-Of-Speech it is.
    
    #Every word will be added in one of the three lists that we create before.    
    for tagged_word in tagged_words:
        word=tagged_word[0]  
        tag=tagged_word[1] 
                
        if tag.startswith('NN'): #To find all Nouns
            nouns.append(word) #And add them in first list
            
        elif tag.startswith('VB'): #To find all Verbs
            verbs.append(word) #And add them in second list
                
        elif tag.startswith('JJ'): #To find all Adkectives
            adjectives.append(word) #And add them in third list
#With this function we will add words in a dictionary and create tag cloud. 
def tag_cloud(word_list):
    
    frequencies={}
    for word in word_list:
        frequencies[word]=frequencies.get(word,0)+1

    wordcloud = WordCloud(background_color='white')
    wordcloud.generate_from_frequencies(frequencies=frequencies)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
#Last part is to call the function and display the three tag clouds.
#Each word's size in the tag cloud will depend on the frequency that it appears in these 500 tweets.
tag_cloud(nouns)
tag_cloud(verbs)
tag_cloud(adjectives)