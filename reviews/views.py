from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Review
from properties.models import Property

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        property_obj = get_object_or_404(Property, id=self.kwargs['property_id'])
        form.instance.property = property_obj
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('properties:detail', kwargs={'pk': self.kwargs['property_id']})
