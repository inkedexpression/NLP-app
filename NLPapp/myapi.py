from http.client import responses

import nlpcloud
class API:

    def __init__(self):
        self.client = nlpcloud.Client("finetuned-llama-3-70b", '49544baf18b79c1b14346886918d23d4d34a67f8', gpu=True)

    def sentiment_analysis(self,text):
       response =  self.client.sentiment(
            text,
            target="NLP Cloud"
        )
       return response


    def ner(self,text):
        response = self.client.entities(
            text,
            searched_entity="programming languages"
        )
        return response

    def emotion(self,text):
        response = self.client.lang_detection(
            text
        )
        return response