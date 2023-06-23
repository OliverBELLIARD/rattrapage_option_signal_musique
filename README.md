# Rattrapage Option Signal Musique
*Rattrapage d'OPTION : Signal Musique*

## Comment lancer le code
Le programme en Python est prévu pour être lancé sur un environnement [Replit](https://replit.com/@OliverBELLIARD/PhaserResitExamMusicSignalOPTION#phaser.py) pour simplifier la mise en place.  
Cependant, il est en théorie possible de faire fonctionner le code en local avec un environnement Python >=3.10. Les packages necessaires sont spécifiés sur le fichier ```requirements.txt```.

## Comment spécifier le fichier
Pour spécifier le fichier à traiter, il faut remplacer le contenu de la variable ```input_file``` par le nom du fichier avec son format. Par exemple : ```input_file = 'Clean-Electric-Guitar-Loop.wav'```.  
Le fichier doit être au format .wav, pour cela, une version est déjà fournie dans le projet avec l'original pour comparer si besoin.

## Les paramètres
Les paramètres de l'effet peuvent être modifiés à travers les variables ```f``` pour la vitesse de l'effet et de ```d``` qui va définir l'intensité de l'effet. Un autre paramètre```depth_control``` permet de contrôler la profondeur de l'effet. Pour plus de détails sur ce dernier, se référer aux [ressources fournies](https://www.dsprelated.com/freebooks/pasp/Virtual_Analog_Example_Phasing.html#sec:allpassphasing).
