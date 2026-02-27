JSONPlaceholder API Tesztelés
Ez a projekt a JSONPlaceholder REST API automatizált tesztelését valósítja meg Python nyelven.

Projekt felépítése
* clients/: Az API hívásokat kezelő modulok (Base, Comments, Post).

* tests/: A tényleges tesztesetek helye.

* conftest.py: Tesztkonfigurációk és fixture-ök.

* riport.html: A futtatási eredmények vizuális jelentése.

Tesztelt funkciók
* Lekérés: Egyedi bejegyzések és hozzászólások ellenőrzése (GET).

* Létrehozás: Új posztok beküldésének tesztelése (POST).

* Módosítás: Meglévő adatok szerkesztésének validálása (PUT/PATCH).

Futtatás
Használd a pytest --html=riport.html --self-contained-html parancsot a terminálban a tesztek indításához.
