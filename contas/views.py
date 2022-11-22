from django.shortcuts import render, redirect
from .models import Transacao, Cliente
from .form import TransacaoForm, ClienteForm
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.views.generic.list import ListView

# Create your views here.
def home(request):

    return render(request, 'contas/home.html')

def listagem(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Transacao.objects.filter(descricao__contains=q)
    else:
        data = Transacao.objects.all()
    context = {
        'data': data
    }

    return render(request, 'contas/listagem.html', context)


def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form.html', data)

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')

def gerarPdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    
    transcoes = Transacao.objects.all()
    
    lines = []
    for transacao in transcoes:
        lines.append(transacao.descricao)
        lines.append(transacao.observacoes)
        lines.append(transacao.valor)
        lines.append("-------------")

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='relatorio.pdf')

def voltar(request):
    return redirect('url_listagem')

def listagemC(request):
    data ={}
    data['clientes'] = Cliente.objects.all()
    return render(request, 'contas/clientes.html', data)

def novo_cliente(request):
    data = {}
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_clientes')

    data['form'] = form
    return render(request, 'contas/addclientes.html', data)

def updateC(request, pk):
    data = {}
    clientes = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST or None, instance=clientes)
    
    if form.is_valid():
        form.save()
        return redirect('url_clientes')

    data['form'] = form
    data['cliente'] = clientes
    return render(request, 'contas/addclientes.html', data)

def deleteC(request, pk):
    clientes = Cliente.objects.get(pk=pk)
    clientes.delete()
    return redirect('url_clientes')
