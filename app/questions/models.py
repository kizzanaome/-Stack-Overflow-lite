from flask_restful import Api, abort,Resource
from flask import Flask

"""we first create an empty question list"""

question_db = []
answers =[]

class Question():
    def __init__(self, qstn_id, title, description ):
        self.qstn_id = qstn_id
        self.title =title
        self.description =description

    def create_question(self):

        question = {
            "qstn_id" : self.qstn_id,
            "title" :self.title,
            "description" : self.description
        }

        question_db.append(question)

        return question

                
class Replytoquestion():
    def __init__(self, qstn_id, reply):
        self.qstn_id = qstn_id
        self.reply = reply
    
    def create_answer(self):
        answer = {
            "qstn_id": self.qstn_id,
            "reply": self.reply
        }

        answers.append(answer)
        return answer








