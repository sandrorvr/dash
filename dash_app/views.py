from django.shortcuts import render
from .models import Dados

import pandas as pd
import random
import json

data = pd.read_csv('./scriptAux/bd_novo.csv')

context = {}

def generateColor(n):
    color = []
    for i in range(n):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color.append(f'rgba({r}, {g}, {b}, 1)')
    return color


def fKPI1():
    dic = {}
    dic['values'] = list(data['kpi1'].value_counts().values)
    dic['label'] = list(data['kpi1'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi1'].unique()))
    return dic


def fKPI2():
    dic = {}

    label = data['kpi2'].value_counts().index
    label = ['_'.join(i.split(' ')) for i in label]
    values = data['kpi2'].value_counts().values
    total = sum(values)
    values = [(i/total)*100 for i in values]

    for i in range(len(values)):
        dic[label[i]] =values[i]
    
    return dic


def fDescribe1():
    dic = {}

    counts = data['kpi2'].value_counts()
    success= counts['Success']
    del counts['Success']

    erro = sum([i for i in counts.values])

    total = erro + success

    dic['erro'] = round((erro/total)*100,2)
    dic['success'] = round((success/total)*100,2)
    dic['nulos'] = round((sum(data['countNull_N_expected'].values)/(len(data)*len(data.columns)))*100, 2)

    return dic


def fDescribe2():
    dic = {}

    counts = data['kpi9'].value_counts()
    mdx = counts['MDX']
    gdx = counts['GDX']

    del counts['MDX']
    del counts['GDX']

    Not_Decoded = sum([i for i in counts.values])

    total = mdx + gdx + Not_Decoded

    dic['Not_Decoded'] = round((Not_Decoded/total)*100,2)
    dic['MDX'] = round((mdx/total)*100,2)
    dic['GDX'] = round((gdx/total)*100,2)

    return dic


def fKPI3():
    dic = {}
    kpi1 = pd.crosstab(data.did_id, data.kpi1)

    for col in kpi1.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi1.loc[:,col].values)
    
    dic['did'] = list(kpi1.index)
    dic['color'] = generateColor(len(kpi1.columns))
    
    return dic

def fKPI4_did():
    dic = {}
    kpi4 = pd.crosstab(data.did_id, data.kpi4)

    for col in kpi4.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi4.loc[:,col].values)
    
    dic['did'] = list(kpi4.index)
    dic['color'] = generateColor(len(kpi4.columns))
    
    return dic


def fKPI5():
    dic = {}
    kpi5 = pd.crosstab(data.did_id, data.kpi5)

    for col in kpi5.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi5.loc[:,col].values)
    
    dic['did'] = list(kpi5.index)
    dic['color'] = generateColor(len(kpi5.columns))
    
    return dic


def fKPI4():
    dic = {}
    dic['values'] = list(data['kpi4'].value_counts().values)
    dic['label'] = list(data['kpi4'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi4'].unique()))
    return dic



def fKPI6():
    dic = {}
    dic['values'] = list(data['kpi6'].value_counts().values)
    dic['label'] = list(data['kpi6'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi6'].unique()))
    return dic



def fKPI7_did():
    dic = {}
    kpi7 = pd.crosstab(data.did_id, data.kpi7)

    for col in kpi7.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi7.loc[:,col].values)
    
    dic['did'] = list(kpi7.index)
    dic['color'] = generateColor(len(kpi7.columns))
    
    return dic

def fKPI7():
    dic = {}
    dic['values'] = list(data['kpi7'].value_counts().values)
    dic['label'] = list(data['kpi7'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi7'].unique()))
    return dic


def fKPI8():
    return {'label': round((sum(data['countNull_N_expected'].values)/(len(data)*len(data.columns)))*100, 2)}

def fKPI8_describe():
    dic = {}
    for vet in data['kpi8'].values:
        for col in json.loads(vet):
            previous_count = dic.get(col,0)
            dic[col] = previous_count + 1
    return dic



def fKPI9():
    dic = {}

    label = data['kpi9'].value_counts().index
    label = ['_'.join(i.split(' ')) for i in label]
    label = ['_'.join(i.split('/')) for i in label]
    values = data['kpi9'].value_counts().values
    total = sum(values)
    values = [(i/total)*100 for i in values]

    for i in range(len(values)):
        dic[label[i]] =values[i]
    
    return dic



def fKPI9_chart_did():
    dic = {}
    kpi9 = pd.crosstab(data.did_id, data.kpi9)

    for col in kpi9.columns:
        key = '_'.join(col.split(' '))
        dic[key] = list(kpi9.loc[:,col].values)
    
    dic['did'] = list(kpi9.index)
    dic['color'] = generateColor(len(kpi9.columns))
    
    return dic


def fKPI9_chart():
    dic = {}
    dic['values'] = list(data['kpi9'].value_counts().values)
    dic['label'] = list(data['kpi9'].value_counts().index)
    dic['color'] = generateColor(len(data['kpi9'].unique()))
    return dic




def index(request):

    context['kpi1'] = fKPI1()
    context['kpi2'] = fKPI2()
    context['kpi3'] = fKPI3()
    context['kpi4_did'] = fKPI4_did()
    context['kpi4'] = fKPI4()
    context['kpi5'] = fKPI5()
    context['kpi6'] = fKPI6()
    context['kpi7_did'] = fKPI7_did()
    context['kpi7'] = fKPI7()
    context['kpi8'] = fKPI8()
    context['kpi8_describe'] = fKPI8_describe()

    context['kpi9'] = fKPI9()
    context['kpi9_chart_did'] = fKPI9_chart_did()
    context['kpi9_chart'] = fKPI9_chart()

    context['describe1'] = fDescribe1()
    context['describe2'] = fDescribe2()
    
    return render(request, 'index.html', context)
