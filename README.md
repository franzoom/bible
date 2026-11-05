# bible

supports de mes cours de Bible.

Les polices utilisées pour le Grec et l'Hébreu sont respectivement SBL Greek et SBL Hebrew.
La police pour le texte "romain" est Libertinus

Lorsque les langues sont en vis-à-vis (hébreu ou grec sur les pages de gauche, français sur les pages de droite), un seul fichier tex contient les deux textes, synchronisés verset par verset grâce au paquet paracol, avec \verset{langue originale}{français}.
Les macros et leur syntaxe sont décrites dans assets/versets.tex, commun à Galates et Ézéchiel :
- chaque ligne dans \verset est une ligne du PDF ;
- les > en début de ligne donnent le niveau d'indentation ;
- un / après les > met toute la ligne en italique.
Les titres (\section*, \subsection*) et les espacements écrits hors de \verset ne s'écrivent qu'une fois, du côté français.

Pour Galates, le texte est dans galates/galates.tex.
Pour Ézéchiel, le texte est dans ezechiel/Ez 33-37.tex, inclus dans ezechiel/Cours sur Ezechiel.tex, qui produit directement le PDF final (introduction, puis hébreu et français en vis-à-vis).

La compilation se fait par LuaLaTeX


Pour définir un environnement LaTeX dans VSCode, installer l'extension LaTeX Workshop, et installer latexindent:
brew install perl
brew install cpanm
cpanm YAML::Tiny
cpanm File::HomeDir