BGG Scraper
===========

Outil de récupération ("Scraper") pour récupérer les données de BGG et les mettre sous forme de base de données
relationnelle.

Utilisation
-----------

```sh
bgg-scraper [-h]
          (-m GAME_ID [MAX_GAME_ID ...] | -i GAME_ID [GAME_ID ...] | -r)
          [-fr] [-d] [-dsql] [-v]
```

Paramètres :
```sh
  -h, --help            Affiche l'aide
  -m GAME_ID [MAX_GAME_ID], --max-game-id MAX_GAME_ID [MAX_GAME_ID]
                        Récupère tous les jeux jusqu'à GAME_ID (Il y en a environ 350000) ou entre GAME_ID et MAX_GAME_ID
  -i GAME_ID [GAME_ID ...], --game-id GAME_ID [GAME_ID ...]
                        Récupère uniquement GAME_ID (ou tous les GAME_ID indiqués)
  -r, --recover         Reprend le traitement à partir des données sauvegardées (utile en cas de déconnexion)
  -fr                   Utilise le schéma français pour la BDD
  -d                    Débogage (n'enregistre pas dans la base)
  -dsql                 Débogage SQL
  -v                    Mode verbeux
```

Exemples
--------

Pour récupérer les ~100 premiers jeux : ```bgg-scraper -m 100 -fr -v```
Pour récupérer au moins un de chaque type d'objet : ```bgg-scraper -i 40692 156497 293300 219880 47163 182880 195673 -fr```

Schéma
------

Un schéma de la base est disponible dans le dossier schema au format [MoCoDo](https://www.mocodo.net/) (/schema/BGG_SR.mocodo)
