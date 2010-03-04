from frontend.scans.models import Scan, Comment, Tag
from django.contrib import admin

#class CommentInline(admin.TabularInline):
#    model = Comment
#    extra = 1

#class TagInline(admin.TabularInline):
#    model = Tag
#    extra = 3

#class ScanAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,          {'fields' : ['ocr']}),
#        ('File Info',   {'fields' : ['datedir', 'timedir', 'filename'], 'classes' : ['collapse']}),
#    ]

#    inlines = [CommentInline, TagInline]
#    # search_fields = ['ocr', 'datedir', 'timedir']

#admin.site.register(Scan, ScanAdmin)
admin.site.register(Scan)
admin.site.register(Comment)
admin.site.register(Tag)
