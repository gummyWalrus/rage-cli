# rage-cli
---
# Un CLI python pour relâcher la pression

rage-cli est un outil en ligne de commande consistant en une boucle qui affiche une phrase customisable, 2 variables sont disponibles pour le moment.

Installez en exécutant install.sh en tant que root.
## How to use
En colère contre un logiciel ou une lib ?
Utilisez rage-cli en lui donnant le nom du logiciel en argument et spécifier les variables optionelles.

Options disponibles :
* --user permet d'assigner un nom d'utilisateur à afficher dans la phrase, sinon rage-cli utilise la variable d'environnement "USER"
* --phrase pour assigner la phrase à afficher, formatable selon les instructions ci-dessous. Si cette option n'est pas précisée, "$SOFTWARE qui ne marche pas rend $USER fou !" sera utilisé.

Exemples :
```bash
(utilisateur@pc) $  ragecli "Visual Studio"
output : Visual Studio qui ne marche pas rend utilisateur fou !
(utilisateur@pc) $ ragecli "Visual Studio" --user=utilisatrice
output : Visual Studio qui ne marche pas rend utilisatrice fou !
(utilsateur@pc) $ ragecli "Visual Studio" --phrase="$SOFTWARE rend $USER confus, $USER se blesse dans sa confusion !"
output : Visual Studio rend utilisateur confus, utilisateur se blesse dans sa confusion !

```

### Formater la phrase
Variables: 
* $USER
* $SOFTWARE

La phrase peut être formatée en utilisant les variables, par exemple la variable $USER sera remplacée par le nom d'utilisateur

Ce projet incroyablement polyvalent est open source, faites des pulls requests, proposez des idées en issues, tout ce que vous voulez
