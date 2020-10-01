from django.contrib import admin
from .models import Book

from django.shortcuts import get_object_or_404

from users.models import Course, Book
from multiupload.admin import MultiUploadAdmin
# Register your models here.
class BookInlineAdmin(admin.TabularInline):
    model = Book

class CourseMultiuploadMixing(object):

    def process_uploaded_file(self, uploaded, course, request):
        if course:
            book = course.books.create(file=uploaded)
        else:
            book = Book.objects.create(file=uploaded, course=None)
        return {
            'url': image.pdf.url,
            'thumbnail_url': image.pdf.url,
            'pdf_url': book.pdf.url,
            'cover_url': book.cover.url,
            'id': book.id,
            'name': book.title
        }
        
class CourseAdmin(CourseMultiuploadMixing, MultiUploadAdmin):
    inlines = [BookInlineAdmin,]
    multiupload_form = True
    multiupload_list = False

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Book, pk=pk)
        return obj.delete()

class BookAdmin(CourseMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = True
    multiupload_limitconcurrentuploads = 6


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Book, BookAdmin)

