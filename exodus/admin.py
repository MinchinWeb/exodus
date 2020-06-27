from django.contrib import admin

from .models import (AddressLink, Address, Child, Citation,
                     Configuration, Event, Exclusion, FactType,
                     Family, Group, Label, LinkAncestry,
                     Link, MediaLink, Multimedia, Name,
                     Person, Place, ResearchItem, Research,
                     Role, Source, SourceTemplate, Url,
                     Witness)

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


class AddressLinkAdmin(RootsMagicModelAdmin):
    pass

class AddressAdmin(RootsMagicModelAdmin):
    pass

class ChildAdmin(RootsMagicModelAdmin):
    pass

class CitationAdmin(RootsMagicModelAdmin):
    pass

class ConfigurationAdmin(RootsMagicModelAdmin):
    pass

class EventAdmin(RootsMagicModelAdmin):
    pass

class ExclusionAdmin(RootsMagicModelAdmin):
    pass

class FactTypeAdmin(RootsMagicModelAdmin):
    pass

class FamilyAdmin(RootsMagicModelAdmin):
    pass

class GroupAdmin(RootsMagicModelAdmin):
    pass

class LabelAdmin(RootsMagicModelAdmin):
    pass

class LinkAncestryAdmin(RootsMagicModelAdmin):
    pass

class LinkAdmin(RootsMagicModelAdmin):
    pass

class MediaLinkAdmin(RootsMagicModelAdmin):
    pass

class MultimediaAdmin(RootsMagicModelAdmin):
    pass

class NameAdmin(RootsMagicModelAdmin):
    pass

class PersonAdmin(RootsMagicModelAdmin):
    pass

class PlaceAdmin(RootsMagicModelAdmin):
    pass

class ResearchItemAdmin(RootsMagicModelAdmin):
    pass

class ResearchAdmin(RootsMagicModelAdmin):
    pass

class RoleAdmin(RootsMagicModelAdmin):
    pass

class SourceAdmin(RootsMagicModelAdmin):
    pass

class SourceTemplateAdmin(RootsMagicModelAdmin):
    pass

class UrlAdmin(RootsMagicModelAdmin):
    pass

class WitnessAdmin(RootsMagicModelAdmin):
    pass



admin.site.register(AddressLink, AddressLinkAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Citation, CitationAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Exclusion, ExclusionAdmin)
admin.site.register(FactType, FactTypeAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(LinkAncestry, LinkAncestryAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(MediaLink, MediaLinkAdmin)
admin.site.register(Multimedia, MultimediaAdmin)
admin.site.register(Name, NameAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(ResearchItem, ResearchItemAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(SourceTemplate, SourceTemplateAdmin)
admin.site.register(Url, UrlAdmin)
admin.site.register(Witness, WitnessAdmin)
