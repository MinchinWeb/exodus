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
    list_display = [
        "id",
        "owner_type",
        "address_id",
        "owner_id",
        "address_number",
        "details",
    ]

class AddressAdmin(RootsMagicModelAdmin):
    pass

class ChildAdmin(RootsMagicModelAdmin):
    list_display = [
        "record_id",
        "child_id",
        "family_id",
        "father_relationship",
        "mother_relationship",
        "child_order",
        "is_private",
        "father_proof",
        "mother_proof",
        "note",
    ]

class CitationAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "owner_type",
        "source_id",
        "owner_id",
        "quality",
        "is_private",
        "comments",
        "actual_text",
        "reference_number",
        "flags",
        # "fields",
    ]

class ConfigurationAdmin(RootsMagicModelAdmin):
    pass

class EventAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "event_type",
        "owner_type",
        "owner_id",
        "family_id",
        "place_id",
        "site_id",
        "date",
        "sort_date",
        "is_primary",
        "is_private",
        "proof",
        "status",
        "edit_date",
        "sentence",
        # "details",
        # "note",
    ]

class ExclusionAdmin(RootsMagicModelAdmin):
    pass

class FactTypeAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "owner_type",
        "name",
        "abbreviation",
        "gedcom_tag",
        "use_value",
        "use_date",
        "use_place",
        "sentence",
        "flags",
    ]

class FamilyAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "father_id",
        "mother_id",
        "child_id",
        "husband_order",
        "wife_order",
        "is_private",
        "proof",
        "spouse_label",
        "father_label",
        "mother_label",
        # "note",
    ]

class GroupAdmin(RootsMagicModelAdmin):
    pass

class LabelAdmin(RootsMagicModelAdmin):
    pass

class LinkAncestryAdmin(RootsMagicModelAdmin):
    pass

class LinkAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "ext_system",
        "link_type",
        "rootsmagic_id",
        "ext_id",
        "modified",
        "ext_version",
        "ext_date",
        "status",
        "note",
    ]

class MediaLinkAdmin(RootsMagicModelAdmin):
    list_display = [
        "link_id",
        "media_id",
        "owner_type",
        "owner_id",
        "is_primary",
        "include_1",
        "include_2",
        "include_3",
        "include_4",
        "sort_order",
        "rectangle_left",
        "rectangle_top",
        "rectangle_right",
        "rectangle_bottom",
        "note",
        "caption",
        "reference_number",
        "date",
        "sort_date",
        # "description",
    ]

class MultimediaAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "media_type",
        "media_path",
        "media_file",
        "url",
        "thumbnail",
        "caption",
        "reference_number",
        "date",
        "sort_date",
        "description",
    ]

class NameAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "owner_id",
        "surname",
        "given",
        "prefix",
        "suffix",
        "nickname",
        "name_type",
        "date",
        "sort_date",
        "is_primary",
        "is_private",
        "proof",
        "edit_date",
        "sentence",
        # "note",
        "birth_year",
        "death_year",
    ]

class PersonAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "unique_id",
        "sex",
        "edit_date",
        "parent_id",
        "spouse_id",
        "color",
        "relate_1",
        "relate_2",
        "flags",
        "is_living",
        "is_private",
        "proof",
        "bookmark",
        # "note",
    ]

class PlaceAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "place_type",
        "name",
        "abbreviation",
        "normalized",
        "latitude",
        "longitude",
        "exact_latituate_longitude",
        "master_id",
        "note",
    ]

class ResearchItemAdmin(RootsMagicModelAdmin):
    pass

class ResearchAdmin(RootsMagicModelAdmin):
    pass

class RoleAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "role_name",
        "event_type",
        "role_type",
        "sentence",
    ]

class SourceAdmin(RootsMagicModelAdmin):
    pass

class SourceTemplateAdmin(RootsMagicModelAdmin):
    pass

class UrlAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "owner_type",
        "owner_id",
        "link_type",
        "name",
        "url",
        "note",
    ]

class WitnessAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "event_id",
        "person_id",
        "witness_order",
        "role",
        "sentence",
        "note",
        "given",
        "surname",
        "prefix",
        "suffix",
    ]



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
