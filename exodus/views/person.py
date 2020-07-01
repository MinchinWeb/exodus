from django.views.generic import ListView, DetailView

from ..models import Person

class PersonIndex(ListView):
    model = Person
    context_object_name = "people"
    # template_name = "exodus/person_list.html"

class PersonDetails(DetailView):
    model = Person
    context_object_name = "person"
