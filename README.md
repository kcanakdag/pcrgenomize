# pcrgenomize

Proje için backend django ve djangorestframework, frontend için vue.js 3 kullandım. Dinamik tabloyu BootstrapVue ile yaptım. Proje, docker ile build edildikten sonra **http://127.0.0.1:8000/** adresinde çalışır halde. Server-side pagination kullandım.

Rest api call şu adrese yapılıyor: **http://127.0.0.1:8000/PCRendpoint/?page=1&pagesize=10**

Repoyu indirdikten sonra aşağıdaki komutla direkt çalıştırabilirsiniz.

```
docker-compose up --build
```

