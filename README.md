# Framgia Training

Project training how to use django

## Installation

* [Environment](http://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu)

## Usage

1. Create virtualenv
	* mkvirtualenv name_virtualenv
	* workon name_virtualenv
2. Install environment with requirements.txt
	* pip install requirements.txt
3. Migrate database
	* python manage.py migrate
4. Create superuser
	* python manage.py createsuperuser (user login admin)
5. Run
	* python manage.py runserver [port] (default: 8000)

## Task Admin
	1. Login
		1. Signin, Signout
	2. Profile
		1. Change profile
		2. Change password
	3. User
		1. List all user register
		2. Delete user
		3. View detail user
		4. View course, subject, task user register
	4. Course
		1. List all course
		2. View detail course
		3. Add, edit, delete course
		4. View subject detail in course
		5. View all trainees in course
		6. Can assign trainee to course
		7. Can finish course
	5. Subject
		1. List all subject
		2. View detail subject
		3. Add, edit, detele subject
		4. Can assign trainee to subject
		5. Can finish subject
	6. Task
		1. List all task
		2. View detail task
		3. Can assign trainee to task

## Task User
	Waiting


## License

Framgia VN
