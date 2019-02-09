# monitor_app

django app for website monitoring


## guide:

* backgroud: python version: 3.5.2, django version: 2.1.5, postgresql: 10.6
* db info
  ```python
  # DATABASES = {
  #     'default': {
  #         'ENGINE': 'django.db.backends.sqlite3',
  #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  #     }
  # }
  
  # postgreSQL
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'mydb',
          'USER': 'admin',
          'PASSWORD': 'admin',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```
 * use django migrate function to initialize DATABASES
   ``` 
   if there are initial files in dir: monitor_app\users\migrations
   just run command: 'python manage.py migrate'
    
   else, run command: 'python manage.py makemigrations' to generate the files, 
   and then run command: 'python manage.py migrate'
   
   ```
   if it completed, you will see table in DB. (pyAdmin4 of postgreSQL)
   
   ![image.png](https://upload-images.jianshu.io/upload_images/2407746-0f3d3bf87a5ac1e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
   
   
* it's highly recommended to create a super user of django, run: 'python manage.py createsuperuser'.

  user can not only sign in to the monitor_app, but also admin panel.




* dashboard:

![image.png](https://upload-images.jianshu.io/upload_images/2407746-530853251e684e93.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
   
* admin panel

![image.png](https://upload-images.jianshu.io/upload_images/2407746-66c06bf58ee9330a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
