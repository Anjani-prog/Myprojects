from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
 
# Create your views here.
from modelforms.models import Car
 
# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'car_list'
    template_name = 'modelforms/index.html'
 
    def get_queryset(self):
        return Car.objects.all()
 
# view for the entry page
class Entry(CreateView):
    model = Car
    # the fields mentioned below become the entry rows in the generated form
    fields = ['car_name', 'car_price', 'car_horsepower', 'car_mileage','car_brand', 'car_fueltype', 'car_geartype']
 
# view for the update page
class CarUpdate(UpdateView):
    model = Car
    # the fields mentioned below become the entyr rows in the update form
    fields = ['car_name', 'car_price', 'car_horsepower', 'car_mileage','car_brand', 'car_fueltype', 'car_geartype']
 
# view for deleting a entry
class CarDelete(DeleteView):
    model = Car
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('modelforms:index')
