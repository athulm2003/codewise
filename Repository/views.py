from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionDb
from Repository.serializers import QuestionSerializer

# Create your views here.

class QuestionCreateView(APIView):
    def get(self,request):
        qs=QuestionDb.objects.all().values()    #Query the QuestionDb model to retrieve all the questions.

        serializer_instance=QuestionSerializer(qs,many=True) #Serialize the queryset using the QuestionSerializer

        return Response(data=serializer_instance.data) #Return the serialized data as a response

    #post method for adding questions
    
    def post(self,request):

        form_data=request.data      #Get the data from the request body, python native type

        serializer_instance= QuestionSerializer(data=form_data)

        if  serializer_instance.is_valid():

            actual_data=serializer_instance.validated_data



            #create a new QuestionDb instance with the form data
            QuestionDb.objects.create(**actual_data)

            return Response(data={"Message" : "Question added Successfully"})
        
        else:
            return Response(data={"errors" : serializer_instance.errors })

class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):

        qs=QuestionDb.objects.get(id=pk)
        serializer_instance=QuestionSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data =request.data
        serializer_instance=QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)            
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        QuestionDb.objects.filter(id=pk).delete()

        return Response(
            {
                "Message" : "Question Deleted Successfully...!"
            }
        )