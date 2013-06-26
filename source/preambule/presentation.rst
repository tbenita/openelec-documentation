############
Présentation
############

************
Introduction
************

openElec est un logiciel qui permet la gestion des listes électorales (listes
politiques). Il permet de traiter et de gérer facilement les listes
d'émargement (pdf), les cartes d'électeurs (pdf), les procurations, les centres
de vote, les mairies européennes, les étiquettes pour la propagande (pdf), les
listes d'électeurs, les listes annuelles des mouvements, les statistiques, les
envois à l'insee, l'import des inscriptions d'office, les tableaux de fin
d'année, les tableaux j-5, la gestion du découpage des voies.


**********
Historique
**********

Ce logiciel a été développé par la Direction des Systèmes d'Informations et de
Télécommunications de la Mairie d'Arles en 2005 pour son service élections. Ce
logiciel dépend du framework openMairie, qui est un ensemble de bibliothèques
permettant le développement rapide d'applications métiers pour les
collectivités locales.

openElec a remporté le trophée d'or aux trophées du libre 2006 dans le cadre du
concours international organisé par le CETRIL.

Depuis 2006, openElec a évolué pour se plier aux nouvelles règlementations du
code électoral, mais aussi pour améliorer son ergonomie.


***************************
Caractéristiques techniques
***************************

Ce logiciel est développé en PHP (PHP est un langage de scripts libre
principalement utilisé pour être exécuté par un serveur Web) et utilise
une base de données PostgreSQL. openElec dépend de plusieurs composants PHP :

* le framework openMairie,

* l'abstracteur de base de données DB du framework PEAR,

* le générateur de documents pdf FPDF.

Cette interface Web permet donc au logiciel d'être facilement utilisé en local
comme à distance.
