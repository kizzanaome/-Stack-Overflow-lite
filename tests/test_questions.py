import unittest
from unittest import TestCase
from app.questions.models import Question, question_db
import json
from app import create_app


class Test_Questions(unittest.TestCase):
    def setUp(self):
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client
   
    def test_add_question(self):
        """Test API can add a question (POST request)"""
        post_qstn1 ={
            'question_id':"2",
            "title":"What is programing",
            "description":"Programing is coding"
        }
        response = self.client().post('api/v1/questions',
                                    content_type = 'application/json',
                                    data = json.dumps(post_qstn1))

        self.assertEqual(response.status_code,201)
        

    
    def test_veiw_all_questions(self):   
        """Test to get or fetch all questions""" 
        post_qstn1={
            'question_id':"2",
            "title":"What is programing",
            "description":"Programing is coding"
        }

        response = self.client().post('api/v1/questions',
                                    content_type ='application/json',
                                    data =json.dumps(post_qstn1))
        self.assertEqual(response.status_code,201)
        response = self.client().get('api/v1/questions')
        self.assertEqual(response.status_code,200)


    def test_get_single_question(self):
        '''Test to fetch single question'''
        post_qstn1={
            
            'quiestion_id':"2",
            "title":"What is programing",
            "description":"Programing is coding"
        }
        
        response = self.client().post("/api/v1/questions",
            content_type='application/json',
            data=json.dumps(post_qstn1))
        self.assertEquals(response.status_code, 201)
            
        response2 = self.client().get("/api/v1/questions/2",
        content_type='application/json',data=json.dumps(post_qstn1))
        self.assertEquals(response2.status_code, 200)

    
    


       