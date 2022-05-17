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
import os, csv
import pprint


from honeypeartea.forms import SchoolPredict, AdmissionChance, HistoryAdmission, cmaInput

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def requirement(request):
    return render(request, 'requirement.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

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


class school_predict(TemplateView):
    templatename = 'prediction.html'

    def get(self, request):
        form = SchoolPredict()
        return render(request, self.templatename, {'form': form})

    def post(self, request):
        form = SchoolPredict(request.POST)
        if form.is_valid():
            schoolrank = form.cleaned_data['schoolrank']
            gpa = form.cleaned_data['gpa']
            race = form.cleaned_data['race']
            sat = form.cleaned_data['sat']
            ap = form.cleaned_data['ap']

            # Main decision conditions
            if gpa >= 3.7 and schoolrank == 'top_30':
                print(f' === You will get in UCLA!!!! ===')
                result = 'UC Berkeley'
            elif gpa >= 3.5 and schoolrank == 'top_30':
                result = 'UCLA'
            elif gpa >= 3.0 and schoolrank == 'top_30':
                result = 'UC San Diego'
            elif gpa >= 3.0 and schoolrank == 'top_50':
                result = 'UC Santa Barbara'
            elif gpa >= 3.0 and schoolrank == 'top_70':
                result = 'UC Irvine'
            elif gpa >= 3.0 and schoolrank == 'top_100':
                result = 'UC Davis'
            elif gpa >= 2.5 and schoolrank == 'top_70':
                result = 'UC Santa Cruz'
            elif gpa >= 2.5 and schoolrank == 'top_100':
                result = 'UC Riverside'
            else:
                result = 'UC Merced'

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)

class admission_chance(TemplateView):
    templatename = 'chance.html'

    def get(self, request):
        form = AdmissionChance()
        return render(request, self.templatename, {'form': form})

    def post(self, request):
        form = AdmissionChance(request.POST)
        if form.is_valid():
            schoolrank = form.cleaned_data['schoolrank']
            gpa = form.cleaned_data['gpa']
            race = form.cleaned_data['race']
            sat = form.cleaned_data['sat']
            ap = form.cleaned_data['ap']
            college = form.cleaned_data['college']

            high = "You have a high chance of being admitted to UC "
            mid =  "You have a medium chance of being admitted to UC "
            low =  "You have a low chance of being admitted to UC"
            # Main decision conditions

            if college == 'Los Angeles':
                if gpa >= 3.5 and schoolrank == 'top_30':
                    result = high + college
                elif gpa >= 3.5 and schoolrank == 'top_50':
                    result = mid + college
                else:
                    result = low + college
            elif college == 'Berkeley':
                if gpa >= 3.7 and schoolrank == 'top_30':
                    result = high + college
                elif gpa >= 3.5 and schoolrank == 'top_50':
                    result = mid + college
                else:
                    result = low + college
            elif college == 'San Diego':
                if gpa >= 3.3 and schoolrank == 'top_30':
                    result = high + college
                elif gpa >= 3.0 and schoolrank == 'top_50':
                    result = mid + college
                else:
                    result = low + college
            elif college == 'Santa Barbara':
                if gpa >= 3.0 and schoolrank == 'top_30':
                    result = high + college
                elif gpa >= 2.7 and schoolrank == 'top_50':
                    result = mid + college
                else:
                    result = low + college
            elif college == 'Irvine':
                if gpa >= 3.5 and schoolrank == 'top_50':
                    result = high + college
                elif gpa >= 3.0 and schoolrank == 'top_70':
                    result = mid + college
                else:
                    result = low + college
            elif college == 'Davis':
                if gpa >= 3.0 and schoolrank == 'top_50':
                    result = high + college
                elif gpa >= 3.0 and schoolrank == 'top_70':
                    result = mid + college
                else:
                    result = low + college
            elif college == 'Santa Cruz':
                if gpa >= 3.0 and schoolrank == 'top_50':
                    result = high + college
                elif gpa >= 2.7 and schoolrank == 'top_70':
                    result = mid + college
                else:
                    result = low + college
            elif college == 'Riverside':
                if gpa >= 3.0 and schoolrank == 'top_50':
                    result = high + college
                elif gpa >= 2.5 and schoolrank == 'top_70':
                    result = mid + college
                else:
                    result = low + college
            elif college == 'Merced':
                if gpa >= 3.0 and schoolrank == 'top_70':
                    result = high + college
                elif gpa >= 2.5 and schoolrank == 'top_100':
                    result = mid + college
                else:
                    result = low + college
            else:
                print('=== you are fucked ===')
                result = "Please input again"

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)

class history_admission(TemplateView):
    templatename = 'history.html'

    def csv2list(self, csvpath):
        with open(csvpath, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            return data

    def get(self, request):
        form = HistoryAdmission()
        return render(request, self. templatename, {'form': form})

    def post(self, request):
        form = HistoryAdmission(request.POST)
        if form.is_valid():
            college = form.cleaned_data['college']
            year = form.cleaned_data['year']
            category = form.cleaned_data['category']

            # Check the result based on the searching category
            if category == 'race':
                data = self.csv2list(os.path.join(PROJECT_ROOT, 'static/race.csv'))
                dict = {
                    'Asian': 0,
                    'White': 0,
                    'Hispanic': 0,
                    'African': 0,
                    'Indian': 0
                }
                for row in data:
                    for race in dict.keys():
                        if row[2] == college and race in row[3]  and row[7] == str(year):
                            dict[race] += float(row[6])
                # Round up to 100
                value_sum = sum(dict.values())
                dict['Asian'] += (100-value_sum)/2
                dict['White'] += (100-value_sum)/2
                pprint.pprint(dict)
                result = dict

            elif category == 'gpa':
                data = self.csv2list(os.path.join(PROJECT_ROOT, 'static/gpa.csv'))
                for row in data:
                    if row[0] == str(year) and row[1] == college:
                        print(f' - Found it! GPA: {row[2]}')
                        result = row[2]

            elif category == 'sat':
                data = self.csv2list(os.path.join(PROJECT_ROOT, 'static/sat.csv'))
                for row in data:
                    if row[0] == college:
                        print(f' - Found it! SAT: {row[1]}')
                        result = row[1]
            else:
                result = 'Error input. Something went wrong.'
        result = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)


class cma_form(TemplateView):
    templatename = 'cma.html'

    def csv2list(self, csvpath):
        with open(csvpath, newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            print(header)
            data = list(reader)
            return data

    def get(self, request):
        form = cmaInput()
        return render(request, self. templatename, {'form': form})

    def post(self, request):
        form = cmaInput(request.POST)
        if form.is_valid():
            dict = {}
            art_name = form.cleaned_data['art_name']
            artists = form.cleaned_data['artists']
            all = self.csv2list(os.path.join(PROJECT_ROOT, 'static/resource/cleveland_with_rec.csv'))
            if artists != 'none':
                raw_data = []
                data = self.csv2list(os.path.join(PROJECT_ROOT, 'static/artist/cleveland_artists.csv'))
                for row in data:
                    if row[0] == artists:
                        raw_data = row
                        break
                if raw_data != []:
                    dict = {
                        'a': {'name': 'Art name: ' + all[int(raw_data[1])][1], 'year': 'Year: ' + all[int(raw_data[1])][2],
                              'text': "Description: " + (all[int(raw_data[1])][8] if all[int(raw_data[1])][8] != "" else all[int(raw_data[1])][5]), 'link': all[int(raw_data[1])][6]},
                        'b': {'name': 'Art name: ' + all[int(raw_data[2])][1], 'year': 'Year: ' + all[int(raw_data[2])][2],
                              'text': "Description: " + (all[int(raw_data[2])][8] if all[int(raw_data[2])][8] != "" else all[int(raw_data[2])][5]), 'link': all[int(raw_data[2])][6]},
                        'c': {'name': 'Art name: ' + all[int(raw_data[3])][1], 'year': 'Year: ' + all[int(raw_data[3])][2],
                              'text': "Description: " + (all[int(raw_data[3])][8] if all[int(raw_data[3])][8] != "" else all[int(raw_data[3])][5]), 'link': all[int(raw_data[3])][6]},
                        'd': {'name': 'Art name: ' + all[int(raw_data[4])][1], 'year': 'Year: ' + all[int(raw_data[4])][2],
                              'text': "Description: " + (all[int(raw_data[4])][8] if all[int(raw_data[4])][8] != "" else all[int(raw_data[4])][5]), 'link': all[int(raw_data[4])][6]},
                        'e': {'name': 'Art name: ' + all[int(raw_data[5])][1], 'year': 'Year: ' + all[int(raw_data[5])][2],
                              'text': "Description: " + (all[int(raw_data[5])][8] if all[int(raw_data[5])][8] != "" else all[int(raw_data[5])][5]), 'link': all[int(raw_data[5])][6]},
                        'f': {'name': 'Art name: ' + all[int(raw_data[6])][1], 'year': 'Year: ' + all[int(raw_data[6])][2],
                              'text': "Description: " + (all[int(raw_data[6])][8] if all[int(raw_data[6])][8] != "" else all[int(raw_data[6])][5]), 'link': all[int(raw_data[6])][6]},
                        'g': {'name': 'Art name: ' + all[int(raw_data[7])][1], 'year': 'Year: ' + all[int(raw_data[7])][2],
                              'text': "Description: " + (all[int(raw_data[7])][8] if all[int(raw_data[7])][8] != "" else all[int(raw_data[7])][5]), 'link': all[int(raw_data[7])][6]},
                        'h': {'name': 'Art name: ' + all[int(raw_data[8])][1], 'year': 'Year: ' + all[int(raw_data[8])][2],
                              'text': "Description: " + (all[int(raw_data[8])][8] if all[int(raw_data[8])][8] != "" else all[int(raw_data[8])][5]), 'link': all[int(raw_data[8])][6]},
                        'i': {'name': 'Art name: ' + all[int(raw_data[9])][1], 'year': 'Year: ' + all[int(raw_data[9])][2],
                              'text': "Description: " + (all[int(raw_data[9])][8] if all[int(raw_data[9])][8] != "" else all[int(raw_data[9])][5]), 'link': all[int(raw_data[9])][6]},
                        'j': {'name': 'Art name: ' + all[int(raw_data[10])][1], 'year': 'Year: ' + all[int(raw_data[10])][2],
                              'text': "Description: " + (all[int(raw_data[10])][8] if all[int(raw_data[10])][8] != "" else all[int(raw_data[10])][5]), 'link': all[int(raw_data[10])][6]},
                    }






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


            # Check the result based on the searching category

            if dict =={}:
                result = "Please enter artwork name or select artist"
            else:
                result = dict


        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)