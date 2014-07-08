# comment créer un fichier .txt et y ajouter whatever you want.
f = open('score.txt','a')
h_score=("""Nom: Alexandre Erich Sébastien Georges
Ecole: Institution Saint-Louis de Gonzague
Email: erichaitian97@gmail.com""")
f.write(h_score)
f.close()