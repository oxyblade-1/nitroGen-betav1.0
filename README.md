# nitro_generator

<script async defer src="https://buttons.github.io/buttons.js">
</script>

![banner_nitro](https://gifimage.net/wp-content/uploads/2017/10/discord-gif-emoji-3.gif)

> Contexte

Salut! Il y assez longtemps j'ai eut l'idée débile de créer un projet
de "Générateur de Nitro". Pour rappel les nitro sont des récompenses sur
Discord qui vous permet d'avoir certains avantage notamment sur la taille des messages plus conséquente, ainsi que la qualitée des stream et tout autres avantages évidement payant.

> Fonctionnement du programme 

Le programme permet de générer des lien avec un structure propre au gift discord, avec un token du gift générer de façon aléatoire jusqu'à tomber sur le compte de quelqu'un qui aurait potentiellement acheté un cadeau et que l'on soit tomber sur son code (ou bien que ce soit le token d'un gift garder dans l'inventaire discord d'un utilisateur). Pour y parvenir j'ai basé mon code sur l'algorithme suivant.

* Démarrage du programme
* Répéter infiniment
 * prendre 16 valeurs aléatoires de la liste
 * envoyer le lien random à l'[API](https://discordapp.com/api/v6/entitlements/gift-codes/)
 * attendre 12s
 * si reconnais le code est utilisé alors -> "code invalid"
 * si l'API affiche "The resource is being rate limited." -> "many request"
 * sinon (dans le cas ou sa marcherai peut-être) envoyer le code en console + écrire un fichier txt à l'emplacement de l'executable.


> Guide d'utilisation

Maintenant que nous avons vu comment fonctionner le code
il est temps que je vous explique le protocole pour executer le programme.

- lancer le programme ```lib.bat``` (permet de lancer tout les lib du programme si vous voulez modifier le code)
- nitroGen.exe (qui n'est pas un virus pour le coup) executera tout sans normalement d'import de lib

et vous obtiendrez alors ceci:

![c1]()

Après cela si par chance et que le programme fonctionne, il devrait apparaître à l'endroit du exe un fichier .txt avec le lien gift (car j'avais prévu que vous ne resterez pas devant la console), Néanmoins...

/!\ Veuillez noter que le programme est en bêta, Il sera modifier surement entre temps, que ce soit d'un point de vue hergonomie, Designe ou encore performant.

> Mise en garde !

/!\ Pour ce qui serai méfiant avec mon programme (ceci n'est pas un virus), Je n'utilise qu'une API et des requête internet avec un délai 

Je ne conseil à personne d'utiliser ce programme pour des fin de commerce (ce qui je pense n'arrivera pas) ou de profit personnel.
Ce programme est juste utile pour savoir comment faire une démarche dans un projet qui au début peut sembler infinissable. En tout cas vous êtes prévenu
Amusez vous bien et n'hésiter pas à me suggérer des options ou du code.

> Feed-Back

N'hésiter pas à me proposer des idées de projet ou autres suggestion de codes, je vous répond dès que je peux ^^.

