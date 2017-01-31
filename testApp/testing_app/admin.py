#from django.contrib import admin
#from testApp.testing_app.models import Test

#class TestAdmin(admin.ModelAdmin):
 #   pass
#admin.site.register(Test, TestAdmin)

from django.contrib import admin
from .models import Book
#from .models import Book1

admin.site.register(Book)
#admin.site.register(Book1)