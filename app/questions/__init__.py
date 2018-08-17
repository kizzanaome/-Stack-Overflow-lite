from flask import Blueprint
from flask_restful import Api
from . import views
from app .questions.views import(View_questions, Singlequestion, Answerquestion)

questions = Blueprint("questions", __name__, url_prefix='/api/v1')
questions_api = Api(questions)

questions_api.add_resource( View_questions, '/questions')
questions_api.add_resource(Singlequestion, '/questions/<int:qstn_id>')
questions_api.add_resource(Answerquestion, '/questions/<int:qstn_id>/answers')


