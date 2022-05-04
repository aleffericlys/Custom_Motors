from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


import tasks, datetime
from tasks.models import Motos, Acessorios, Ferramentas

from .forms import MensageForm

@login_required
def taskHome(request):
	moto_list = Motos.objects.all()
	
	paginatorM = Paginator(moto_list, 3)
	pageM = request.GET.get('page')

	motos = paginatorM.get_page(pageM)

	acess_list = Acessorios.objects.all()
	
	paginatorA = Paginator(acess_list, 3)
	pageA = request.GET.get('page')

	acess = paginatorA.get_page(pageA)

	ferr_list = Ferramentas.objects.all()
	
	paginatorF = Paginator(ferr_list, 3)
	pageF = request.GET.get('page')

	ferr = paginatorF.get_page(pageF)

	return render(request, 'tasks/home.html', {'motos': motos, 'acess':acess, 'ferr': ferr})


@login_required
def taskContato(request):
	
	if request.method == 'POST':
    	
		form = MensageForm(request.POST)

		if form.is_valid():
			mensagem = form.save(commit=False)
			mensagem.user = request.user
			mensagem.save()
			return redirect('/')		
	else:	
		form = MensageForm()
		return render(request, 'tasks/contato.html', {'form': form}) 

@login_required
def taskQSomos(request):
	return render(request, 'tasks/quemSomos.html')

@login_required
def taskSobre(request):
	return render(request, 'tasks/sobre.html')

@login_required
def taskUser(request):
	return render(request, 'tasks/user.html')

@login_required
def taskLogin(request):
	return render(request, 'tasks/cadastro.html')

@login_required
def taskProduto(request):
	return render(request, 'tasks/produto.html')

@login_required
def taskList(request):
	
	search = request.GET.get('search')

	if search:
		moto_list = Motos.objects.filter(nome__icontains=search)
		acess_list = Acessorios.objects.filter(nome__icontains=search)
		ferr_list = Ferramentas.objects.filter(nome__icontains=search)
	else:
		moto_list = Motos.objects.all()
		acess_list = Acessorios.objects.all()
		ferr_list = Ferramentas.objects.all()
	
	paginatorM = Paginator(moto_list, 6)
	pageM = request.GET.get('page')

	motos = paginatorM.get_page(pageM)

	paginatorA = Paginator(acess_list, 6)
	pageA = request.GET.get('page')

	acess = paginatorA.get_page(pageA)

	paginatorF = Paginator(ferr_list, 6)
	pageF = request.GET.get('page')

	ferr = paginatorF.get_page(pageF)

	return render(request, 'tasks/estoque.html', {'motos': motos, 'acess':acess, 'ferr': ferr})



# def taskList(request):
# 	tasks = Task.objects.all()
# 	print(tasks)
# 	return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def taskViewM(request, id):
	item = get_object_or_404(Motos, pk=id)
	print('Acesso a Página de produto: '+ str(item) +' '+str(datetime.datetime.now()))

	item_list = Motos.objects.all()
	
	paginator = Paginator(item_list, 4)
	page = request.GET.get('page')

	items = paginator.get_page(page)

	return render(request, 'tasks/moto.html', {'item': item, 'items': items})


@login_required
def taskViewA(request, id, tipo):
	item = get_object_or_404(Acessorios, pk=id)
	print('Acesso a Página de produto: '+ str(item) +' '+str(datetime.datetime.now()))

	item_list = get_list_or_404(Acessorios, tipo=tipo)
	
	paginator = Paginator(item_list, 4)
	page = request.GET.get('page')

	items = paginator.get_page(page)

	return render(request, 'tasks/acessorio.html', {'item': item, 'items': items})


@login_required
def taskViewF(request, id, tipo):
	item = get_object_or_404(Ferramentas, pk=id)
	print('Acesso a Página de produto: '+ str(item) +' '+str(datetime.datetime.now()))

	item_list = get_list_or_404(Ferramentas, tipo=tipo)
	
	paginator = Paginator(item_list, 4)
	page = request.GET.get('page')

	items = paginator.get_page(page)

	return render(request, 'tasks/ferramenta.html', {'item': item, 'items': items})
# Create your views here.
