from django.views.generic.list import ListView
from universe.models import Planet, Star

class PlanetListView(ListView):

    template_name = 'planet_list.html'
    model = Planet


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "list_len": len(context["planet_list"])
            })
        return context


class StarListView(ListView):

    template_name = 'star_list.html'
    model = Star


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "list_len": len(context["star_list"])
            })
        return context