# Task Pilot - API

#### DEPLOYED BACKEND API RENDER [LINK](https://task-pilot-api-323c9bc2bc87.herokuapp.com/) 
#### DEPLOYED FRONTEND RENDER [LINK - LIVE SITE](https://task-pilot-e84398da7501.herokuapp.com/)
#### DEPLOYED FRONTEND [REPOSITORY](https://github.com/Blaize-Egelhof/task-pilot)

## Table of Contents
+ [User Stories](#user-stories "User Stories")
+ [Database](#database "Database")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## User Stories:
All User Stories have been documented in their own file, the link for which can be found [HERE](https://github.com/users/Blaize-Egelhof/task-pilot-api/static/userstories.md).

I have included links to the [GitHub Issues](https://github.com/Blaize-Egelhof/task-pilot-api/issues) for this project, as well as the [KANBAN board](https://github.com/users/Blaize-Egelhof/projects/3).

## Database:

- Note: This database model represents the final version of the application. Due to time constraints, I haven't implemented the following apps:
  - Inbox app
  - User Messages app

These apps were designed to manage a large audience, with the Inbox app acting like a regular inbox for users to receive notifications and task invites, enhancing user control and organization. The User Messages app works in conjunction with the Inbox app to handle invites and notifications. These features will be implemented in a future version of the software.


![SQL Database model](/static/images/app_schema_all_models.png)

## Testing:

### Manual Testing:

| **ID** | **CATEGORY**         | **TEST**                | **ACTION**                           | **EXPECTATION**                                                 | **RESULT** |
|--------|----------------------|-------------------------|--------------------------------------|-----------------------------------------------------------------|------------|
| T1     | **Tasks**            | Create                  | Create Task Object                   | Signed-in Users can create tasks                                 | ✅         |
| T2     | **Tasks**            | Edit                    | Edit Created Task                   | Signed-in Users can modify their tasks                           | ✅         |
| T3     | **Tasks**            | Add Member              | Add User as Task Member              | Task Owners can add members to their tasks                       | ✅         |
| T4     | **Tasks**            | Delete                  | Delete Task Object                   | Only Owners can delete their tasks                               | ✅         |
| T5     | **Tasks**            | Comment                 | Add Comment to Task                  | Users can comment on tasks                                       | ✅         |
| T6     | **Tasks**            | Comment                 | Delete Own Comment                   | Users can delete their own comments on tasks                     | ✅         |
| T7     | **Tasks**            | Comment                 | View Commentator Profile            | Users can view profiles of comment contributors                  | ✅         |
| T8     | **Tasks**            | Organize                | Filter Tasks                        | Users can filter tasks by ownership and status                   | ✅         |
| T9     | **Tasks**            | View Details            | View Task Details                   | Owners or members can view task details and dialogue             | ✅         |
| P1     | **Profiles**         | Edit                    | Edit Profile                         | Profile owners can edit their profile details                    | ✅         |
| P2     | **Profiles**         | Create                  | Create Profile Object                | New Users create profiles linked to their accounts               | ✅         |
| P3     | **Account Management** | Create Account        | Create User Account                  | New visitors can create accounts                                 | ✅         |
| P4     | **Account Management** | Sign In                | Login to Account                     | Users can sign into their accounts                               | ✅         |
| P5     | **Account Management** | Logout                 | Logout from Account                  | Signed-in Users can logout and receive confirmation              | ✅         |
| P6     | **Access Control**   | Unauthorized Access     | Access Restricted Pages             | Logged-out users cannot access application features              | ✅         |
| P7     | **Feedback**         | Error Handling          | Invalid Actions                     | Users receive appropriate feedback for invalid actions           | ✅         |
| P8     | **Notifications**    | Logout Notification    | Logout Confirmation                 | Users receive notification upon successful logout                | ✅         |
| T10    | **Tasks**            | Task Priority          | Sort Tasks by Priority              | Tasks are sorted correctly by priority                           | ✅         |
| T11    | **Tasks**            | Task Due Dates         | Sort Tasks by Due Dates             | Tasks are displayed and sorted correctly based on due dates      | ✅         |
| P9     | **Profiles**         | Avatar Upload          | Upload Avatar                       | Users can upload and update their avatar successfully            | ✅         |
| P10    | **Access Control**   | Role-Based Access      | Test Different User Roles           | Access permissions are enforced correctly for different roles    | ✅         |
| P11    | **Session Management** | Session Expiration   | Verify Session Expiration           | Sessions expire correctly based on settings                      | ✅         |
| P12    | **Session Management** | Expired Sessions     | Handle Expired Sessions             | Expired sessions are handled correctly                          | ✅         |


- Profile model instances are created upon User Instance creation. 

### Validator Testing 

| **ID** | **CATEGORY**    | **TEST**              | **ACTION**                                  | **RESULT**                            |
|--------|-----------------|-----------------------|---------------------------------------------|--------------------------------------------|
| T1     | **Task**        | pass pep8 validator  | Run all related files from task app through the validator |  ✅                                         |
| TM1    | **Task Messages** | pass pep8 validator | Run all related files from task_messages app through the validator |  ✅                                         |
| P1     | **Profiles**    | pass pep8 validator  | Run all related files from profiles app through the validator |               ✅                     |
| TP1    | **Task Pilot**  | pass pep8 validator  | Run all related files through the validator |  ✅                                         |


### Unfixed Bugs
- None so far.

## Technologies Used:
### Main Languages Used:
- Python

### Frameworks, Libraries & Programs Used:
- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers

## Deployment:
### Project creation:
1. Create the GitHub repository.
2. Create the project app on [Heroku](heroku.com).
3. Add the Postgres package to the Heroku app via the Resources tab.
4. Once the GitHub repository was launched on GitPod, installed the following packages using the `pip install` command:
```
'django<4'
dj3-cloudinary-storage
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers
```
5. Created the Django project with the following command:
```
django-admin startproject project_name .
```
6. Navigated back to [Heroku](heroku.com), and under the Settings tab, added the following configvars:
 - Key: SECRET_KEY | Value: hidden
 - Key: CLOUDINARY_URL | Value: cloudinary://hidden
 - Key: DISABLE_COLLECTSTATIC | Value: 1
 - Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com
7. Add two additional configvars once the ReactApp has been created:
 - Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
 - Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
  - Check that the trailing slash `\` at the end of both links has been removed.
  - Gitpod occasionally updates the browser preview link. Should this occur, the CLIENT_ORIGIN_DEV value shall need to be updated.

8. Created the env.py file, and added the following variables. The value for DATABASE_URL was obtained from the Heroku configvars in the previous step:
```
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'hidden'
os.environ['DATABASE_URL'] = 'postgres://hidden'
```
### In settings.py: 
9. Add the following to INSTALLED_APPS to support the newly installed packages:
```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'corsheaders',
```
10. Import the database, the regular expression module & the env.py
```
import dj_database_url
import re
import os
if os.path.exists('env.py')
    import env
```

11. Below the import statements, add the following variable for Cloudinary:
```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```
- Below INSTALLED_APPS, set site ID:
```
SITE_ID = 1
```
12. Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```
13. Set the default renderer to JSON:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
14. Beneath that, added the following:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```
15. Then added:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```
16. Updated DEBUG variable to:
```
DEBUG = 'DEV' in os.environ
```
17. Updated the DATABASES variable to:
```
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```
18. Added the Heroku app to the ALLOWED_HOSTS variable:
```
os.environ.get('ALLOWED_HOST'),
'localhost',
```
19. Below ALLOWED_HOST, added the CORS_ALLOWED variable as shown in [DRF-API walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first):
```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
20. Also added to the top of MIDDLEWARE:
```
'corsheaders.middleware.CorsMiddleware',
```
- During a deployment issue, it was suggested by a fellow student, Johan, to add the following lines of code below CORS_ALLOW_CREDENTIALS:
```
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CSRF_TRUSTED_ORIGINS = [os.environ.get(
    'CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN',
)]
```
- In addition, Johan also suggested to add the following import statement at the top of the settings.py file:
```
from corsheaders.defaults import default_headers, default_methods
```

### Final requirements:
21. Created a Procfile, & added the following two lines:
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
```
22. Migrated the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
23. Freeze requirements:
```
pip3 freeze --local > requirements.txt
```
24. Added, committed & pushed the changes to GitHub
25. Navigated back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
26. Deployed the branch.

## CREDITS:

### Content:
- The creation of this API database was provided through the step by step guide of the C.I. DRF-API walkthrough project.
- All classes & functions have been credited.

### Media:
- All Images have been used from CleanPNG for this back-end repository. [CleanPNG](https://www.cleanpng.com/)