Zadanie 1:
1. Zainstaluj dokera
2. utwórz  plik docker-compose.yml który będzie zarządzał serwisami
	1. Apache Spark (PySpark)
	2. MySQL

- Spark powinien widzieć bazę MySQL
- Spark powinien mieć dostęp do lokalnego systemu plików w celu załadowania kodu/joba
	
Plik 'docker-compose.yml' wypchnij do swojego repozytorium.

Zadanie 2:
Napisz skrypt w pythonie (uruchamiany jako Sparkowy job), który:
1. pobierze plik 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv' 
2. za pomocą PySparka wykonaj "analizę"
	1. jaki procent dzieci (dziecko < 18 lat) przeżył katastrofę
	2. jaki procent dorosłych do 40 roku życia przeżył katastrofę
	3. jaki procent dorosłych do 40 roku życia przeżył katastrofę z podziałem na płeć
	4. jaki procent dorosłych powyżej 40 roku życia przeżył katastrofę
	5. jaki procent dorosłych powyżej 40 roku życia przeżył katastrofę z podziałem na płeć
	6. jaki procent przeżywalności był w danej klasie z podziałem na płeć
3. zapisze wyniki powyższej analizy do bazy MySQL
4. Napisz skrypt SQLowy, który utworzy tabele do zapisania wyników powyższej analizy

Plik PYTHONowy i SQLowy wypchnij do swojego repozytorium.

Zadanie 3 - dla chętnych:
Przy użyciu Makefile'a napisz skrypt automatyzujący zadania:
1. startowanie i zatrzymywanie wspomnianych usług na Dockerze
2. uruchamianie joba z analizą na Sparku (submit)
3. tworzący tabele do zapisania wyników analizy w bazie MySQL

Plik Makefile wypchnij do swojego repozytorium.

