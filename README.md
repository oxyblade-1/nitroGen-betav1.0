# nitro_generator

![banner_nitro](https://gifimage.net/wp-content/uploads/2017/10/discord-gif-emoji-3.gif)

> Contexte

Salut à tous ceux à qui cela peux interressé j'ai créer
ce projet à unique but de savoir si il été réellement possible de
faire une sorte de générateur "nitro". Actuellement je n'est toujours pas
la réponse.

> Difficultées rencontrée

Durant ce projet, j'ai fait de nombreuses recherche qui ont aboutit au résultat actuelle (pas forcement incroyable).
En ce qui concerne les difficulté l'une des grande difficultée de ce projet et de demander plusieurs requêtes à un serveur sans se faire Ban IP
J'ai donc trouvé 3 différents moyens:

* Envoyer des requêtes chaques secondes et dès que le message "change IP" apparaît je dois changer d'ip Manuellement avec un VPN (pas ouf, ce qui a fait que j'ai changer mon programme assez rapidement)
* Le second programme pour les envois de paquet et beaucoup moins optimiser mais est celui qui je pense est le plus sûre des 3, Il consiste a utiliser un délai entre chaque requêtes, c'est à dire que le délai pour chaque test est de 12s. C'est donc plus safe mais plus long...
* Le dernier choix qui je pense à mit pour moi fin à ce projet, est l'option d'ajout de proxy (autrement dit, de serveur qui vont permettre le changement d'ip de l'utilisateur pour chaque requête). Mais le problème avec cette idée c'est que de base les proxy son payant et que ce qui été ait proposer "gratuitement" ne fonctionner pas. Et vu que j'avais quasiment tout fini je ne voulais pas me relancer dans un nouveau projet donc je me suis contenter du résultat actuelle

> Guide d'utilisation

Utiliser l'executable du programme (fait en python)
Et pour ce qui auraient peur du programme exe je vous ai mis le fichier py (qui doit être installer avec les assets)
alors que le fichier exe n'a besoin de rien d'autre !
en cas de problème vous pouvez directement installer les lib avec le fichier "lib.bat"
Lorsque vous démarrer le programme vous aller lancer un terminale (pour des questions de simpliciter) celui ci va vous demander un nombre de nitro à trouver (metter 1 car sa ne sert à rien de lui en demander plus, ce n'est même pas sur qui les trouvera !) puis après cela il va lancer le programme vous verrez les logs dans la consoles puis après il faut attendre jusqu'à ce qu'il trouve un code, et si par chane il en trouve un il vous fera un fichier txt avec le code dedans (car oui dans la console je me doute q'avec le nombre de log vous ne risquez pas de retrouver le code).

> Fonctionnement du programme 

* Démarrage du programme
* Répéter infiniment
 * prendre 16 valeurs aléatoires de la liste
 * envoyer le lien random à l'[API](https://discordapp.com/api/v6/entitlements/gift-codes/)
 * attendre 12s
 * si reconnais le code est utilisé alors -> "code invalid"
 * si l'API affiche "The resource is being rate limited." -> "many request"
 * sinon (dans le cas ou sa marcherai peut-être) envoyer le code en console + écrire un fichier txt à l'emplacement de l'executable.
 

> Mise en garde !

/!\ Pour ce qui serai méfiant avec mon programme (ceci n'est pas un virus), Je n'utilise qu'une API et des requête internet avec un délai 

Je ne conseil à personne d'utiliser ce programme pour des fin de commerce (cequi je pense n'arrivera pas) ou de profit personnel.
Ce programme est juste utile pour savoir comment faire une démarche dans un projet qui au début peut sembler infinissable. En tout cas vous êtes prévenu
Amusez vous bien et n'hésiter pas à me suggérer des options ou du code.

> Feed-Back

N'hésiter pas à me proposer des idées de projet ou autres suggestion de codes, je vous répond dès que je peux ^^.

