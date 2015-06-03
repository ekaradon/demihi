from django.contrib import admin
from django.db.models import TextField
from django import forms

# Register your models here.
from blog.forms import EntryForm
from blog.models import Album, Comment, Entry, Image, Tag


class AlbumAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["title"]


class CommentInline(admin.StackedInline):
	model = Comment
	extra = 0
	fieldsets = [
		('Comment', {
			'fields': ['author','answer_to', 'body', 'date_published', 'date_modified'],
			'classes': ['collapse']
		})
	]
	readonly_fields = ['date_published', 'date_modified']


class EntryAdmin(admin.ModelAdmin):
	list_display = ['title', 'date_published', 'language', 'was_published_recently']
	list_filter = ['date_published']
	readonly_fields = [ 'date_created', 'date_published', 'date_modified']
	filter_horizontal = ['tags']
	search_fields = ['title', 'body']
	formfield_overrides = { TextField: {'widget': forms.Textarea(attrs={'data-uk-htmleditor':'{markdown:true}'})}, }
	fieldsets = [
		(None, {'fields': ['title', 'active', 'header', 'language', 'tags']}),
		('Date information', {'fields': ['date_created', 'date_published', 'date_modified'], 'classes': ['collapse']}),
		('Content', {'fields': ['body']})
	]
	inlines = [CommentInline]
	form = EntryForm

	def save_model(self, request, obj, form, change):
		if not change:
			obj.author = request.user
		obj.save()

	class Media:
		css = {
			"all": ("css/uikit.min.css", "css/codemirror.css", "css/components/htmleditor.min.css", "css/admin.css")
		}
		js = (
			# "js/admin/jquery_shortcut.js", not necessary since using autocomplete_light which is defining JQuery
			"js/codemirror-compressed.js", "js/uikit.min.js", "js/marked.min.js","js/components/htmleditor.min.js",
		)



class ImageAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	filter_horizontal = ["tags", "albums"]
	list_display = ["__str__", "title", "user", "rating", "size", "tags_", "albums_", "thumbnail", "date_created"]

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()


class TagAdmin(admin.ModelAdmin):
	list_display = ["name"]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Comment)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Tag, TagAdmin)
