#                   +-----------------+
#                   |  User Interface |
#                   +--------+--------+
#                            |
 #                  +--------v--------+
 #                  |  NLP Processor  |
#                   +--------+--------+
 #                           |
 #                  +--------v--------+
  #                 |  Intent Engine  |
  #                 +--------+--------+
   #                         |
#+------------------+--------v--------+------------------+
#|   Knowledge Base |  Dialog Manager |  External APIs   |
#+------------------+-----------------+------------------+
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class AdvancedNGOChatbot:
    def __init__(self, data_path):
        self.nlp = spacy.load("en_core_web_md")
        self.df = self.preprocess_data(pd.read_excel(data_path))
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['processed_services'])
    
    def preprocess_data(self, df):
        df['processed_services'] = df['Services'].apply(self.normalize_text)
        return df
    
    def normalize_text(self, text):
        doc = self.nlp(text.lower())
        return ' '.join([token.lemma_ for token in doc if not token.is_stop])
    
    def handle_query(self, user_input):
        intent = self.classify_intent(user_input)
        
        if intent == 'find_ngo':
            return self.find_ngo(user_input)
        elif intent == 'contact_info':
            return self.get_contact(user_input)
        else:
            return self.default_response()
    
    def classify_intent(self, text):
        doc = self.nlp(text.lower())
        if any(token.text in ['contact', 'phone', 'email'] for token in doc):
            return 'contact_info'
        return 'find_ngo'

    def find_ngo(self, query):
        processed_query = self.normalize_text(query)
        query_vec = self.vectorizer.transform([processed_query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)
        top_3 = similarities.argsort()[0][-3:][::-1]
        return self.df.iloc[top_3]

    def get_contact(self, query):
        # Implement NER for organization name extraction
        pass

# Usage with error handling
try:
    bot = AdvancedNGOChatbot("ngo_data.xlsx")
    results = bot.handle_query("Find NGOs working in education near Mumbai")
except Exception as e:
    print(f"Chatbot error: {str(e)}")
  #-----------------------Chatbot Tests-----------------
 # def test_chatbot():
  #  test_cases = [
   #     ("Education NGOs", 3),
  #      ("Contact for ABC NGO", 1),
   #     ("Invalid query", "default")
   # ]
    #for query, expected in test_cases:
       # result = bot.handle_query(query)
      #  assert len(result) == expected if isinstance(expected, int) else True
#--------------------------------	Chatbot Development---------------
#•	Phase 1: Basic Recommendation (3 days)
#•	Phase 2: NLP Integration (2 days)
#•	Phase 3: Deployment (1 day)


#------------------ Enhanced Features------------------
#1.	Add NLP processing with NLTK/spaCy
#2.	Implement conversation flow
#3.	Add email integration
#4.	Create API endpoint using Flask

#------------------Implementation Strategy-------------------------
#1.	Scraper Development
#•	Identify target websites (NGO Darpan from6)
#•	Analyze website structure using browser DevTools
#•	Implement pagination handling
#•	Add error logging
#2.	Data Validation
#•	Clean data using pandas
#•	Handle missing values
#•	Standardize phone formats
#3.	Chatbot Training
#•	Create intent classification model
#•	Implement response generation
#•	Add context management
#4.	Deployment
#•	Containerize using Docker
#•	Schedule scraping tasks
#•	Deploy chatbot as web service


