from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def course(request):
    return HttpResponse('''
                        <a  href='/firstapp/contact/'>Contact</a>
                         <a  href='/firstapp/feedback/'>Feedback</a>
                        <h1>This is Course Page</h1>
                        
                        
                        ''')
def about(request):
    return HttpResponse('''
                    
                          <a  href='/firstapp/contact/'>Contact</a>
                         <a  href='/firstapp/feedback/'>Feedback</a>
                        This is About Page''')