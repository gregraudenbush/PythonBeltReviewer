from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book, Review, Author
from django.contrib import messages

def index(request):
    


    return render(request, "dojosecret/index.html")
def success(request):
    
    user = request.session['id']
    context = {
        "user" : User.objects.get(id = user),
        "author" : Author.objects.all(), 
        "book" : Book.objects.all(),
        "reviews" : Review.objects.all()
    }
    

    return render(request, "dojosecret/wall.html", context)
def logout (request):
    if request.method == "POST":
        user = ""
        return redirect ('/')
def add (request):

    context = {
        "author" : Author.objects.all()

    }

    return render(request, "dojosecret/add.html", context)    

def user (request, id):
    user = User.objects.get(id = id)
    count = Review.objects.filter(user = user).count()
    context = {
        "user" : User.objects.get(id = id),
        "review" : Review.objects.filter(user = user),
        "count" : count
    }

    return render(request, "dojosecret/user.html", context)

def book (request, id):
    book = Book.objects.get(id = id)
    context = {
        "book" : Book.objects.get(id = id),
        "reviews" : Review.objects.filter(book = book)
    }


    return render(request, 'dojosecret/book.html', context)

def login(request):
    
    
    if request.method =="POST":
        login = User.objects.login(request.POST['email'], request.POST['password'])
        
        if login['status']:
            
            success = login['data']
            messages.error(request, str(success))
            user = User.objects.get(email = request.POST['email'])
            request.session['id'] = user.id
            return redirect('/success')
        else:
            print "work3"
            error = login['data']
            messages.success(request, str(error))
            return redirect('/')



def register(request):
    
    if request.method == "POST":
        
        res = User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password2'])

        if res['status']:
            
            username = res['data'].user
            messages.success(request, "Thank You Registration")
            user = User.objects.get(email = request.POST['email'])
            request.session['id'] = user.id
            return redirect('/success')
        else:
            for errors in res['data']:
                messages.error(request, errors)
            return redirect('/')
            

def delete(request):

    # review = Review.objects.get(id = id)
    # count1 = Review.objects.filter(book = request.POST['bookid']).count()
    if request.method == "POST":
        
        Review.objects.get(id = request.POST['id']).delete()
        # count = Review.objects.filter(id = request.POST['id']).count()
        # if count == 1:
        #     Review.objects.get(id = request.POST['id']).delete()
        #     Book.objects.get(title = request.POST['title']).delete()   
    # else:    
        # Review.objects.get(id = request.POST['id']).delete()
        

        return redirect ('/success')

def review(request):

    if request.method == "POST":
        try:
            author = Author.objects.get(name = request.POST['author'])
        except:
            author = Author.objects.create(name = request.POST['author'])
        try:
            book = Book.objects.get(title = request.POST['title'], author=author)
        except:
            book = Book.objects.create(title = request.POST['title'], author=author)
        
        review = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], user = User.objects.get(id = request.session['id']), book = book)
    
        return redirect('/success')

        