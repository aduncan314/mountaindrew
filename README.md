# Mountain Drew
*SITE IN PROGRESS*
## Set up
This is my personal website... don't set it up. I'm not going to stop you, but there are much easier ways to make an
easy website. However, if you're interested, I'll provide an explanation of how I set it up.

### config.json
The file "config.json" must be present at the top level and should not be part of VCS. It contains only information that
is specific to a single instance of the site and could vary from time to time. While not necessary, I like to store these
variables in an unversioned file separate from the `setting.py` file that contains *program* settings that affect the
way that the program works.

Fields:
- engine
- db_name
- admin_user
- admin_password
- db_host

Example:
```
{
  "engine": "django.db.backends.postgresql",
  "db_name": "MyDBName",
  "admin_user": "Me",
  "admin_password": "WickedSecurePassword",
  "db_host": "localhost",
  "secret_key": "DoNotUseThisKey"
}
```

### Database
I am using postgres. psycopg2 needs to be installed before setting up postgres in Django as well as postgres itself.
I'm using Debian and chose:
```
sudo apt-get install postgresql-all
```

```
 pip install psycopg2
 ```