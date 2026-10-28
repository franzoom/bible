# bible

supports de mes cours de Bible.

Les polices utilisées pour le Grec et l'Hébreu sont respectivement SBL Greek et SBL Hebrew.
La police pour le texte "romain" est Libertinus

Lors les langues sont alternées selon les pages (typiquement hébreu à gauche, français à droite), j'utilise deux fichiers tex différents, compilés en deux pdf qui sont assemblés dans le document final par le script ptyhon assemblage.py.
Pour Ezechiel, ce script prend sans les toucher les 4 premières pages du document "TOB", puis ensuite alterne avec le document "Hébreu".
Le script python appelle la librairie pymupdf qu'il faut installer dans un environnement virtuel à la racine du dépôt :
python3 -m venv .venv && .venv/bin/pip install pymupdf
Il se lance à la main, depuis le dossier ezechiel : ../.venv/bin/python assemblage.py

Pour Galates, un seul fichier (galates/galates.tex) contient le grec et la TOB, grâce au paquet paracol :
le grec est sur les pages de gauche, la TOB sur les pages de droite, synchronisés verset par verset avec \verset{grec}{français}.
Les titres (\section*, \subsection*) écrits hors de \verset n'apparaissent que du côté français.

La compilation se fait par LuaLaTeX


Pour définir un environnement LaTeX dans VSCode, installer l'extension LaTeX Workshop, et installer latexindent:
brew install perl
brew install cpanm
cpanm YAML::Tiny
cpanm File::HomeDir