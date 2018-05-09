from django.http import JsonResponse, HttpResponse
import requests
import pprint


API_URL = 'http://nlp-ultron.cs.nthu.edu.tw:2266/translate2'
HEADERS = {'Content-Type': 'application/json'}
pp = pprint.PrettyPrinter(indent=4)


def correct_it(request):
    if request.is_ajax() and request.method == 'POST':
        r = requests.post(API_URL, headers=HEADERS, data=request.body)
        # return JsonResponse(r.json())
        pp.pprint(r.json())
        return HttpResponse(content=r.content, status=r.status_code)
