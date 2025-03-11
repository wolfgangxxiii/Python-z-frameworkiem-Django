📝 Blog Django Szymon Blawat

Projekt zaliczeniowy z przedmiotu Język Python - Frameworki.Autor: Szymon Piotr Bławat

📋 Opis projektu

Aplikacja webowa stworzona przy użyciu frameworka Django.Celem projektu jest wykonanie w pełni funkcjonalnego bloga z możliwością:

Przeglądania wpisów,

Dodawania i edytowania postów,

Polubienia wpisów,

Komentowania wpisów,

Wyświetlania najnowszych i najpopularniejszych postów,

Dostępu do API w Django Rest Framework.

Interfejs użytkownika został zaprojektowany w ciemnej stylistyce minimalistycznej, inspirowanej środowiskiem Manjaro GNOME, z akcentami zieleni oraz emotikonami.

✅ Funkcjonalności

📄 Lista postów i szczegóły posta.

📝 Dodawanie i edycja wpisów (dla zalogowanych użytkowników).

👍 Polubienia postów.

💬 Komentarze do postów.

🔥 Sekcja najnowszych i najpopularniejszych postów.

🔧 REST API - pobieranie postów w formacie JSON.

🎨 Profesjonalny i responsywny interfejs (dark mode, Bootstrap 5).

⚙️ Technologie

Python 3.11+

Django 5.1.7

Django Rest Framework

Bootstrap 5

HTML5 / CSS3

SQLite3 (domyślna baza danych)

🚀 Jak uruchomić projekt lokalnie?

Sklonuj repozytorium:

git clone https://github.com/wolfgangxxiii/Python-z-frameworkiem-Django.git
cd Python-z-frameworkiem-Django

Stwórz i aktywuj środowisko wirtualne:

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux / MacOS

Zainstaluj wymagane biblioteki:

pip install -r requirements.txt

Wykonaj migracje bazy danych:

python manage.py makemigrations
python manage.py migrate

Uruchom serwer developerski:

python manage.py runserver

Otwórz przeglądarkę i przejdź do:

http://127.0.0.1:8000/

🛠️ Podstawowe Endpoints

Strona główna:http://127.0.0.1:8000/

Panel administracyjny:http://127.0.0.1:8000/admin_szymonblawat/

API REST (lista postów w JSON):http://127.0.0.1:8000/api/posts/

👤 Autor

Szymon Piotr Bławat 
Kierunek: Informatyka

✅ Status projektu

✅ Ukończony✅ Przetestowany lokalnie⬛️ Do ewentualnej rozbudowy o system rejestracji/logowania użytkowników i autoryzację API.

📄 Licencja

Projekt wykonany w ramach zaliczenia przedmiotu Język Python - Frameworki na potrzeby edukacyjne.

