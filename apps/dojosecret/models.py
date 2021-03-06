from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, password2):
        # reg =post['username']
        errors = []
        user = first_name
        if len(email) < 1 or len(first_name) < 1 or len(last_name) < 1:
            errors.append("Please Complete The Form")
        
        if User.objects.filter(email = email).exists():
            errors.append("Email alredy exists in database")

        if not EMAIL_REGEX.match(email):
            errors.append("Email must include @ ")
        if len(password) <= 8:
            errors.append("Password too short")

        if password != password2:
            errors.append("Passwords do not match")
          
        if not errors:
            user = User.objects.create(first_name = first_name, last_name = last_name, email=email,password=password)
            return {"status": True, "data": user}
        else:
            return {"status": False, "data": errors}

    def login(self, email, password):
        errors = []
        success = "Successful Login"
        user = User.objects.filter(email = email)
        if User.objects.filter(email = email).exists():
            if User.objects.filter(email=email, password=password).exists():
                return {"status": True, "data": user}
            else: 
                errors.append("Incorrect Password")
                return {"status": False, "data": errors}
        else:
            errors.append("Email not found")
            return {"status": False, "data": errors}

class User(models.Model):
    first_name = models.CharField(max_length=38, default = "")
    last_name = models.CharField(max_length=38, default = "")
    email = models.CharField(max_length=38, default = "")
    password = models.CharField(max_length=38, default = "")
    created_at = models.DateTimeField(auto_now = True)
    objects = UserManager()



class Author(models.Model):
    name = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    title= models.CharField(max_length= 255)
    author= models.ForeignKey(Author, related_name="author")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    


class Review(models.Model):
    review = models.CharField(max_length= 255)
    rating = models.CharField(max_length=255, default="")
    user = models.ForeignKey(User, related_name="user" )
    book= models.ForeignKey(Book, related_name="book")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    