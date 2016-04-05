import json

from django.shortcuts import render
from django.views.generic import CreateView
from reception.models import Doctor, Reception


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return "{month}/{day}/{year}".format(
            year=obj.year,
            month=obj.month,
            day=obj.day
        )
    return obj


class ReceptionCreateView(CreateView):
    model = Reception
    fields = ['doctor', 'date', 'hour', 'full_name']
    success_url = 'success'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = json.dumps(list(Doctor.objects.all().values()))
        data = list(Reception.objects.all().values())
        data = json.dumps(data, default=date_handler)
        context['data'] = data
        return context
