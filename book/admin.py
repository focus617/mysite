from django.contrib import admin


# Register your models here.
from book.models import Publisher, Author, Book, Classfication
# from django.contrib.admin.templatetags.admin_list import date_hierarchy


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'pseudonym', 'email')
    search_fields = ('first_name', 'last_name', 'pseudonym')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('publication_date',)
    # fields = ('title', 'authors', 'publisher', 'publication_date')
    search_fields = ('authors', 'title')
    filter_horizontal = ('authors',)
    raw_id_field = ('publisher',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website', 'address')
    search_fields = ('name', 'country')

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
# admin.site.register(Classfication)

