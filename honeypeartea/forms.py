import datetime
from django import forms
from django.core.exceptions import ValidationError

# SCHOOLRANK = [
#     ('top_30', '1 ~ 30'),
#     ('top_50', '30 ~ 50'),
#     ('top_70', '50 ~ 70'),
#     ('top_70', '70 ~ 100'),
#     ('over_100', 'after 100'),
# ]
#
# RACE = [
#     ('asian', 'Asian'),
#     ('hispanic', 'Hispanic/Latino'),
#     ('white', 'White'),
#     ('indian', 'American Indian'),
#     ('black', 'African American'),
# ]
#
# COLLEGES = [
#     ('San Diego', 'San Diego'),
#     ('Los Angeles', 'Los Angeles'),
#     ('Riverside', 'Riverside'),
#     ('Irvine', 'Irvine'),
#     ('Santa Cruz', 'Santa Cruz'),
#     ('Merced', 'Merced'),
#     ('Davis', 'Davis'),
#     ('Berkeley', 'Berkeley'),
#     ('Santa Barbara', 'Santa Barbara'),
# ]
#
# ATTRIBUTES = [
#     ('gpa', 'GPA'),
#     ('sat', 'SAT'),
#     ('race', 'Race'),
# ]
#
# YEARS = [(i, str(i)) for i in range(1994, 2017)]
#
# class SchoolPredict(forms.Form):
#     schoolrank = forms.CharField(label='School Ranking', widget=forms.Select(choices=SCHOOLRANK))
#     gpa = forms.IntegerField()
#     race = forms.CharField(label='Race', widget=forms.Select(choices=RACE))
#     sat = forms.IntegerField()
#     ap = forms.IntegerField()
#
# class AdmissionChance(forms.Form):
#     schoolrank = forms.CharField(label='School Ranking', widget=forms.Select(choices=SCHOOLRANK))
#     gpa = forms.IntegerField()
#     race = forms.CharField(label='Race', widget=forms.Select(choices=RACE))
#     sat = forms.IntegerField()
#     ap = forms.IntegerField()
#     college = forms.CharField(label='College', widget=forms.Select(choices=COLLEGES))
#
# class HistoryAdmission(forms.Form):
#     college = forms.CharField(label='College', widget=forms.Select(choices=COLLEGES))
#     year = forms.CharField(label='Year', widget=forms.Select(choices=YEARS))
#     category = forms.CharField(label='Category', widget=forms.Select(choices=ATTRIBUTES))
#

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
    art_name = forms.CharField(label='Artwork Name', required=False)
    artists = forms.CharField(label='Artists', widget=forms.Select(choices=PEOPLE))

class ngaInput(forms.Form):
    PEOPLE = [
        ('none', 'none'),
        ('Amedeo Modigliani', 'Amedeo Modigliani'),
        ('André Derain', 'André Derain'),
        ('Auguste Renoir', 'Auguste Renoir'),
        ('Barnett Newman', 'Barnett Newman'),
        ('Bernardino Luini', 'Bernardino Luini'),
        ('Berthe Morisot', 'Berthe Morisot'),
        ('Camille Pissarro', 'Camille Pissarro'),
        ('Claude Monet', 'Claude Monet'),
        ('Eastman Johnson', 'Eastman Johnson'),
        ('Edgar Degas', 'Edgar Degas'),
        ('Edouard Manet', 'Edouard Manet'),
        ('Edouard Vuillard', 'Edouard Vuillard'),
        ('Erastus Salisbury Field', 'Erastus Salisbury Field'),
        ('Eugène Boudin', 'Eugène Boudin'),
        ('George Bellows', 'George Bellows'),
        ('George Catlin', 'George Catlin'),
        ('Georges Seurat', 'Georges Seurat'),
        ('Georgia O\'Keeffe','Georgia O\'Keeffe'),
        ('Gilbert Stuart', 'Gilbert Stuart'),
        ('Giovanni Battista Tiepolo', 'Giovanni Battista Tiepolo'),
        ('Henri Fantin-Latour', 'Henri Fantin-Latour'),
        ('Henri Matisse', 'Henri Matisse'),
        ('Henri de Toulouse-Lautrec', 'Henri de Toulouse-Lautrec'),
        ('Jacob Eichholtz', 'Jacob Eichholtz'),
        ('Jean Dubuffet', 'Jean Dubuffet'),
        ('Jean Honoré Fragonard', 'Jean Honoré Fragonard'),
        ('Jean-Baptiste-Camille Corot', 'Jean-Baptiste-Camille Corot'),
        ('Jean-Louis Forain', 'Jean-Louis Forain'),
        ('John Frederick Peto', 'John Frederick Peto'),
        ('John Marin', 'John Marin'),
        ('John Singer Sargent', 'John Singer Sargent'),
        ('John Singleton Copley', 'John Singleton Copley'),
        ('Joseph Mallord William Turner', 'Joseph Mallord William Turner'),
        ('Mark Rothko', 'Mark Rothko'),
        ('Mary Cassatt', 'Mary Cassatt'),
        ('Pablo Picasso', 'Pablo Picasso'),
        ('Paul Cézanne', 'Paul Cézanne'),
        ('Paul Gauguin', 'Paul Gauguin'),
        ('Pierre Bonnard', 'Pierre Bonnard'),
        ('Raoul Dufy', 'Raoul Dufy'),
        ('Rembrandt van Rijn', 'Rembrandt van Rijn'),
        ('Robert Mangold', 'Robert Mangold'),
        ('Sir Anthony van Dyck', 'Sir Anthony van Dyck'),
        ('Thomas Chambers', 'Thomas Chambers'),
        ('Thomas Cole', 'Thomas Cole'),
        ('Thomas Eakins', 'Thomas Eakins'),
        ('Thomas Gainsborough', 'Thomas Gainsborough'),
        ('Thomas Sully', 'Thomas Sully'),
        ('Vincent van Gogh', 'Vincent van Gogh'),
        ('Winslow Homer', 'Winslow Homer'),
    ]
    art_name = forms.CharField(label='Artwork Name', required=False)
    artists = forms.CharField(label='Artists', widget=forms.Select(choices=PEOPLE))

class louvreInput(forms.Form):
    PEOPLE = [
        ('none', 'none'),
        ('Alaux, Jean', 'Alaux, Jean'),
        ('Balke, Peder', 'Balke, Peder'),
        ('Berchem, Nicolaes Pietersz.', 'Berchem, Nicolaes Pietersz.'),
        ('Bernaerts, Nicasius', 'Bernaerts, Nicasius'),
        ('Biennourry, Victor François Eloi', 'Biennourry, Victor François Eloi'),
        ('Blin de Fontenay, Jean-Baptiste', 'Blin de Fontenay, Jean-Baptiste'),
        ('Blondel, Merry-Joseph', 'Blondel, Merry-Joseph'),
        ('Boel, Pieter', 'Boel, Pieter'),
        ('Bondoux, Jules-Georges', 'Bondoux, Jules-Georges'),
        ('Boucher, François', 'Boucher, François'),
        ('Boullogne, Louis II de, dit Le Jeune', 'Boullogne, Louis II de, dit Le Jeune'),
        ('Champaigne, Philippe de', 'Champaigne, Philippe de'),
        ('Chardin, Jean Baptiste Siméon', 'Chardin, Jean Baptiste Siméon'),
        ('Chassériau, Théodore', 'Chassériau, Théodore'),
        ('Clouet, François', 'Clouet, François'),
        ('Cornu, Sébastien', 'Cornu, Sébastien'),
        ('Corot, Jean-Baptiste Camille', 'Corot, Jean-Baptiste Camille'),
        ('Coypel, Antoine', 'Coypel, Antoine'),
        ('Coypel, Charles-Antoine', 'Coypel, Charles-Antoine'),
        ('Damoiselet, Florentin', 'Damoiselet, Florentin'),
        ('Daubigny, Charles-François', 'Daubigny, Charles-François'),
        ('David, Jacques-Louis', 'David, Jacques-Louis'),
        ('Decamps, Alexandre-Gabriel', 'Decamps, Alexandre-Gabriel'),
        ('Delacroix, Eugène', 'Delacroix, Eugène'),
        ('Desportes, Alexandre-François', 'Desportes, Alexandre-François'),
        ('Diaz de la Pena, Narcisse', 'Diaz de la Pena, Narcisse'),
        ('Dorigny, Michel', 'Dorigny, Michel'),
        ('Dou, Gerard', 'Dou, Gerard'),
        ('Dubois, Ambroise', 'Dubois, Ambroise'),
        ('Dujardin, Karel', 'Dujardin, Karel'),
        ('Dupré, Jules', 'Dupré, Jules'),
        ('Dyck, Antoon van', 'Dyck, Antoon van'),
        ('Fragonard, Alexandre-Évariste', 'Fragonard, Alexandre-Évariste'),
        ('Fragonard, Jean-Honoré', 'Fragonard, Jean-Honoré'),
        ('France', 'France'),
        ('Gand, Juste de', 'Gand, Juste de'),
        ('Gellée, Claude', 'Gellée, Claude'),
        ('Giovanni Francesco da Rimini', 'Giovanni Francesco da Rimini'),
        ('Greuze, Jean-Baptiste', 'Greuze, Jean-Baptiste'),
        ('Guérin, Pierre-Narcisse', 'Guérin, Pierre-Narcisse'),
        ('Gérard, François Baron', 'Gérard, François Baron'),
        ('Géricault, Théodore', 'Géricault, Théodore'),
        ('Hals, Frans', 'Hals, Frans'),
        ('Heim, François-Joseph', 'Heim, François-Joseph'),
        ('Huet, Paul', 'Huet, Paul'),
        ('Huysum, Jan van', 'Huysum, Jan van'),
        ('Ingres, Jean-Auguste-Dominique', 'Ingres, Jean-Auguste-Dominique'),
        ('Isabey, Eugène', 'Isabey, Eugène'),
        ('Largillière, Nicolas de', 'Largillière, Nicolas de'),
        ('Lawrence, Sir Thomas', 'Lawrence, Sir Thomas'),
        ('Le Brun, Charles', 'Le Brun, Charles'),
        ('Le Sueur, Eustache', 'Le Sueur, Eustache'),
        ('Maes, Nicolaes', 'Maes, Nicolaes'),
        ('Müller, Charles-Louis', 'Müller, Charles-Louis'),
        ('Nattier, Jean-Marc', 'Nattier, Jean-Marc'),
        ('Ostade, Adriaen van', 'Ostade, Adriaen van'),
        ('Oudry, Jean-Baptiste', 'Oudry, Jean-Baptiste'),
        ('Pays-Bas du Sud', 'Pays-Bas du Sud'),
        ('Poelenburgh, Cornelis van', 'Poelenburgh, Cornelis van'),
        ('Prud\'hon, Pierre-Paul','Prud\'hon, Pierre-Paul'),
        ('Rembrandt, Harmensz. van Rijn', 'Rembrandt, Harmensz. van Rijn'),
        ('Rigaud, Hyacinthe', 'Rigaud, Hyacinthe'),
        ('Robert, Hubert', 'Robert, Hubert'),
        ('Roslin, Alexandre', 'Roslin, Alexandre'),
        ('Rousseau, Théodore', 'Rousseau, Théodore'),
        ('Rubens, Petrus Paulus', 'Rubens, Petrus Paulus'),
        ('Scheffer, Ary', 'Scheffer, Ary'),
        ('Teniers, David II', 'Teniers, David II'),
        ('Troy, Jean-François de', 'Troy, Jean-François de'),
        ('Troyon, Constant', 'Troyon, Constant'),
        ('Valenciennes, Pierre de', 'Valenciennes, Pierre de'),
        ('Van Loo, Louis-Michel', 'Van Loo, Louis-Michel'),
        ('Vernet, Claude-Joseph', 'Vernet, Claude-Joseph'),
        ('Wouwerman, Philips', 'Wouwerman, Philips'),
    ]
    art_name = forms.CharField(label='Artwork Name', required=False)
    artists = forms.CharField(label='Artists', widget=forms.Select(choices=PEOPLE))

class rijksInput(forms.Form):
    PEOPLE = [
        ('none', 'none'),
        ('bakhuysen  ludolf', 'bakhuysen  ludolf'),
        ('berchem  nicolaes pietersz', 'berchem  nicolaes pietersz'),
        ('bol  ferdid', 'bol  ferdid'),
        ('borch  gerard ter  ii', 'borch  gerard ter  ii'),
        ('dijk  philip van', 'dijk  philip van'),
        ('dujardin  karel', 'dujardin  karel'),
        ('dyck  anthony van', 'dyck  anthony van'),
        ('flinck  govert', 'flinck  govert'),
        ('geest  wybrand de', 'geest  wybrand de'),
        ('goyen  jan van', 'goyen  jan van'),
        ('halen  arnoud van', 'halen  arnoud van'),
        ('hals  frans', 'hals  frans'),
        ('heemskerck  maarten van', 'heemskerck  maarten van'),
        ('hillegaert  pauwels van', 'hillegaert  pauwels van'),
        ('hodges  charles howard', 'hodges  charles howard'),
        ('hondecoeter  melchior d', 'hondecoeter  melchior d'),
        ('honthorst  gerard van', 'honthorst  gerard van'),
        ('kruseman  cornelis', 'kruseman  cornelis'),
        ('lairesse  gerard de', 'lairesse  gerard de'),
        ('lelie  adriaan de', 'lelie  adriaan de'),
        ('lingelbach  johannes', 'lingelbach  johannes'),
        ('maes  nicolaes', 'maes  nicolaes'),
        ('maris  jacob', 'maris  jacob'),
        ('maris  matthijs', 'maris  matthijs'),
        ('meester van alkmaar', 'meester van alkmaar'),
        ('mierevelt  michiel jansz  van', 'mierevelt  michiel jansz  van'),
        ('musscher  michiel van', 'musscher  michiel van'),
        ('neer  aert van der', 'neer  aert van der'),
        ('netscher  caspar', 'netscher  caspar'),
        ('os  pieter gerardus van', 'os  pieter gerardus van'),
        ('ostade  adriaen van', 'ostade  adriaen van'),
        ('pieneman  jan willem', 'pieneman  jan willem'),
        ('pieneman  nicolaas', 'pieneman  nicolaas'),
        ('poelenburch  cornelis van', 'poelenburch  cornelis van'),
        ('quinkhard  jan maurits', 'quinkhard  jan maurits'),
        ('ravesteyn  jan antonisz  van', 'ravesteyn  jan antonisz  van'),
        ('rembrandt harmensz  van rijn', 'rembrandt harmensz  van rijn'),
        ('ruisdael  jacob isaacksz  van', 'ruisdael  jacob isaacksz  van'),
        ('schalcken  godfried', 'schalcken  godfried'),
        ('scorel  jan van', 'scorel  jan van'),
        ('steen  jan havicksz', 'steen  jan havicksz'),
        ('troost  cornelis', 'troost  cornelis'),
        ('vanmour  jean baptiste', 'vanmour  jean baptiste'),
        ('veen  otto van', 'veen  otto van'),
        ('velde  adriaen van de', 'velde  adriaen van de'),
        ('velde  willem van de  i', 'velde  willem van de  i'),
        ('velde  willem van de  ii', 'velde  willem van de  ii'),
        ('venne  adriaen pietersz  van de', 'venne  adriaen pietersz  van de'),
        ('werff  adriaen van der', 'werff  adriaen van der'),
        ('werff  pieter van der', 'werff  pieter van der'),
        ('wit  jacob de', 'wit  jacob de'),
        ('wouwerman  philips', 'wouwerman  philips'),

    ]
    art_name = forms.CharField(label='Artwork Name', required=False)
    artists = forms.CharField(label='Artists', widget=forms.Select(choices=PEOPLE))


class randomInput(forms.Form):
    PEOPLE = [
        ('none', 'none'),
    ]
    text = forms.CharField(label='Please enter how you feel right now:', required=False)
    artists = forms.CharField(label='Your Color choice', widget=forms.Select(choices=PEOPLE))