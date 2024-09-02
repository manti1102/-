from urllib import request

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from blog.models import Publication, Category, PublicationComment, ContactClient


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.filter(is_active=True)

        }
        return context

class HomesearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        search_word = self.request.GET['search']
        context = {
            'publication_list': Publication.objects.filter(
                is_active=True).filter(Q(title__icontains=search_word) | Q(short_description__icontains=search_word))
        }
        return context

class ContactUs(TemplateView):
    template_name ='contact.html'

def contact_client_view(request, **kwargs):
    print( request.POST)

    input_name = request.POST['name']
    input_email = request.POST['email']
    subject = request.POST['subject']
    input_message = request.POST['message']

    ContactClient.objects.create(name=input_name, email=input_email, telephone=subject, message=input_message)

    return HttpResponse()



class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication': Publication.objects.get(id=publication_pk),
            'category_list': Category.objects.all()
                    }
        return context


class CreatePublicationCommentView(View):
    def post(self,request,*args,**kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.get(id=publication_pk)
        comment_text = request.POST['message']
        PublicationComment.objects.create(publication=publication, text=comment_text)
        return redirect('publication-detail', pk=publication_pk)



