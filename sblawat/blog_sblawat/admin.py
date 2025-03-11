from django.contrib import admin
from .models import PostSblawat

admin.site.register(PostSblawat)

# Personalizacja panelu admina Szymon Blawat
admin.site.site_header = "Panel administracyjny Szymon Blawat"
admin.site.site_title = "Admin Szymon Blawat"
admin.site.index_title = "Witaj w panelu admina Szymon Blawat"
