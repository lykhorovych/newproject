from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from cities.models import City
from .forms import CityForm, CityForm2
from django.contrib import messages

# Create your views here.
__all__ = (
    'index',
    'CityListView',
    'all_cities',
    'single_city',
    'CityView',
    'CreateCity',
    'CityDeleteView',
)


def index(request):
    return render(request, template_name='base.html')


def all_cities(request):
    cities = get_list_or_404(City)
    form = CityForm2()
    paginator = Paginator(cities, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template_name='cities/cities.html', context={'cities': cities,
                                                                        'form': form,
                                                                        'page_obj': page_obj,
                                                                        'page_number': page_number})


def single_city(request, pk=None):
    city = get_object_or_404(City, pk=pk)
    return render(request, template_name='cities/city.html', context={'city': city,
                                                                      'form': CityForm()})


class CityView(View):

    def get(self, request, pk=None):
        city = get_object_or_404(City, pk=pk)
        return render(request, template_name='cities/city.html', context={'city': city,
                                                                          'form': CityForm2(),
                                                                          })

    def post(self, request, pk=None):
        city = CityForm2(request.POST)
        if city.is_valid():
            City.objects.create(**city.cleaned_data)
            reverse('all_cities')
        return HttpResponse(city.errors)


class CreateCity(SuccessMessageMixin, generic.CreateView):
    model = City
    form_class = CityForm2
    success_url = reverse_lazy('all_cities')
    template_name = 'cities/form.html'
    success_message = "%(name)s was created successfully"


def view_city(request, pk=None):
    city = get_object_or_404(City, pk=pk)

    if request.method == 'GET':
        form = CityForm(initial={'name': city.name})
        return render(request, template_name="", context={'form': form})

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city.name = form.cleaned_data['name']
            city.save()
            return reverse('city', args=(pk,))


class CityUpdateView(SuccessMessageMixin, generic.UpdateView):
    queryset = City.objects.all()
    template_name = "cities/city.html"
    form_class = CityForm2
    success_url = reverse_lazy('all_cities')
    success_message = "%(name)s was updated successfully"


class CityDeleteView(SuccessMessageMixin, generic.DeleteView):
    queryset = City.objects.all()
    template_name = "cities/city.html"
    success_url = reverse_lazy('all_cities')

    def get(self, request, **kwargs):
        messages.warning(request, "Object was deleted successfully")
        return self.post(request, **kwargs)



class CityListView(SuccessMessageMixin, generic.ListView):
    model = City
    template_name = 'cities/cities.html'
    context_object_name = 'cities'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        form = CityForm2()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context
