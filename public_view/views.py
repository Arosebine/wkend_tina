from django.shortcuts import render
from django.http import HttpResponse 
from public_view.models import *
from django.contrib import messages

from django.core import mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def home(request):
     rent = Property.objects.filter(offer_type='Rent').order_by('-created')[:3]
     sale = Property.objects.filter(offer_type='Sale').order_by('-created')[:3]
     args = {
          'rent':rent,
          'sale':sale
     }
     return render(request, 'public/index.html', args)


def about(request):
     display_team = Team.objects.all()
     return render(request, 'public/about.html', {'team':display_team})

def team_detail(request, team_id):
     detail = Team.objects.get(id=team_id)
     return render(request, 'public/team-detail.html', {'det':detail})



def agent(request):
     return render(request, 'public/agent.html')




def rent(request):
     return render(request, 'public/rent.html')



def request(request):
     return render(request, 'public/request.html')



def property_details(request, slug):
     detail_property = Property.objects.get(slug=slug)
     get_location = detail_property.location_id
     related_prop = Property.objects.filter(location_id=get_location)

     if request.method == 'POST':
          name = request.POST.get('name')
          phone = request.POST.get('phone')
          email = request.POST.get('email')
          detail_property = Property.objects.get(slug=slug)
          get_location = detail_property.location_id
          get_agent = detail_property.agent_id
          get_agent_email = detail_property.agent_id.email

          subject = 'From Real Estate Site'
          args = {
               'name':name,
               'phone':phone,
               'email':email,
               'location':get_location,
               'agent':get_agent
          }
          html_message = render_to_string('public/mail-template.html', args)
          plain_message = strip_tags(html_message)
          from_email = settings.FROM_EMAIL
          send = mail.send_mail(subject, plain_message, from_email, [get_agent_email, ], html_message=html_message)
          if send:
               ContactAgent.objects.create(name=name, phone=phone, email=email, 
                    agent_id=get_agent, location_id=get_location)
               messages.success(request, 'Data sent to the agent')
     return render(request, 'public/property-details.html', 
          {'det':detail_property, 'rel':related_prop})





def buy(request):
     return render(request, 'public/buy.html')




def register(request):
     return render(request, 'public/register.html')




def login(request):
     return render(request, 'public/login.html')




# def add(request):
#      return HttpResponse( 6+3 )



