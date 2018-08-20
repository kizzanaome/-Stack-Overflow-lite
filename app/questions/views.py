from flask import Flask, jsonify, make_response, Blueprint
from flask_restful import Api, abort, reqparse, Resource
from .models import question_db, Question, Replytoquestion,answers

class View_questions(Resource):
    def get(self):
        """Method for getting questions"""
        if not question_db:
            return make_response(jsonify({"message":"No questions posted yet"}),200)
        return make_response(jsonify({"questions": question_db}),200)

    def post(self):
        """Method for posting a question"""
        parser =reqparse.RequestParser()
        parser.add_argument("title")
        parser.add_argument("description")
        args = parser.parse_args()

        if len(question_db) == 0:
            user_id = len(question_db)+1
        else:
            user_id = len(question_db)+1


        question = Question(user_id, args['title'], args['description'])
        question.create_question()

        return make_response(jsonify({"massage":"Question has been created"}),201)

class Singlequestion(Resource):
    def get(self, qstn_id):
        a_qustn = None
        for question in question_db:
            if (question["qstn_id"] == qstn_id):
                a_qustn = question
                return make_response(jsonify({"question":a_qustn}), 200)
        return make_response(jsonify({"message":"Question not found"}),404)

class Answerquestion(Resource):
    def post(self, qstn_id):
        parser = reqparse.RequestParser()
        parser.add_argument("reply")
        args = parser.parse_args()

        # class insatnce
        answer = Replytoquestion(qstn_id,args["reply"])
        answer.create_answer()
        for answer in answers:
            if (qstn_id == answer["qstn_id"]):
                return "Your answer to question with qstn_id {} has been sent succesfully ". format(qstn_id), 201
        return make_response(jsonify(
            {"message": "question was not found"
            }), 404)









