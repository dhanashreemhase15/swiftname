from django.shortcuts import render,redirect
from django.http import HttpResponse
import  datetime
# Create your views here.
def index(request):
    #content="Hello all i am from content"
    #x=12
    #return HttpResponse(x)
    #content="<h1>value of x is : {}</h1>".format(x)
    #return HttpResponse(content)
    #return HttpResponse("<h1>hello world</h1>")
    return redirect('/home')

def home(request):
    dt=datetime.datetime.now()
    content={}
    #content['x']='Itvedant'
    #content['x']=160
    #content['y']=100
    #content['l']=[10,20,30,40,50]
    #content['t']=(100,200,300,'Eclass')
    #content['s']={1,2,3,4,5}
    content['d']={'a':'apple','b':'ball','c':20,'f':'fish'}
    content['name']='Itvedant-Eclass'
    content['cdt']=dt
    return render(request,'index.html',content)
    #return HttpResponse("<h1> welcome to home page</h1>")

def delete(request,rid):    #rid=15
    content="<h1>record id is : {}</h1>".format(rid)
    return HttpResponse(content)

def addition(request,x1,x2):
    #content="x1 is :{} and x2 is : {}".format(x1,x2)
    content=int(x1)+int(x2)
    return HttpResponse(content)

def postblog(request):
    form='''
        <html>
        <head>
            <title>BLOG|CREATE</title>
        </head>
        <body>
            <form method="POST">
                <table>
                    <tr>
                        <td>Heading:</td>
                        <td><input type="text" name="bhead" /></td>
                    </tr>
                    <tr>
                        <td>category:</td>
                        <td><input type="text" name="bcat" /></td>
                    </tr>
                    <tr>
                        <td>Description:</td>
                        <td><textarea name="bdesc" cols="20" rows="5" ></textarea></td>
                    </tr>
                    <tr>
                        <td><input type="submit" name="send" value="POST" /></td>
                    </tr>
                </table>
            
            </form>
        </body>
        </html>
    
    '''
    return HttpResponse(form)

def contact(request):
    return render(request,'contact.html')

def placement(request):
    return render(request,'placement.html')

def create(request):
    return render(request,'createblog.html')

def store(request):
    # h=request.GET['bhead']
    # c=request.GET['bcat']
    # d=request.GET['bdesc']
    h=request.POST['bhead']
    c=request.POST['bcat']
    d=request.POST['bdesc']
    return HttpResponse(h+"-"+c+"-"+d)