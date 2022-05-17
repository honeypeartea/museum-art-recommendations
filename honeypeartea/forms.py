import datetime
from django import forms
from django.core.exceptions import ValidationError

SCHOOLRANK = [
    ('top_30', '1 ~ 30'),
    ('top_50', '30 ~ 50'),
    ('top_70', '50 ~ 70'),
    ('top_70', '70 ~ 100'),
    ('over_100', 'after 100'),
]

RACE = [
    ('asian', 'Asian'),
    ('hispanic', 'Hispanic/Latino'),
    ('white', 'White'),
    ('indian', 'American Indian'),
    ('black', 'African American'),
]

COLLEGES = [
    ('San Diego', 'San Diego'),
    ('Los Angeles', 'Los Angeles'),
    ('Riverside', 'Riverside'),
    ('Irvine', 'Irvine'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Merced', 'Merced'),
    ('Davis', 'Davis'),
    ('Berkeley', 'Berkeley'),
    ('Santa Barbara', 'Santa Barbara'),
]

ATTRIBUTES = [
    ('gpa', 'GPA'),
    ('sat', 'SAT'),
    ('race', 'Race'),
]

YEARS = [(i, str(i)) for i in range(1994, 2017)]

class SchoolPredict(forms.Form):
    schoolrank = forms.CharField(label='School Ranking', widget=forms.Select(choices=SCHOOLRANK))
    gpa = forms.IntegerField()
    race = forms.CharField(label='Race', widget=forms.Select(choices=RACE))
    sat = forms.IntegerField()
    ap = forms.IntegerField()

class AdmissionChance(forms.Form):
    schoolrank = forms.CharField(label='School Ranking', widget=forms.Select(choices=SCHOOLRANK))
    gpa = forms.IntegerField()
    race = forms.CharField(label='Race', widget=forms.Select(choices=RACE))
    sat = forms.IntegerField()
    ap = forms.IntegerField()
    college = forms.CharField(label='College', widget=forms.Select(choices=COLLEGES))

class HistoryAdmission(forms.Form):
    college = forms.CharField(label='College', widget=forms.Select(choices=COLLEGES))
    year = forms.CharField(label='Year', widget=forms.Select(choices=YEARS))
    category = forms.CharField(label='Category', widget=forms.Select(choices=ATTRIBUTES))


class cmaInput(forms.Form):
    PEOPLE = [
        ('none', 'none'),
        ('Aoki Shukuya', 'Aoki Shukuya'),
        ('Basavana', 'Basavana'),
        ('Bian Shoumin', 'Bian Shoumin'),
        ('Chen Hongshou', 'Chen Hongshou'),
        ('Devachandra', 'Devachandra'),
        ('Fan Qi', 'Fan Qi'),
        ('George Inness', 'George Inness'),
        ('Hua Yan', 'Hua Yan'),
        ('Kano Tan’yū', 'Kano Tan’yū'),
        ('Mei Qing', 'Mei Qing'),
        ('Min Zhen', 'Min Zhen'),
        ('Pierre Rousseau', 'Pierre Rousseau'),
        ('Shen Zhou', 'Shen Zhou'),
        ('Shibata Zeshin', 'Shibata Zeshin'),
        ('Shitao', 'Shitao'),
        ('Shōrakusai', 'Shōrakusai'),
        ('Song Xu', 'Song Xu'),
        ('Tsubaki Chinzan', 'Tsubaki Chinzan'),
        ('Xiao Yuncong', 'Xiao Yuncong'),
        ('Zeng Yandong', 'Zeng Yandong'),
        ('Zha Shibiao', 'Zha Shibiao'),
        ('Zhai Dakun', 'Zhai Dakun'),
        ('Zhang Ruoai', 'Zhang Ruoai'),
    ]

    artists = forms.CharField(label='Artists', widget=forms.Select(choices=PEOPLE))
    art_name = forms.CharField(label='Artwork Name',required=False)
