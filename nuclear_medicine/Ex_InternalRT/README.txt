Ce dossier contient un exercice pour simuler une radiotherapie interne vectorisee.

Objectifs:

- utiliser un CT comme geometrie patient
- utiliser un SPECT comme carte d'activitee
- simuler un radioisotope

Exercice:

1 - ecrire la macro patient.mac pour definir la geometrie voxelisee du patient a partir de:
- data/patient_CT.mhd
- data/Schneider2000DensitiesTable.txt
- data/Schneider2000MaterialsTable.txt
aide en ligne: http://wiki.opengatecollaboration.org/index.php/Users_Guide:Voxelized_Source_and_Phantom

2 - ecrire la macro source.mac pour definir la source voxelisee a partir de:
- data/patient_SPECT.mhd
et definir la source avec ion_source de GATE.
aide en ligne: http://wiki.opengatecollaboration.org/index.php/Users_Guide:Source#Defining_the_energy

3 - inspecter la macro mac/main.mac pour en comprendre les détails.

4 - executer la simulation avec 1000 particules.

Gate mac/main.mac

-> les donnees de sortie sont crees dans le dossier output.

5 - analyser les resultats avec le python notebook analysis/dose_map_analysis.ipynb:

jupyter notebook

puis dans le navigateur internet ouvrir le fichier (vert) dose_map_analysis.ipynb

utiliser shift+entree pour executer les cellules.

6 - augmenter le nombre de particules
