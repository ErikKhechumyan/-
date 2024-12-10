

# Create your models here.
from django.db import models

# Create your models here.

class product(models.Model):
    
    name = models.CharField('Product name',max_length=50,null=True,blank=True)
    name2 = models.CharField('Product name2',max_length=50,null=True)
    but = models.CharField('Product but',max_length=50,null=True)
    but2 = models.CharField('Product but2',max_length=50,null=True)
    img = models.ImageField('Product images',upload_to='',null=True)
    
    def __str__(self) -> str:
        return self.name

class menu(models.Model):
    home = models.CharField('home name',max_length=50,null=True)
    about = models.CharField('about name',max_length=50,null=True)
    project = models.CharField('project name',max_length=50,null=True)
    service = models.CharField('service name',max_length=50,null=True)
    contact = models.CharField('contact name',max_length=50,null=True)
    testimonial = models.CharField('testimonial name',max_length=50,null=True)
    
    def __str__(self) -> str:
        return self.home

class serv(models.Model):
    servicee=models.CharField('service name',max_length=50,null=True)
    text=models.CharField('text',max_length=50,null=True)
    img1=models.ImageField('img1 ',upload_to='',null=True)
    text1=models.CharField('text1 ',max_length=50,null=True)
    text11=models.CharField('text11 ',max_length=50,null=True)
    read=models.CharField('read ',max_length=50,null=True)
    img2=models.ImageField('img2 ',upload_to='',null=True)
    text2=models.CharField('text2 ',max_length=50,null=True)
    text22=models.CharField('text22 ',max_length=50,null=True)
    img3=models.ImageField('img3 ',upload_to='',null=True)
    text3=models.CharField('text3 ',max_length=50,null=True)
    text33=models.CharField('text33 ',max_length=50,null=True)
    img4=models.ImageField('img4 ',upload_to='',null=True)
    text4=models.CharField('text4 ',max_length=50,null=True)
    text44=models.CharField('text44 ',max_length=50,null=True)
    
    def __str__(self) -> str:
        return self.servicee
    
class about(models.Model):
    a_me=models.CharField('about ',max_length=50,null=True)
    ab_me=models.CharField('about our company ',max_length=500,null=True)
    read=models.CharField('READ',max_length=50,null=True)
    img=models.ImageField('img ',upload_to='',null=True)
    
    def __str__(self) -> str:
        return self.a_me
    
class cont(models.Model):
    name=models.CharField('name',max_length=50,null=True)
    email=models.EmailField("email",null=True)
    phon=models.IntegerField('phone number',null=True)
    text =models.TextField("text",null=True)
    
    def __str__(self) -> str:
        return self.email
    
class projectss(models.Model):
    text=models.CharField('about ',max_length=50,null=True)
    img=models.ImageField('img ',upload_to='',null=True)
    text1=models.CharField('about1 ',max_length=50,null=True,blank=True)
    img1=models.ImageField('img1 ',upload_to='',null=True,blank=True) 
    text2=models.CharField('about2 ',max_length=50,null=True,blank=True)
    img2=models.ImageField('img2 ',upload_to='',null=True,blank=True) 
    text3=models.CharField('about3 ',max_length=50,null=True,blank=True)
    img3=models.ImageField('img3 ',upload_to='',null=True,blank=True)
    text4=models.CharField('about4 ',max_length=50,null=True,blank=True)
    img4=models.ImageField('img4 ',upload_to='',null=True,blank=True)
    text5=models.CharField('about5 ',max_length=50,null=True,blank=True)
    img5=models.ImageField('img5 ',upload_to='',null=True,blank=True)
    text6=models.CharField('about6 ',max_length=50,null=True,blank=True)
    img6=models.ImageField('img6 ',upload_to='',null=True,blank=True)  
           
    def __str__(self) -> str:
        return self.text
    
class Us(models.Model):
    text=models.CharField('about ',max_length=50,null=True) 
    img1=models.ImageField('img1 ',upload_to='',null=True,blank=True)
    text1=models.CharField('about1 ',max_length=50,null=True) 
    text11=models.CharField('about11 ',max_length=500,null=True) 
    img2=models.ImageField('img1 ',upload_to='',null=True,blank=True)
    text2=models.CharField('about1 ',max_length=50,null=True) 
    text22=models.CharField('about11 ',max_length=500,null=True)
    img3=models.ImageField('img1 ',upload_to='',null=True,blank=True)
    text3=models.CharField('about1 ',max_length=50,null=True) 
    text33=models.CharField('about11 ',max_length=500,null=True)
    
    def __str__(self) -> str:
        return self.text
    
class flag(models.Model):
    text33=models.CharField('about11 ',max_length=500,null=True,blank=True)
    
    uk=models.ImageField('UK ',upload_to='',null=True,blank=True)
    hy=models.ImageField('hy ',upload_to='',null=True,blank=True)
    ru=models.ImageField('ru ',upload_to='',null=True,blank=True)

    def __str__(self) -> str:
        return self.text33

class Post(models.Model):
    author = models.CharField(max_length=250,null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(max_length=250,upload_to ="post/",null=True)
    