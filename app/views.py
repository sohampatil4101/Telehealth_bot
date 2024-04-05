from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, HttpResponse
import google.generativeai as genai

# Create your views here.

class Ask(APIView):
    def post(self, request):
        genai.configure(api_key="AIzaSyAje4c-yOKwI8GcBgO0EdrnCx-uum0hW20")

        data = request.data
        print("This is the data", data['query'])
        
        # print(json_data1, "soham is great", json_data2)
        # user_input = f""
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(data['query'])
        print("\nResponse from Assistance Bot:")
        print(response.text)
        return HttpResponse(response.text)