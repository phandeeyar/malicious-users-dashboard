## Phandeeyar Dashboard

### Local ENV setup

- Make sure `docker` and `docker-compose` are installed
- Make sure that you have the user `appuser` and group `appuser` defined on your system:

```
/etc/passwd: appuser:x:1000:1000:App User:/home/appuser:/bin/bash
/etc/group:  appuser:x:1000:appuser,<your user id>
```

- Create a `.env` file (it is already ignored in `.gitignore`)
- Define DEBUG=1/0 depending on what you want, this will be used to set Django DEBUG env var

### Development & Deployment

- Run `docker-compose up`
- This will start the containers and the server on localhost:8080
- To allow access from another IP, add that IP to `ALLOWED_HOSTS` in `settings.py`
- ### For production deployments you will want `DEBUG` to be set to **0**
- `/data/phandeeyar/` gets mounted to Docker as a Volume and the database uses this volume for stroage

### Project Organisation

- Everything is organised in the typical Django fashion
- The database models are in `core/models.py`
- All the front-end views are in `frontend/views.py`
- The front-end for the dashboard comes from `frontend/templates/index.html`
- The JavaScript for the charts is inside: `dashboard/static/vendor/sb-admin-2/js/demo`

### Adding to database

- In a new shell, run `docker-compose run web bash` to get inside the Docker container
- There are a bunch of available commands to add to database
	1. `add_data_window`
	2. `add_lexicon_data`
	3. `add_malicious_users`
	4. `add_target_group_data`
	5. `add_wordcloud_data`
- Currently, the file paths inside these commands are static (open core/management/commands) to see the commands
- To run a command type `python manage.py migrate [command_name]` for example `python manage.py migrate add_data_window`

## Add new user
- To add new user, inside the shell from earlier, run `python manage.py createsuperuser`
- This will prompt for username/email/password details.

#### Gotchas:

- Ensure that the headers of the csv files match that of the management commands
- Change the file paths to insert data from multiple files
