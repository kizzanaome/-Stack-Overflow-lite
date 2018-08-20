import unittest
from unittest import TestCase
from app.questions.models import Question, question_db
import json
from app import create_app


class Test_Answers(unittest.TestCase):
    def setUp(self):
        
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client

    def test_add_answer(self):
        """ Test for posting an answer """

        mock_data ={

            "qstn_id":"1",
            "reply":"What is programing"
           
        }

        post_qstn={
             'question_id':"1",
            "title":"What is programing",
            "description":"Programing is coding"

        }
        response = self.client().post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(post_qstn))

        self.client().post("/api/v1/questions/1/answer",
            content_type='application/json',
            data=json.dumps(mock_data))
        self.assertEquals(response.status_code, 201)