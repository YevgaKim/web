After you downloading this project follow the rules below
1. Create your .env(it's must have SECRET_KEY, DEBUG, DATABASE_URL, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_NAME, POSTGRES_HOST, POSTGRES_PORT)
2. Next step is build and run containers(in main folder run the command(docker-compose up -d))
3. After everything will be completed and containers are running - you must run these 3 commands in "anitiming's"(container) terminal
   - python manage.py makemigrations
   - python manage.py migrate
   - python insert.py
4. Well done. Here is the url to visit the site - http://localhost:80
