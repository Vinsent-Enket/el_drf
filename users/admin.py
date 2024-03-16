from django.contrib import admin

from users.models import User, Transaction, Subscribe

# Register your models here.


admin.site.register(User)

admin.site.register(Transaction)

admin.site.register(Subscribe)
