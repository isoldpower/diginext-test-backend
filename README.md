## Short user manual

---

### In order to start project:
0) if using _**JetBrains Pycharm**_, set `src` folder as source folder
```text
1. right click > Mark Directory as > Sources Root
2. refresh python interpreter (bottom right corner) 
```
1) connect to virtual environment
```shell
source .venv/bin/activate
```
2) upgrade pip
```shell
pip install --upgrade pip
```
3) install dependencies
```shell
pip install -r requirements.txt
```
4) upgrade dependencies
```python
import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
```
5) set up PostgresSQL database with all granted privileges ([Manual](https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL.htm))
6) make initial migrations, and run them
```shell
python src/manage.py makemigrations
python src/manage.py migrate
```
---
### In order to provide environmental variables:
1) Create `.env` file
2) Paste template:
```text
SECRET_KEY=[key]
DEBUG=[True/False]
DATABASE_NAME=[db_name]
DATABASE_USER=[db_root_user]
DATABASE_PASSWORD=[db_password]
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
3) Set variables. Change defaults if needed

---

### Hints
#### Starting an app
1) navigate to src folder
```shell
cd src
```
2) start an app
```shell
python manage.py startapp [name]
```
3) in `apps.[name].apps.Config` config, add `apps.` prefix to app name
4) add app to `src.config.settings.py` `INSTALLED_APPS`
