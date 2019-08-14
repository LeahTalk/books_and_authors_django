from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.books),
    url(r'^books/create_book$', views.create_book),
    url(r'^books/(?P<book_id>\d+)', views.book_details),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<author_id>\d+)', views.author_details)
]
