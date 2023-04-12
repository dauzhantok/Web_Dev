import json
from django.http.response import JsonResponse
from .models import Company,Vacancy


def company_list(request):
    # select * from company;
    if request.method == 'GET':
        company = Company.objects.all()
        company_json = [p.to_json() for p in company]
        return JsonResponse(company_json, safe=False)

def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())

def vacancy_detail(request, company_id):
    try:
        vacancy = Vacancy.objects.get(company=company_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
