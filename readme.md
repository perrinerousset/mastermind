# Projet Développement Collaboratif : MASTERMIND

###### 

###### Ce projet réalisé en Python permet de jouer au Mastermind sur son PC. Étant communément joué grâce à un plateau de jeu nous proposons ici de le dématérialiser en offrant un suivi de progression. En effet, grâce à la page historique vous pouvez suivre votre progression en observant vos scores précédents. Enfin, comme le jeu matériel, notre application vous propose de stopper puis de reprendre une partie quand vous le voulez.



#### I. Conception générale du projet.



##### A) Description de la vue



Dans le menu 3 boutons sont disponibles :

-Bouton "Jouer" : c'est ici que les utilisateurs peuvent jouer au mastermind

-Bouton "Historique" : Les utilisateurs peuvent découvrir l'historique de leurs parties

-Bouton "Règles du jeu" : Les utilisateurs peuvent lire les règles appliquées à ce jeu.



*(j'ai mit des tirets mais promis ce n'est pas chatgpt)*





##### B) Fonctionnement derrière la vue



Notre classe VuePrincipale sert de squelette à notre vue : elle divise la fenêtre en deux : une zone\_laterale pour le menu (qui ne change jamais) et une zone\_centrale qui est un cadre vide. Ainsi à chaque fois que nous appuyons sur un bouton la zone\_centrale est remplie.

Le fonctionnement du remplissage est le suivant : Le Contrôleur appelle la méthode nettoyer\_zone\_centrale() de la vue principale ( Nous supprimons tout ce qui se trouve dans le cadre central). Le Contrôleur crée ensuite une nouvelle instance et lui donne self.vue\_principale.zone\_centrale comme parent.



##### C) Jouer au mastermind 



La prise en main du jeu est très facile. Il suffit de changer les couleurs en appuyant sur les ronds (initialement bleu) puis d'appuyer sur le bouton "valider" à droite de votre ligne pour suggérer une proposition. Une fois le bouton "valider" un chiffre suivit d'un pion rouge indiquera le nombre de ronds de couleurs de la bonne couleur ET bien placés, ainsi qu'un chiffre suivit d'un pion blanc indiquera le nombre de ronds de couleurs de la bonne couleur MAIS mal placés. 

Notons que l'ordre des couleurs lors de l'appui est le suivant : Bleu, vert, jaune, orange, rouge, violet pour un total de six couleurs. La boucle de couleur recommence dès que vous appuyez sur le violet : Rouge, violet, bleu, vert…



Pour plus de renseignement sur les règles du jeu, il suffit de se rendre sur notre page dédiée en cliquant sur le bouton "Règles du jeu". 



##### D) Gestion du score 



Le score peut être visualisé lorsque que vous perdez (score =0) ou gagnez. Il est également affiché dans l'onglet historique. 

Si le joueur trouve en 1 tour il gagne 1200 points. Si le joueur trouve en 12 tours il gagne 100 points. Le calcul est donc le suivant : score = 1200 -100\*nbr de tentatives







#### II. Lancer l'application



##### A) Avec Python



Pour lancer l'application il suffit de taper dans votre console la consigne suivante :

python main.py



##### B) Avec pip install-e .



Notre projet Mastermind peut être installé à l'aide de la commande pip install-e . Cette dernière télécharge les dépendances nécessaires à l'exécution du programme. Pour ce qui est de la majorité des imports de la partie mvc, ils sont disponible avec l'installation de python.



#### III. Choix sur la gestion des fonctionnalités



##### A) Gestion de la fermeture puis réouverture de l’application :



**Différents scénarios :**



Ouvrir l’application -> lancer une partie -> valider quelques tentatives -> fermer l’application -> rouvrir l’application -> Reprise là où l’utilisateur était.



Ouvrir l’application -> lancer une partie -> gagner/perdre -> fermer l’application -> rouvrir l’application -> affichage d’une nouvelle partie (0 tentatives validées), l’ancienne partie gagnée/ perdue est enregistrée et s’affiche dans l’historique



###### B) Gestion « nouvelle partie » :



**Différents scénarios :**



L’utilisateur a gagné/perdu -> clique sur nouvelle partie -> une nouvelle partie se lance -> ancienne partie enregistrée et affichée dans l’historique



L’utilisateur a fait n<12 tentatives infructueuses -> clique sur nouvelle partie -> une nouvelle partie se lance -> l’ancienne partie est enregistrée et affichée dans l’historique comme un ECHEC avec n/12 tentatives.



#### IV. Commentaires



##### A) Lint



Nous n’avons pas réussi à valider le test lint pendant de nombreux jours: le test ne réussissait pas à passer le « Analysing the code with pylint » et cela était dû à notre note du code qui était inférieur à 10. Cette note était dûe au manque de Docstring pour toutes les fonctions. Nous n’avions pas le temps de rajouter un Docstring pour toutes les fonctions et trouvions cela inutile pour la plus part. Nous avons donc décidé de réajuster la note seuil de validation à 8/10.

