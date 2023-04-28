from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from polls.models import Question
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status

# 깃헙 테스트를 위해 코드변경을 해봤습니다.
# 한번 더 코드변경을 해봤습니다.
# 한번 정리합니다
@api_view(['GET', 'POST'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def question_detail(request, id):
    question = Question.objects.get(pk=id)
    serializer = QuestionSerializer(question)
    return Response(serializer.data)