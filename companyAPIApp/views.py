from django.views import View
from .models import Company
from django.http import JsonResponse
from django.forms.models import model_to_dict


class CompanyListView(View):

    def get(self, request):
        if 'name' in request.GET:
            company_data = Company.objects.filter(name__contains=request.GET['name'])
        else:
            company_data = Company.objects.all()
        return  JsonResponse(list(company_data.values()), safe=False)



class CompanyDetailView(View):

    def get(self, request, pk):
        company_data = Company.objects.get(pk=pk)
        return   JsonResponse(model_to_dict(company_data))