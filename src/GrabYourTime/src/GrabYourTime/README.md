### Runserver:
python manage.py runserver 0.0.0.0:8000
### Superusers:
janathonl   ljt123456
aval        lxy123456
yaxili      lyx123456
### Apache server reference:
https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04
### Database:
#mysql -u root -p
#WebApp123
create database Team19
create user team19
grant all on Team19.* to 'team19'@'localhost' identified by 'WebApp123';

### How to configure Apache:
sudo vim /etc/apache2/sites-available/000-default.conf
sudo service apache2 restart
### 

