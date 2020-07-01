from django.views.generic import ListView

from ..models import Person

class PeopleIndex(ListView):
    model = Person
    # template_name = "exodus/person_list.html"