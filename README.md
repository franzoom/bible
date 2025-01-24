# bible

supports de mes cours de Bible.

Les polices utilisées pour le Grec et l'Hébreu sont respectivement SBL Greek et SBL Hebrew.
La police pour le texte "romain" est Libertinus

Lors les langues sont alternées selon les pages (typiquement hébreu à gauche, français à droite), j'utilise deux fichiers tex différents, compilés en deux pdf qui sont assemblés dans le document final par le script ptyhon assemblage.py.
Pour Ezechiel, ce script prend sans les toucher les 4 premières pages du document "TOB", puis ensuite alterne avec le document "Hébreu".
Le script python appelle la librairie pymupd qu'il faut installer.
