from django.contrib import admin

from .models import (Addresslinktable, Addresstable, Childtable, Citationtable,
                     Configtable, Eventtable, Exclusiontable, Facttypetable,
                     Familytable, Grouptable, Labeltable, Linkancestrytable,
                     Linktable, Medialinktable, Multimediatable, Nametable,
                     Persontable, Placetable, Researchitemtable, Researchtable,
                     Roletable, Sourcetable, Sourcetemplatetable, Urltable,
                     Witnesstable)

class MultiDBModelAdmin(admin.ModelAdmin):
    # file:///home/william/Code/exodus-testsite/django-docs/topics/db/multi-db.html

    # A handy constant for the name of the alternate database.
    using = 'other'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class RootsMagicModelAdmin(MultiDBModelAdmin):
    using = 'rm'


class AddresslinktableAdmin(RootsMagicModelAdmin):
    pass

class AddresstableAdmin(RootsMagicModelAdmin):
    pass

class ChildtableAdmin(RootsMagicModelAdmin):
    pass

class CitationtableAdmin(RootsMagicModelAdmin):
    pass

class ConfigtableAdmin(RootsMagicModelAdmin):
    pass

class EventtableAdmin(RootsMagicModelAdmin):
    pass

class ExclusiontableAdmin(RootsMagicModelAdmin):
    pass

class FacttypetableAdmin(RootsMagicModelAdmin):
    pass

class FamilytableAdmin(RootsMagicModelAdmin):
    pass

class GrouptableAdmin(RootsMagicModelAdmin):
    pass

class LabeltableAdmin(RootsMagicModelAdmin):
    pass

class LinkancestrytableAdmin(RootsMagicModelAdmin):
    pass

class LinktableAdmin(RootsMagicModelAdmin):
    pass

class MedialinktableAdmin(RootsMagicModelAdmin):
    pass

class MultimediatableAdmin(RootsMagicModelAdmin):
    pass

class NametableAdmin(RootsMagicModelAdmin):
    pass

class PersontableAdmin(RootsMagicModelAdmin):
    pass

class PlacetableAdmin(RootsMagicModelAdmin):
    pass

class ResearchitemtableAdmin(RootsMagicModelAdmin):
    pass

class ResearchtableAdmin(RootsMagicModelAdmin):
    pass

class RoletableAdmin(RootsMagicModelAdmin):
    pass

class SourcetableAdmin(RootsMagicModelAdmin):
    pass

class SourcetemplatetableAdmin(RootsMagicModelAdmin):
    pass

class UrltableAdmin(RootsMagicModelAdmin):
    pass

class WitnesstableAdmin(RootsMagicModelAdmin):
    pass



admin.site.register(Addresslinktable, AddresslinktableAdmin)
admin.site.register(Addresstable, AddresstableAdmin)
admin.site.register(Childtable, ChildtableAdmin)
admin.site.register(Citationtable, CitationtableAdmin)
admin.site.register(Configtable, ConfigtableAdmin)
admin.site.register(Eventtable, EventtableAdmin)
admin.site.register(Exclusiontable, ExclusiontableAdmin)
admin.site.register(Facttypetable, FacttypetableAdmin)
admin.site.register(Familytable, FamilytableAdmin)
admin.site.register(Grouptable, GrouptableAdmin)
admin.site.register(Labeltable, LabeltableAdmin)
admin.site.register(Linkancestrytable, LinkancestrytableAdmin)
admin.site.register(Linktable, LinktableAdmin)
admin.site.register(Medialinktable, MedialinktableAdmin)
admin.site.register(Multimediatable, MultimediatableAdmin)
admin.site.register(Nametable, NametableAdmin)
admin.site.register(Persontable, PersontableAdmin)
admin.site.register(Placetable, PlacetableAdmin)
admin.site.register(Researchitemtable, ResearchitemtableAdmin)
admin.site.register(Researchtable, ResearchtableAdmin)
admin.site.register(Roletable, RoletableAdmin)
admin.site.register(Sourcetable, SourcetableAdmin)
admin.site.register(Sourcetemplatetable, SourcetemplatetableAdmin)
admin.site.register(Urltable, UrltableAdmin)
admin.site.register(Witnesstable, WitnesstableAdmin)
