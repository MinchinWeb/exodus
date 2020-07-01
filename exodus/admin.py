from django.contrib import admin

from .models import (AddressLink, Address, Child, Citation,
                     Configuration, Event, Exclusion, FactType,
                     Family, Group, Label, LinkAncestry,
                     Link, MediaLink, Multimedia, Name,
                     Person, Place, ResearchItem, Research,
                     Role, Source, SourceTemplate, Url,
                     Witness)

from . import EXODUS_DB_NAME
from .utils.admin import MultiDBModelAdmin
from .utils.rootsmagic import read_and_pprint_date


class RootsMagicModelAdmin(MultiDBModelAdmin):
    using = EXODUS_DB_NAME


class AddressLinkAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "owner_type",
        "address",
        "owner_id",
        "address_number",
        "details",
    ]

class AddressAdmin(RootsMagicModelAdmin):
    pass

class ChildAdmin(RootsMagicModelAdmin):
    list_display = [
        "record_id",
        "child",
        "family",
        "father_relationship",
        "mother_relationship",
        "child_order",
        "is_private",
        "father_proof",
        "mother_proof",
        "note",
    ]
    raw_id_fields = [
        'child',
        'family',
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
        "owner",
        "family",
        "place",
        "site",
        # "date",
        "pretty_date",
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

    def pretty_date(self, obj):
        return read_and_pprint_date(obj.date)
    pretty_date.short_description = "Date"

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
        "father",
        "mother",
        "child",
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
        "rootsmagic",
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
        "media",
        "owner_type",
        "owner",
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
        # "date",
        "pretty_date",
        "sort_date",
        # "description",
    ]

    def pretty_date(self, obj):
        return read_and_pprint_date(obj.date)
    pretty_date.short_description = "Date"

class NameAdmin(RootsMagicModelAdmin):
    list_display = [
        "id",
        "owner",
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
        'primary_name',
        "sex_short",
        "edit_date",
        "parent",
        "spouse",
        "color",
        "relate_1",
        "relate_2",
        "flags",
        "is_living",
        "is_private",
        "proof",
        "unique_id",
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
        "master_place",
        # "latitude",
        # "longitude",
        "pretty_latlong",
        "exact_latituate_longitude",
        "note",
    ]
    raw_id_fields = [
        "master_place"
    ]
    readonly_fields = [
        "pretty_latlong"
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
    raw_id_fields = ['template']

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
        "event",
        "person",
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
