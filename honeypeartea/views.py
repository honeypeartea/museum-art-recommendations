import datetime
from django.core.exceptions import ValidationError
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.static import serve
from django.urls import reverse
import hashlib
import os, csv, numpy
import pprint


from honeypeartea.forms import cmaInput, ngaInput, louvreInput,rijksInput, randomInput

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cma(request):
    return render(request, 'cma.html')

def nga(request):
    return render(request, 'nga.html')

def louvre(request):
    return render(request, 'louvre.html')

def rijksmuseum(request):
    return render(request, 'rijksmuseum.html')

def random(request):
    return render(request, 'random.html')




class cma_form(TemplateView):
    templatename = 'cma.html'

    def csv2list(self, csvpath):
        with open(csvpath, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
            return data

    def get(self, request):
        form = cmaInput()
        return render(request, self. templatename, {'form': form})

    def post(self, request):
        form = cmaInput(request.POST)
        if form.is_valid():
            dict = {}
            raw_data = []
            art_name = form.cleaned_data['art_name']
            artists = form.cleaned_data['artists']
            all = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/cleveland_with_rec.csv'))
            if artists != 'none':
                data = self.csv2list(os.path.join(PROJECT_ROOT, 'static/artist/cleveland_artists.csv'))
                for row in data:
                    if row[0] == artists:
                        raw_data = row
                        break
            elif art_name != "":
                raw_data = []
                for row in all:
                    if row[1] == art_name:
                        raw_data = row[9:]
                        break

            if raw_data != []:
                dict = {
                    'a': {'name': 'Art name: ' + all[int(raw_data[1])][1], 'year': 'Year: ' + all[int(raw_data[1])][2],
                          'text': "Description: " + (
                              all[int(raw_data[1])][8] if all[int(raw_data[1])][8] != "" else all[int(raw_data[1])][5]),
                          'link': all[int(raw_data[1])][6]},
                    'b': {'name': 'Art name: ' + all[int(raw_data[2])][1], 'year': 'Year: ' + all[int(raw_data[2])][2],
                          'text': "Description: " + (
                              all[int(raw_data[2])][8] if all[int(raw_data[2])][8] != "" else all[int(raw_data[2])][5]),
                          'link': all[int(raw_data[2])][6]},
                    'c': {'name': 'Art name: ' + all[int(raw_data[3])][1], 'year': 'Year: ' + all[int(raw_data[3])][2],
                          'text': "Description: " + (
                              all[int(raw_data[3])][8] if all[int(raw_data[3])][8] != "" else all[int(raw_data[3])][5]),
                          'link': all[int(raw_data[3])][6]},
                    'd': {'name': 'Art name: ' + all[int(raw_data[4])][1], 'year': 'Year: ' + all[int(raw_data[4])][2],
                          'text': "Description: " + (
                              all[int(raw_data[4])][8] if all[int(raw_data[4])][8] != "" else all[int(raw_data[4])][5]),
                          'link': all[int(raw_data[4])][6]},
                    'e': {'name': 'Art name: ' + all[int(raw_data[5])][1], 'year': 'Year: ' + all[int(raw_data[5])][2],
                          'text': "Description: " + (
                              all[int(raw_data[5])][8] if all[int(raw_data[5])][8] != "" else all[int(raw_data[5])][5]),
                          'link': all[int(raw_data[5])][6]},
                    'f': {'name': 'Art name: ' + all[int(raw_data[6])][1], 'year': 'Year: ' + all[int(raw_data[6])][2],
                          'text': "Description: " + (
                              all[int(raw_data[6])][8] if all[int(raw_data[6])][8] != "" else all[int(raw_data[6])][5]),
                          'link': all[int(raw_data[6])][6]},
                    'g': {'name': 'Art name: ' + all[int(raw_data[7])][1], 'year': 'Year: ' + all[int(raw_data[7])][2],
                          'text': "Description: " + (
                              all[int(raw_data[7])][8] if all[int(raw_data[7])][8] != "" else all[int(raw_data[7])][5]),
                          'link': all[int(raw_data[7])][6]},
                    'h': {'name': 'Art name: ' + all[int(raw_data[8])][1], 'year': 'Year: ' + all[int(raw_data[8])][2],
                          'text': "Description: " + (
                              all[int(raw_data[8])][8] if all[int(raw_data[8])][8] != "" else all[int(raw_data[8])][5]),
                          'link': all[int(raw_data[8])][6]},
                    'i': {'name': 'Art name: ' + all[int(raw_data[9])][1], 'year': 'Year: ' + all[int(raw_data[9])][2],
                          'text': "Description: " + (
                              all[int(raw_data[9])][8] if all[int(raw_data[9])][8] != "" else all[int(raw_data[9])][5]),
                          'link': all[int(raw_data[9])][6]},
                    'j': {'name': 'Art name: ' + all[int(raw_data[10])][1],
                          'year': 'Year: ' + all[int(raw_data[10])][2],
                          'text': "Description: " + (
                              all[int(raw_data[10])][8] if all[int(raw_data[10])][8] != "" else all[int(raw_data[10])][
                                  5]), 'link': all[int(raw_data[10])][6]},
                }

            if dict =={}:
                result = "Please enter valid artwork name or select artist"
            else:
                result = dict

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)


class nga_form(TemplateView):
    templatename = 'nga.html'

    def csv2list(self, csvpath):
        with open(csvpath, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
            return data

    def get(self, request):
        form = ngaInput()
        return render(request, self. templatename, {'form': form})

    def post(self, request):
        form = ngaInput(request.POST)
        if form.is_valid():
            dict = {}
            raw_data = []
            art_name = form.cleaned_data['art_name']
            artists = form.cleaned_data['artists']
            all = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/nga_with_rec.csv'))
            if artists != 'none':
                data = self.csv2list(os.path.join(PROJECT_ROOT, 'static/artist/nga_artists.csv'))
                for row in data:
                    if row[0] == artists:
                        raw_data = row
                        break
            elif art_name != "":
                raw_data = []
                for row in all:
                    if row[1] == art_name:
                        raw_data = row[10:]
                        break

            if raw_data != []:
                dict = {
                    'a': {'name': 'Art name: ' + all[int(raw_data[1])][1], 'year': 'Year: ' + all[int(raw_data[1])][2],
                          'text': "Description: " + (
                              all[int(raw_data[1])][10] if all[int(raw_data[1])][10] != "" else all[int(raw_data[1])][8]),
                          'link': all[int(raw_data[1])][9]},
                    'b': {'name': 'Art name: ' + all[int(raw_data[2])][1], 'year': 'Year: ' + all[int(raw_data[2])][2],
                          'text': "Description: " + (
                              all[int(raw_data[2])][10] if all[int(raw_data[2])][10] != "" else all[int(raw_data[2])][8]),
                          'link': all[int(raw_data[2])][9]},
                    'c': {'name': 'Art name: ' + all[int(raw_data[3])][1], 'year': 'Year: ' + all[int(raw_data[3])][2],
                          'text': "Description: " + (
                              all[int(raw_data[3])][10] if all[int(raw_data[3])][10] != "" else all[int(raw_data[3])][8]),
                          'link': all[int(raw_data[3])][9]},
                    'd': {'name': 'Art name: ' + all[int(raw_data[4])][1], 'year': 'Year: ' + all[int(raw_data[4])][2],
                          'text': "Description: " + (
                              all[int(raw_data[4])][10] if all[int(raw_data[4])][10] != "" else all[int(raw_data[4])][8]),
                          'link': all[int(raw_data[4])][9]},
                    'e': {'name': 'Art name: ' + all[int(raw_data[5])][1], 'year': 'Year: ' + all[int(raw_data[5])][2],
                          'text': "Description: " + (
                              all[int(raw_data[5])][10] if all[int(raw_data[5])][10] != "" else all[int(raw_data[5])][8]),
                          'link': all[int(raw_data[5])][9]},
                    'f': {'name': 'Art name: ' + all[int(raw_data[6])][1], 'year': 'Year: ' + all[int(raw_data[6])][2],
                          'text': "Description: " + (
                              all[int(raw_data[6])][10] if all[int(raw_data[6])][10] != "" else all[int(raw_data[6])][8]),
                          'link': all[int(raw_data[6])][9]},
                    'g': {'name': 'Art name: ' + all[int(raw_data[7])][1], 'year': 'Year: ' + all[int(raw_data[7])][2],
                          'text': "Description: " + (
                              all[int(raw_data[7])][10] if all[int(raw_data[7])][10] != "" else all[int(raw_data[7])][8]),
                          'link': all[int(raw_data[7])][9]},
                    'h': {'name': 'Art name: ' + all[int(raw_data[8])][1], 'year': 'Year: ' + all[int(raw_data[8])][2],
                          'text': "Description: " + (
                              all[int(raw_data[8])][10] if all[int(raw_data[8])][10] != "" else all[int(raw_data[8])][8]),
                          'link': all[int(raw_data[8])][9]},
                    'i': {'name': 'Art name: ' + all[int(raw_data[9])][1], 'year': 'Year: ' + all[int(raw_data[9])][2],
                          'text': "Description: " + (
                              all[int(raw_data[9])][10] if all[int(raw_data[9])][10] != "" else all[int(raw_data[9])][8]),
                          'link': all[int(raw_data[9])][9]},
                    'j': {'name': 'Art name: ' + all[int(raw_data[10])][1],
                          'year': 'Year: ' + all[int(raw_data[10])][2],
                          'text': "Description: " + (
                              all[int(raw_data[10])][10] if all[int(raw_data[10])][10] != "" else all[int(raw_data[10])][
                                  8]), 'link': all[int(raw_data[10])][9]},
                }

            if dict =={}:
                result = "Please enter valid artwork name or select artist"
            else:
                result = dict

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)


class louvre_form(TemplateView):
    templatename = 'louvre.html'

    def csv2list(self, csvpath):
        with open(csvpath, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
            return data

    def get(self, request):
        form = louvreInput()
        return render(request, self. templatename, {'form': form})

    def post(self, request):
        form = louvreInput(request.POST)
        if form.is_valid():
            dict = {}
            raw_data = []
            art_name = form.cleaned_data['art_name']
            artists = form.cleaned_data['artists']
            all = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/louvre_with_rec.csv'))
            if artists != 'none':
                data = self.csv2list(os.path.join(PROJECT_ROOT, 'static/artist/louvre_artists.csv'))
                for row in data:
                    if row[0] == artists:
                        raw_data = row
                        break
            elif art_name != "":
                raw_data = []
                for row in all:
                    if row[1] == art_name:
                        raw_data = row[11:]
                        break

            if raw_data != []:
                dict = {
                    'a': {'name': 'Art name: ' + all[int(raw_data[1])][1], 'year': 'Year: ' + all[int(raw_data[1])][3],
                          'text': "Description: " + (
                              all[int(raw_data[1])][11] if all[int(raw_data[1])][11] != "" else all[int(raw_data[1])][6]),
                          'link': all[int(raw_data[1])][5]},
                    'b': {'name': 'Art name: ' + all[int(raw_data[2])][1], 'year': 'Year: ' + all[int(raw_data[2])][3],
                          'text': "Description: " + (
                              all[int(raw_data[2])][11] if all[int(raw_data[2])][11] != "" else all[int(raw_data[2])][6]),
                          'link': all[int(raw_data[2])][5]},
                    'c': {'name': 'Art name: ' + all[int(raw_data[3])][1], 'year': 'Year: ' + all[int(raw_data[3])][3],
                          'text': "Description: " + (
                              all[int(raw_data[3])][11] if all[int(raw_data[3])][11] != "" else all[int(raw_data[3])][6]),
                          'link': all[int(raw_data[3])][5]},
                    'd': {'name': 'Art name: ' + all[int(raw_data[4])][1], 'year': 'Year: ' + all[int(raw_data[4])][3],
                          'text': "Description: " + (
                              all[int(raw_data[4])][11] if all[int(raw_data[4])][11] != "" else all[int(raw_data[4])][6]),
                          'link': all[int(raw_data[4])][5]},
                    'e': {'name': 'Art name: ' + all[int(raw_data[5])][1], 'year': 'Year: ' + all[int(raw_data[5])][3],
                          'text': "Description: " + (
                              all[int(raw_data[5])][11] if all[int(raw_data[5])][11] != "" else all[int(raw_data[5])][6]),
                          'link': all[int(raw_data[5])][5]},
                    'f': {'name': 'Art name: ' + all[int(raw_data[6])][1], 'year': 'Year: ' + all[int(raw_data[6])][3],
                          'text': "Description: " + (
                              all[int(raw_data[6])][11] if all[int(raw_data[6])][11] != "" else all[int(raw_data[6])][6]),
                          'link': all[int(raw_data[6])][5]},
                    'g': {'name': 'Art name: ' + all[int(raw_data[7])][1], 'year': 'Year: ' + all[int(raw_data[7])][3],
                          'text': "Description: " + (
                              all[int(raw_data[7])][11] if all[int(raw_data[7])][11] != "" else all[int(raw_data[7])][6]),
                          'link': all[int(raw_data[7])][5]},
                    'h': {'name': 'Art name: ' + all[int(raw_data[8])][1], 'year': 'Year: ' + all[int(raw_data[8])][3],
                          'text': "Description: " + (
                              all[int(raw_data[8])][11] if all[int(raw_data[8])][11] != "" else all[int(raw_data[8])][6]),
                          'link': all[int(raw_data[8])][5]},
                    'i': {'name': 'Art name: ' + all[int(raw_data[9])][1], 'year': 'Year: ' + all[int(raw_data[9])][3],
                          'text': "Description: " + (
                              all[int(raw_data[9])][11] if all[int(raw_data[9])][11] != "" else all[int(raw_data[9])][6]),
                          'link': all[int(raw_data[9])][5]},
                    'j': {'name': 'Art name: ' + all[int(raw_data[10])][1],
                          'year': 'Year: ' + all[int(raw_data[10])][3],
                          'text': "Description: " + (
                              all[int(raw_data[10])][11] if all[int(raw_data[10])][11] != "" else all[int(raw_data[10])][
                                  6]), 'link': all[int(raw_data[10])][5]},
                }

            if dict =={}:
                result = "Please enter valid artwork name or select artist"
            else:
                result = dict

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)


class rijks_form(TemplateView):
    templatename = 'rijksmuseum.html'

    def csv2list(self, csvpath):
        with open(csvpath, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
            return data

    def get(self, request):
        form = rijksInput()
        return render(request, self. templatename, {'form': form})

    def post(self, request):
        form = rijksInput(request.POST)
        if form.is_valid():
            dict = {}
            raw_data = []
            art_name = form.cleaned_data['art_name']
            artists = form.cleaned_data['artists']
            all = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/rijks_with_rec.csv'))
            if artists != 'none':
                data = self.csv2list(os.path.join(PROJECT_ROOT, 'static/artist/rijks_artists.csv'))
                for row in data:
                    if row[0] == artists:
                        raw_data = row
                        break
            elif art_name != "":
                raw_data = []
                for row in all:
                    if row[1] == art_name:
                        raw_data = row[10:21]
                        break

            if raw_data != []:

                dict = {
                    'a': {'name': 'Art name: ' + all[int(raw_data[1])][1], 'year': 'Year: ' + all[int(raw_data[1])][3],
                          'text': "Description: " + (
                              all[int(raw_data[1])][9] if all[int(raw_data[1])][9] != "" else all[int(raw_data[1])][5]),
                          'link': all[int(raw_data[1])][-1]},
                    'b': {'name': 'Art name: ' + all[int(raw_data[2])][1], 'year': 'Year: ' + all[int(raw_data[2])][3],
                          'text': "Description: " + (
                              all[int(raw_data[2])][9] if all[int(raw_data[2])][9] != "" else all[int(raw_data[2])][5]),
                          'link': all[int(raw_data[2])][-1]},
                    'c': {'name': 'Art name: ' + all[int(raw_data[3])][1], 'year': 'Year: ' + all[int(raw_data[3])][3],
                          'text': "Description: " + (
                              all[int(raw_data[3])][9] if all[int(raw_data[3])][9] != "" else all[int(raw_data[3])][5]),
                          'link': all[int(raw_data[3])][-1]},
                    'd': {'name': 'Art name: ' + all[int(raw_data[4])][1], 'year': 'Year: ' + all[int(raw_data[4])][3],
                          'text': "Description: " + (
                              all[int(raw_data[4])][9] if all[int(raw_data[4])][9] != "" else all[int(raw_data[4])][5]),
                          'link': all[int(raw_data[4])][-1]},
                    'e': {'name': 'Art name: ' + all[int(raw_data[5])][1], 'year': 'Year: ' + all[int(raw_data[5])][3],
                          'text': "Description: " + (
                              all[int(raw_data[5])][9] if all[int(raw_data[5])][9] != "" else all[int(raw_data[5])][5]),
                          'link': all[int(raw_data[5])][-1]},
                    'f': {'name': 'Art name: ' + all[int(raw_data[6])][1], 'year': 'Year: ' + all[int(raw_data[6])][3],
                          'text': "Description: " + (
                              all[int(raw_data[6])][9] if all[int(raw_data[6])][9] != "" else all[int(raw_data[6])][5]),
                          'link': all[int(raw_data[6])][-1]},
                    'g': {'name': 'Art name: ' + all[int(raw_data[7])][1], 'year': 'Year: ' + all[int(raw_data[7])][3],
                          'text': "Description: " + (
                              all[int(raw_data[7])][9] if all[int(raw_data[7])][9] != "" else all[int(raw_data[7])][5]),
                          'link': all[int(raw_data[7])][-1]},
                    'h': {'name': 'Art name: ' + all[int(raw_data[8])][1], 'year': 'Year: ' + all[int(raw_data[8])][3],
                          'text': "Description: " + (
                              all[int(raw_data[8])][9] if all[int(raw_data[8])][9] != "" else all[int(raw_data[8])][5]),
                          'link': all[int(raw_data[8])][-1]},
                    'i': {'name': 'Art name: ' + all[int(raw_data[9])][1], 'year': 'Year: ' + all[int(raw_data[9])][3],
                          'text': "Description: " + (
                              all[int(raw_data[9])][9] if all[int(raw_data[9])][9] != "" else all[int(raw_data[9])][5]),
                          'link': all[int(raw_data[9])][-1]},
                    'j': {'name': 'Art name: ' + all[int(raw_data[10])][1],
                          'year': 'Year: ' + all[int(raw_data[10])][3],
                          'text': "Description: " + (
                              all[int(raw_data[10])][9] if all[int(raw_data[10])][9] != "" else all[int(raw_data[10])][
                                  5]), 'link': all[int(raw_data[10])][-1]},
                }

            if dict =={}:
                result = "Please enter valid artwork name or select artist"
            else:
                result = dict

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)

class random_form(TemplateView):
    templatename = 'random.html'

    def csv2list(self, csvpath):
        with open(csvpath, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
            return data

    def get(self, request):
        form = randomInput()
        return render(request, self. templatename, {'form': form})

    def post(self, request):
        form = randomInput(request.POST)
        if form.is_valid():
            dict = {}
            raw_data = []
            text = form.cleaned_data['text']
            color = form.cleaned_data['color']
            cma = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/cleveland_with_rec.csv'))
            nga =  self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/nga_with_rec.csv'))
            louvre = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/louvre_with_rec.csv'))
            rijks = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/rijks_with_rec.csv'))

            if text != "":
                raw_data = numpy.random.randint(low = 0, high = len(cma), size = 11)
                raw_data = [int(i) for i in raw_data]
                if raw_data != []:
                    dict = {
                        'a': {'name': 'Art name: ' + cma[int(raw_data[1])][1],
                              'year': 'Year: ' + cma[int(raw_data[1])][2],
                              'text': "Description: " + (
                                  cma[int(raw_data[1])][8] if cma[int(raw_data[1])][8] != "" else cma[int(raw_data[1])][
                                      5]),
                              'link': cma[int(raw_data[1])][6]},
                        'b': {'name': 'Art name: ' + cma[int(raw_data[2])][1],
                              'year': 'Year: ' + cma[int(raw_data[2])][2],
                              'text': "Description: " + (
                                  cma[int(raw_data[2])][8] if cma[int(raw_data[2])][8] != "" else cma[int(raw_data[2])][
                                      5]),
                              'link': cma[int(raw_data[2])][6]},
                        'c': {'name': 'Art name: ' + nga[int(raw_data[3])][1],
                              'year': 'Year: ' + nga[int(raw_data[3])][2],
                              'text': "Description: " + (
                                  nga[int(raw_data[3])][10] if nga[int(raw_data[3])][10] != "" else
                                  nga[int(raw_data[3])][8]),
                              'link': nga[int(raw_data[3])][9]},
                        'd': {'name': 'Art name: ' + nga[int(raw_data[4])][1],
                              'year': 'Year: ' + nga[int(raw_data[4])][2],
                              'text': "Description: " + (
                                  nga[int(raw_data[4])][10] if nga[int(raw_data[4])][10] != "" else
                                  nga[int(raw_data[4])][8]),
                              'link': nga[int(raw_data[4])][9]},
                        'e': {'name': 'Art name: ' + louvre[int(raw_data[5])][1],
                              'year': 'Year: ' + louvre[int(raw_data[5])][3],
                              'text': "Description: " + (
                                  louvre[int(raw_data[5])][11] if louvre[int(raw_data[5])][11] != "" else
                                  louvre[int(raw_data[5])][
                                      6]),
                              'link': louvre[int(raw_data[5])][5]},
                        'f': {'name': 'Art name: ' + louvre[int(raw_data[6])][1],
                              'year': 'Year: ' + louvre[int(raw_data[6])][3],
                              'text': "Description: " + (
                                  louvre[int(raw_data[6])][11] if louvre[int(raw_data[6])][11] != "" else
                                  louvre[int(raw_data[6])][
                                      6]),
                              'link': louvre[int(raw_data[6])][5]},
                        'g': {'name': 'Art name: ' + louvre[int(raw_data[7])][1],
                              'year': 'Year: ' + louvre[int(raw_data[7])][3],
                              'text': "Description: " + (
                                  louvre[int(raw_data[7])][11] if louvre[int(raw_data[7])][11] != "" else
                                  louvre[int(raw_data[7])][
                                      6]),
                              'link': louvre[int(raw_data[7])][5]},
                        'h': {'name': 'Art name: ' + louvre[int(raw_data[8])][1],
                              'year': 'Year: ' + louvre[int(raw_data[8])][3],
                              'text': "Description: " + (
                                  louvre[int(raw_data[8])][11] if louvre[int(raw_data[8])][11] != "" else
                                  louvre[int(raw_data[8])][
                                      6]),
                              'link': louvre[int(raw_data[8])][5]},
                        'i': {'name': 'Art name: ' + rijks[int(raw_data[9])][1],
                              'year': 'Year: ' + rijks[int(raw_data[9])][3],
                              'text': "Description: " + (
                                  rijks[int(raw_data[9])][9] if rijks[int(raw_data[9])][9] != "" else
                                  rijks[int(raw_data[9])][5]),
                              'link': rijks[int(raw_data[9])][-1]},
                        'j': {'name': 'Art name: ' + rijks[int(raw_data[10])][1],
                              'year': 'Year: ' + rijks[int(raw_data[10])][3],
                              'text': "Description: " + (
                                  rijks[int(raw_data[10])][9] if rijks[int(raw_data[10])][9] != "" else
                                  rijks[int(raw_data[10])][
                                      5]), 'link': rijks[int(raw_data[10])][-1]},
                    }
            elif color != 'none':
                color_nga = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/color_nga.csv'))
                if color == 'red':
                    raw_data = color_nga[0]
                elif color == 'blue':
                    raw_data = color_nga[1]
                elif color == 'green':
                    raw_data = color_nga[2]
                if raw_data != []:
                    all = nga
                    dict = {
                        'a': {'name': 'Art name: ' + all[int(raw_data[1])][1],
                              'year': 'Year: ' + all[int(raw_data[1])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[1])][10] if all[int(raw_data[1])][10] != "" else
                                  all[int(raw_data[1])][8]),
                              'link': all[int(raw_data[1])][9]},
                        'b': {'name': 'Art name: ' + all[int(raw_data[2])][1],
                              'year': 'Year: ' + all[int(raw_data[2])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[2])][10] if all[int(raw_data[2])][10] != "" else
                                  all[int(raw_data[2])][8]),
                              'link': all[int(raw_data[2])][9]},
                        'c': {'name': 'Art name: ' + all[int(raw_data[3])][1],
                              'year': 'Year: ' + all[int(raw_data[3])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[3])][10] if all[int(raw_data[3])][10] != "" else
                                  all[int(raw_data[3])][8]),
                              'link': all[int(raw_data[3])][9]},
                        'd': {'name': 'Art name: ' + all[int(raw_data[4])][1],
                              'year': 'Year: ' + all[int(raw_data[4])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[4])][10] if all[int(raw_data[4])][10] != "" else
                                  all[int(raw_data[4])][8]),
                              'link': all[int(raw_data[4])][9]},
                        'e': {'name': 'Art name: ' + all[int(raw_data[5])][1],
                              'year': 'Year: ' + all[int(raw_data[5])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[5])][10] if all[int(raw_data[5])][10] != "" else
                                  all[int(raw_data[5])][8]),
                              'link': all[int(raw_data[5])][9]},
                        'f': {'name': 'Art name: ' + all[int(raw_data[6])][1],
                              'year': 'Year: ' + all[int(raw_data[6])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[6])][10] if all[int(raw_data[6])][10] != "" else
                                  all[int(raw_data[6])][8]),
                              'link': all[int(raw_data[6])][9]},
                        'g': {'name': 'Art name: ' + all[int(raw_data[7])][1],
                              'year': 'Year: ' + all[int(raw_data[7])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[7])][10] if all[int(raw_data[7])][10] != "" else
                                  all[int(raw_data[7])][8]),
                              'link': all[int(raw_data[7])][9]},
                        'h': {'name': 'Art name: ' + all[int(raw_data[8])][1],
                              'year': 'Year: ' + all[int(raw_data[8])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[8])][10] if all[int(raw_data[8])][10] != "" else
                                  all[int(raw_data[8])][8]),
                              'link': all[int(raw_data[8])][9]},
                        'i': {'name': 'Art name: ' + all[int(raw_data[9])][1],
                              'year': 'Year: ' + all[int(raw_data[9])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[9])][10] if all[int(raw_data[9])][10] != "" else
                                  all[int(raw_data[9])][8]),
                              'link': all[int(raw_data[9])][9]},
                        'j': {'name': 'Art name: ' + all[int(raw_data[10])][1],
                              'year': 'Year: ' + all[int(raw_data[10])][2],
                              'text': "Description: " + (
                                  all[int(raw_data[10])][10] if all[int(raw_data[10])][10] != "" else
                                  all[int(raw_data[10])][
                                      8]), 'link': all[int(raw_data[10])][9]},
                    }





            if dict =={}:
                result = "Please enter valid text or select color"
            else:
                result = dict

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)