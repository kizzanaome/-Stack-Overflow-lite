import unittest
from unittest import TestCase
from app.questions.models import Question, question_db
import json
from app import create_app


class RequestTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client

    def test_question_creation(self):
        mock_data ={
            'quiestion_id':"2",
            "title":"What is programing",
            "description":"Programing is coding"
        }
        response = self.client().post('api/v1/questions',
                                    content_type = 'application/json',
                                    data = json.dumps(mock_data))

        self.assertEqual(response.status_code,201)

    def test_view_all(self):
        response = self.client().get('api/v1/questions',
                                    content_type = 'application/json')

        self.assertEqual(response.status_code,200)



    def test_single_question(self):

        mock_data ={

            'quiestion_id':"2",
            "title":"What is programing",
            "description":"Programing is coding"
        }
        """
           The test tests the get method that gets a single question
          
       """
        response = self.client().get("/api/v1/questions/1",
                                content_type="application/json",
                                data=json.dumps(mock_data))          
        self.assertEqual(response.status_code, 200)


    def test_answer_post(self):

        mock_data ={

            "qstn_id":"1",
            "reply":"What is programing"
           
        }
        """
           The test tests the post method that posts an answer
        """
        response = self.client().post("/api/v1/questions/1/answers",
                                content_type="application/json",
                                data=json.dumps(mock_data))
        self.assertEqual(response.status_code, 201)
        

