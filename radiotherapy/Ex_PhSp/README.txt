Ces deux macros montrent comment utiliser un fichier IAEAphsp comme entrée ET comment sauver les particules dans un second fichier IAEAphsp pour les simulations suivantes...

Première partie
Gate --qt mac/writePHSP.mac

Cette simulation utilise les particules contenues dans le fichier IAEAphsp data/1000p.IAEAphsp.
Les particules traversent un plan durant la simulation (outPhSp) ou leur état est sauvegardé (mais sans perturber la simulation) dans un second fichier IAEAphsp pour une future simulation. C'est grâce à l'actor PhaseSpaceActor.
Ce nouveau fichier est output/myIAEA.IAEAphsp

Cette simulation sauve egalement le meme espace des phases en format ROOT pour pouvoir l'analyser avec le python notebook analysis/phase-space_analysis.ipynb


Deuxième partie
Gate --qt mac/reUse.mac

Les particules stockées dans output/myIAEA.IAEAphsp en première partie sont utilisées comme source. 
Il n'y a pas de sortie dans cet exemple.

A noter les fichiers de type .IAEAphsp sont toujours accompagnés d'un header
.IAEAheader

ROOT : 
La première partie (writePHSP.mac) exporte le fichier d’espaces de phase en format IAEAphsp mais également en format root (output/output-PhS-g.root). ROOT permet par exemple de tracer simplement un spectre énergétique de ces particules. Pour cela dans le terminal taper : 
root –l 
ROOT démarre, taper la commande suivante pour avoir un navigateur. 
 new TBrowser

Dans le menu de gauche, parcourir l’arborescence pour double cliquer sur le fichier output-PhS-g.root. Ensuite ouvrir l’arborescence pour double cliquer sur la « feuille » Ekine. Ceci va tracer le spectre 
