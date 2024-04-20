from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.db import connection
from .forms import CreateTableForm
import pandas as pd
from .models import CustomTable
from . import dbcontab as ct

# Create your views here.

def contactlist(request):
    return render(request, "contactlist.html")


def create_table(request):
    if request.method == 'POST':
        form = CreateTableForm(request.POST)
        if form.is_valid():
            table_name = form.cleaned_data['table_name']
            table_name = "contactlist_" + table_name
            con = ct.connect_to_postgresql()
            rqst = ct.create_table(con, table_name)
            return render(request, 'contactlist_tables.html')
    else:
        form = CreateTableForm()
    return render(request, 'contactlist/create_table.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def contactlist_tables(request):
    con = ct.connect_to_postgresql()
    names = ct.get_table_names(con)
    print(names)
    return(request, 'contactlist/contactlist_tables.html', names)
