from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from selenium import webdriver
from django.views.decorators.csrf import csrf_exempt
from selenium.webdriver.chrome.options import Options
from .models import Model

@csrf_exempt
def home(request):
    return render(request,'paginicial.html')

@csrf_exempt
def pesq(request):
    

    options = Options()
    options.add_argument("--headless")
    options.add_argument('--window-size=1920,1080')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f"user-agent={user_agent}")

    browser = webdriver.Chrome(
        "C:/Users/Mars/OneDrive - Mars Inc/Área de Trabalho/Projeto-webbot/proj/static/Dependencies/chromedriver_win32/chromedriver.exe",
        options=options)

    produto_procurado = request.POST.get("drink"), " ", request.POST.get('brand'), " ", request.POST.get('amount')

    productsCarrefour = Model.buscarProdutoCarrefour(browser, produto_procurado)

    template = loader.get_template('scrap.html')
    context = {
        'productsCarrefour': productsCarrefour,
        # 'productsTenda': productsCarrefour,
        # 'products': productsCarrefour,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
