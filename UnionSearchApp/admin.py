from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Direaction)
class DireactionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Classfication)
class ClassficationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    pass
