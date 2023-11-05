## User Guide

Bienvenue dans notre guide ! Celui-ci  vous servira à utiliser notre Dashboard sur votre propre machine.

Avant de commencer, faites gaffe à ce que vous ayez bien Python de téléchargé sur votre machine car le projet ne contient que de ça !

**Déploiement du travail**

Dans un premier temps, vous allez cloner le dépôt Git du projet dans votre terminal à l'aide de la commande suivante :
``git clone adresse_publique_de_votre_projet``

Puis, toujours dans le terminal, vous allez installer les dépendances nécessaires (packages) au projet avec la commande suivante :
``python -m pip install -r requirements.txt``

Maintenant que c'est fait vous allez rentrer la commande suivante dans le terminal afin que le projet avec le dashboard se lance :
``python main.py``

Maintenant que c'est fait, vous n'avez plus qu'à faire *ctrl + click* sur le lien affiché dans le terminal et le Dashboard sera à vous !

**Utilisation du Dashboard**

Bienvenue dans le Sustainable Development Dashboard !
Vous y trouverez 4 graphiques aussi passionnant les uns que les autres.
Voici ce que chacun d'entre eux proposent :

*Graphique 1 : La carte du monde*
Dans ce premier graphique, vous verrez une coloration des pays du monde en fonction de leur score en développement durable. Plus la couleur est claire, plus le pays en question favorise le développement durable. Vous pouvez voir l'évolution au cours du temps en appuyant sur le signe play au niveau de l'échelle temporelle ou vous pouvez sélectionner l'année à étudier avec le curseur.

*Graphique 2 : L'histogramme*
Dand ce second graphique, vous pourrez observer un histogramme en fonction du temps du score en développement durable des pays du monde. Afin d'affiner votre observation, vous avez la possibilité de sélectionner le pays à étudier avec le menu déroulant. Plus la barre est haute, plus le développement durable est appliqué.

*Graphique 3 : La pauvreté et la faim*
Dans ce troisième et avant dernier graphique, nous nous concentrons sur les données concernant la pauvreté et la faim. En effet, vous allez observer 5 nuages de points (1 par continent) qui lient la pauvreté à la famine. Plus les points sont haut, moins il y a de famine dans le pays en question. Plus les points se situent vers la droite, moins il y a de pauvreté. Si il y a plus de famine que de pauvreté dans le pays en question, les points seront bleus. Au contraire, s'il y a plus de pauvreté que de famine, les points seront rouges.

*Graphique 4 : Étude de la totalité des critères*
Dans ce dernier graphique, nous allons pouvoir étudier l'ensemble des critères, selon l'année, en fonction du score de développement durable. En effet, vous ne pouvez choisir pas une mais DEUX variables ! Grâce à un menu déroulant, choisissez l'indicateur que vous souhaitez étudier. Vous pouvez également sélectionner l'année à observer avec le slider. Ainsi, vous aurez 5 nuages de points (1 par continent) montrant l'indicateur en question en fonction du score de développement durable. Plus le point est haut, plus l'indicateur en question est élevé.

## Analyses

**Introduction**

Maintenant que vous connaissez notre Dashbord comme votre poche, place aux principales conclusions extraites des données !
Mais avant ça nous allons clarifier quelques points concernant notre base de donnée.
En effet, notre base de données regroupe des observations concernant les Objectifs Développement Durable des pays du monde entre 2000 et 2022. Ceci met donc en lumière le progrès (ou non) de chacun des pays. Ces objectifs représentent plusieurs critères comme l'égalité des genres, l'action climatique, la lutte contre la famine, la qualité de l'éducation, la consommation responsable... Au cours de notre analyse, nous nous concentrerons particulièrement sur notre Score de l'Indice de Développement Durable (sdg_index_score) car cet indice rassemble les informartions de tous les autres objectifs, un peu comme une moyenne de ceux-ci ! De manière générale, plus un objectif a un score élevé, plus le pays en question est développé dans ce dernier.
Désormais, nous pouvons analyser chacun des graphiques !

**Graphique 1**

*Vue statique :* D'un point de statique, nous remarquons que les pays les moins développés se situent dans l'hémisphère sud. Plus précisément, ils se trouvent en Afrique, en Amérique Centrale et en Asie du Sud. En revanche, nous remarquons que 2 pays se démarquent : la Suède et la Finlande qui ont une couleur bien plus claire que les autres pays (et donc un Objectif Développement Durable mieux accompli).

*Vue dynamique :* D'un point de vue dynamique Nous remarquons que l'ensemble des pays évoluent de manière positive. Ceci montre donc que l'Objectif Développement Durable avance pas au pas au fin du temps et que nous sommes sur une bonne lancée.
Avec une observation plus recherchée, nous remarquons qu'il y a des pays qui évoluent plus vite que les autres comme le Mali, la Mauritanie et l'Inde, bien que leurs indices restent encore plutôt bas.
Néanmoins, il y a tout de même des pays qui n'évoluent quasiment voir pas du tout comme la Papouasie Nouvelle Guinée, le Soudan du sud et la République Centrafricaine. Nous pouvons également observer que l'Amérique du nord et de manière générale la partie du monde qui évolue le moins vite, bien que l'indice soit plutot élevé.

*Conclusion :* Dans ce premier graphique, nous constatons que les pays de l'hémisphère nord possèdent un Objectif de Développement Durable bien plus accompli, mais qu'en termes d'évolution, l'hémisphère sud progresse plus rapidement.

**Graphique 2**

*Intérêt :* Ce second graphique illustre le premier de façon plus précise à l'aide d'un histogramme. En effet, il nous permet de sélectionner un pays et d'observer son score en Objectif Développement Durable au fil du temps. Prenons l'exemple de la France : nous constatons que le score augmente de manière relativement constante au cours des années.

*Lien avec le premier graphique :* En reprenant les exemples du premier graphique, nous pouvons constater que la Papouasie-Nouvelle-Guinée ne présente pratiquement aucune évolution au fil du temps. En revanche, nous remarquons que le Mali possède un histogramme en croissance, ce qui témoigne de l'amélioration du pays en matière d'Objectif Développement Durable.

*Analyse des variations :* Toutes les évolutions ne sont pas toujours constantes, comme nous l'avons vu précédemment. Prenons l'exemple de l'Afghanistan : entre 2014 et 2018, le pays affiche un score en Objectif Développement Durable en nette augmentation par rapport au reste de la période. Cette augmentation peut s'expliquer par un changement majeur survenu dans le pays. En effectuant quelques recherches, nous découvrons qu'il y a eu de nouvelles élections présidentielles en 2014. Cet événement a donc contribué aux progrès réalisés dans divers domaines, ce qui est reflété dans cet histogramme. En revanche, nous observons également une baisse de l'indice en 2021, expliquée par le retour des talibans au pouvoir cette année-là.

*Conclusion :* En résumé, le second graphique offre une vue détaillée de l'évolution des pays au fil du temps en terme de Score de Développement Durable. Comparé au premier graphique, il apporte une précision supplémentaire en permettant de déterminer si cette évolution s'est déroulée de manière constante ou non, mettant ainsi en évidence des liens avec des événements majeurs susceptibles d'avoir influencé la trajectoire d'un pays en matière d'Objectif de Développement Durable.

**Graphique 3**

*Vue statique :* Dans ce graphique, nous observons un nuage de points par continent comparant la pauvreté à la faim dans les pays. On peut séparer ces données en 2 où nous avons d'un côté l'Amérique, l'Océanie l'Asie et l'Europe où le problème est largement plus la famine que la pauvreté, notamment en Europe où la totalité des pays ont un indice de famine plus élevé que celui de pauvreté. En revanche, nous pouvons voir dans un second temps que l'Afrique est le seul continent où les pays ont un indice de pauvreté plus élevé que celui des pays du reste du monde.

*Vue dynamique :* Avec la vue dynamique, nous observons qu'avec le temps, les points ont tendance à se rapprocher. En effet, ils se regroupent de plus en plus vers la partie supérieure droite ce qui veut dire que les pays en question gèrent de mieux en mieux les problèmes de pauvreté et de famine. Ceci est particulièrement flagrant sur le nuage de points de l'Asie. En effet, on remarque qu'entre 2000 et 2009, les points montent ce qui veut dire qu'il y a de moins en moins de famine. Puis, entre 2010 et 2022, les points se "tassent" vers la droite ce qui veut dire que la pauvreté s'atténue à son tour. On remarque également que plus les pays d'Asie évoluent, plus les points deviennent bleu, ce qui veut dire que la pauvreté diminue plus vite que la famine. En revanche, on remarque pour la Papouasie Nouvelle Guinée par exemple que le pays ne s'appauvrie pas spécialement mais que la famine accroît.

*Conclusion :* Pour conclure sur ce graphique, nous remarquons que la plupart des pays ont un taux de famine et de pauvreté qui diminue au cours du temps, notamment en Asie. On remarque également que, moins le pays est développé, plus la famine est un problème plus préoccupant que la pauvreté, comme nous le voyons en Afrique. Ainsi, la réduction de la pauvreté progresse plus rapidement que celle de la famine.

## Developper Guide