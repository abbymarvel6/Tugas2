from django.urls import path
from mywatchlist.views import show_film
from mywatchlist.views import show_xml 
from mywatchlist.views import show_json
from mywatchlist.views import show_xml_by_id
from mywatchlist.views import show_json_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_film, name='show_film'),
    path('html/', show_film, name='show_film'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]