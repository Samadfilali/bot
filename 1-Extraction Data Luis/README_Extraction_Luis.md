# Frames Dataset Evaluation

Le référentiel contient le code utilisé pour produire l'évaluation du modèle Frametracking
in [A Frame Tracking Model for Memory-Enhanced Dialogue Systems](https://arxiv.org/abs/1706.01690) 
by Hannes Schulz, Jeremie Zumer, Layla El Asri, and Shikhar Sharma.


## Installation

Vous devez d'abord télécharger le jeu de données Maluuba Frames ([Link](https://www.microsoft.com/en-us/research/project/frames-dataset/#!download), [Backup Link](https://msropendata.com/datasets/1cc496ec-aaff-4576-b4bc-4a65798fa907)).

Cloner le répértoire avec 
```bash
$ git clone https://github.com/Maluuba/frames
```
puis intaller les modules et leurs indépendances en utilisant :

```bash
$ cd frames
$ pip install -U -e .
```

Si vous êtes dans un environnement virtuel ou dans un environnement conda, vous pouvez omettre `-U`.


## Utilisation

Changer dans le fichier preparation_data_luis.py le chemin d'accès à votre datset frame.json, ensuite lancer : python preparation_data_luis.py.
Ce dernier va générer un fichier "FlightBooking.LU" dans un format pris en charge par LUIS. Il suffit de le télécharger sur la plate-forme LUIS pour commencer l'entrainement de votre modèle.