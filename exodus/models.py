# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddressLink(models.Model):
    id = models.AutoField(db_column='LinkID', primary_key=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    address_id = models.IntegerField(db_column='AddressID', blank=True, null=True)
    owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    address_number = models.IntegerField(db_column='AddressNum', blank=True, null=True)
    details = models.TextField(db_column='Details', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AddressLinkTable'
        verbose_name = "Address Link"


class Address(models.Model):
    id = models.AutoField(db_column='AddressID', primary_key=True)
    address_type = models.IntegerField(db_column='AddressType', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    street_1 = models.TextField(db_column='Street1', blank=True, null=True)
    street_2 = models.TextField(db_column='Street2', blank=True, null=True)
    city = models.TextField(db_column='City', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    zip = models.TextField(db_column='Zip', blank=True, null=True)
    country = models.TextField(db_column='Country', blank=True, null=True)
    phone_1 = models.TextField(db_column='Phone1', blank=True, null=True)
    phone_2 = models.TextField(db_column='Phone2', blank=True, null=True)
    fax = models.TextField(db_column='Fax', blank=True, null=True)
    email = models.TextField(db_column='Email', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)
    latitude = models.IntegerField(db_column='Latitude', blank=True, null=True)
    longitude = models.IntegerField(db_column='Longitude', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AddressTable'
        verbose_name_plural = "Addresses"


class Child(models.Model):
    record_id = models.AutoField(db_column='RecID', primary_key=True)
    child_id = models.IntegerField(db_column='ChildID', blank=True, null=True)
    family_id = models.IntegerField(db_column='FamilyID', blank=True, null=True)
    father_relationship = models.IntegerField(db_column='RelFather', blank=True, null=True)
    mother_relationship = models.IntegerField(db_column='RelMother', blank=True, null=True)
    child_order = models.IntegerField(db_column='ChildOrder', blank=True, null=True)
    is_private = models.IntegerField(db_column='IsPrivate', blank=True, null=True)
    father_proof = models.IntegerField(db_column='ProofFather', blank=True, null=True)
    mother_proof = models.IntegerField(db_column='ProofMother', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ChildTable'
        verbose_name_plural = "Children"


class Citation(models.Model):
    id = models.AutoField(db_column='CitationID', primary_key=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    source_id = models.IntegerField(db_column='SourceID', blank=True, null=True)
    owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    quality = models.TextField(db_column='Quality', blank=True, null=True)
    is_private = models.IntegerField(db_column='IsPrivate', blank=True, null=True)
    comments = models.BinaryField(db_column='Comments', blank=True, null=True)
    actual_text = models.BinaryField(db_column='ActualText', blank=True, null=True)
    reference_number = models.TextField(db_column='RefNumber', blank=True, null=True)
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)
    fields = models.BinaryField(db_column='Fields', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CitationTable'


class Configuration(models.Model):
    record_id = models.AutoField(db_column='RecID', primary_key=True)
    record_type = models.IntegerField(db_column='RecType', blank=True, null=True)
    title = models.TextField(db_column='Title', blank=True, null=True)
    data_record = models.BinaryField(db_column='DataRec', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ConfigTable'


class Event(models.Model):
    id = models.AutoField(db_column='EventID', primary_key=True)
    event_type = models.IntegerField(db_column='EventType', blank=True, null=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    family_id = models.IntegerField(db_column='FamilyID', blank=True, null=True)
    place_id = models.IntegerField(db_column='PlaceID', blank=True, null=True)
    site_id = models.IntegerField(db_column='SiteID', blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)
    sort_date = models.IntegerField(db_column='SortDate', blank=True, null=True)
    is_primary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)
    is_private = models.IntegerField(db_column='IsPrivate', blank=True, null=True)
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    edit_date = models.TextField(db_column='EditDate', blank=True, null=True)  # This field type is a guess.
    sentence = models.BinaryField(db_column='Sentence', blank=True, null=True)
    details = models.BinaryField(db_column='Details', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EventTable'


class Exclusion(models.Model):
    record_id = models.AutoField(db_column='RecID', primary_key=True)
    exclusion_type = models.IntegerField(db_column='ExclusionType', blank=True, null=True)
    id_1 = models.IntegerField(db_column='ID1', blank=True, null=True)
    id_2 = models.IntegerField(db_column='ID2', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ExclusionTable'
        unique_together = (('exclusion_type', 'id_1', 'id_2'),)


class FactType(models.Model):
    id = models.AutoField(db_column='FactTypeID', primary_key=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    abbreviation = models.TextField(db_column='Abbrev', blank=True, null=True)
    gedcom_tag = models.TextField(db_column='GedcomTag', blank=True, null=True)
    use_value = models.IntegerField(db_column='UseValue', blank=True, null=True)
    use_date = models.IntegerField(db_column='UseDate', blank=True, null=True)
    use_place = models.IntegerField(db_column='UsePlace', blank=True, null=True)
    sentence = models.BinaryField(db_column='Sentence', blank=True, null=True)
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FactTypeTable'
        verbose_name = "Fact Type"


class Family(models.Model):
    id = models.AutoField(db_column='FamilyID', primary_key=True)
    father_id = models.IntegerField(db_column='FatherID', blank=True, null=True)
    mother_id = models.IntegerField(db_column='MotherID', blank=True, null=True)
    child_id = models.IntegerField(db_column='ChildID', blank=True, null=True)
    husband_order = models.IntegerField(db_column='HusbOrder', blank=True, null=True)
    wife_order = models.IntegerField(db_column='WifeOrder', blank=True, null=True)
    is_private = models.IntegerField(db_column='IsPrivate', blank=True, null=True)
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)
    spouse_label = models.IntegerField(db_column='SpouseLabel', blank=True, null=True)
    father_label = models.IntegerField(db_column='FatherLabel', blank=True, null=True)
    mother_label = models.IntegerField(db_column='MotherLabel', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FamilyTable'
        verbose_name_plural = "Families"


class Group(models.Model):
    record_id = models.AutoField(db_column='RecID', primary_key=True)
    group_id = models.IntegerField(db_column='GroupID', blank=True, null=True)
    start_id = models.IntegerField(db_column='StartID', blank=True, null=True)
    end_id = models.IntegerField(db_column='EndID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GroupTable'


class Label(models.Model):
    id = models.AutoField(db_column='LabelID', primary_key=True)
    label_type = models.IntegerField(db_column='LabelType', blank=True, null=True)
    label_value = models.IntegerField(db_column='LabelValue', blank=True, null=True)
    label_name = models.TextField(db_column='LabelName', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LabelTable'


class LinkAncestry(models.Model):
    link_id = models.AutoField(db_column='LinkID', primary_key=True)
    ext_system = models.IntegerField(db_column='extSystem', blank=True, null=True)
    link_type = models.IntegerField(db_column='LinkType', blank=True, null=True)
    rootsmagic_id = models.IntegerField(db_column='rmID', blank=True, null=True)
    ext_id = models.TextField(db_column='extID', blank=True, null=True)
    modified = models.IntegerField(db_column='Modified', blank=True, null=True)
    ext_version = models.TextField(db_column='extVersion', blank=True, null=True)
    ext_date = models.TextField(db_column='extDate', blank=True, null=True)  # This field type is a guess.
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LinkAncestryTable'
        verbose_name = "Link Ancestry"
        verbose_name_plural = "Link Ancestries"


class Link(models.Model):
    id = models.AutoField(db_column='LinkID', primary_key=True)
    ext_system = models.IntegerField(db_column='extSystem', blank=True, null=True)
    link_type = models.IntegerField(db_column='LinkType', blank=True, null=True)
    rootsmagic_id = models.IntegerField(db_column='rmID', blank=True, null=True)
    ext_id = models.TextField(db_column='extID', blank=True, null=True)
    modified = models.IntegerField(db_column='Modified', blank=True, null=True)
    ext_version = models.TextField(db_column='extVersion', blank=True, null=True)
    ext_date = models.TextField(db_column='extDate', blank=True, null=True)  # This field type is a guess.
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LinkTable'


class MediaLink(models.Model):
    link_id = models.AutoField(db_column='LinkID', primary_key=True)
    media_id = models.IntegerField(db_column='MediaID', blank=True, null=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    is_primary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)
    include_1 = models.IntegerField(db_column='Include1', blank=True, null=True)
    include_2 = models.IntegerField(db_column='Include2', blank=True, null=True)
    include_3 = models.IntegerField(db_column='Include3', blank=True, null=True)
    include_4 = models.IntegerField(db_column='Include4', blank=True, null=True)
    sort_order = models.IntegerField(db_column='SortOrder', blank=True, null=True)
    rectangle_left = models.IntegerField(db_column='RectLeft', blank=True, null=True)
    rectangle_top = models.IntegerField(db_column='RectTop', blank=True, null=True)
    rectangle_right = models.IntegerField(db_column='RectRight', blank=True, null=True)
    rectangle_bottom = models.IntegerField(db_column='RectBottom', blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)
    caption = models.TextField(db_column='Caption', blank=True, null=True)
    reference_number = models.TextField(db_column='RefNumber', blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)
    sort_date = models.IntegerField(db_column='SortDate', blank=True, null=True)
    description = models.BinaryField(db_column='Description', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MediaLinkTable'
        verbose_name = "Media Link"


class Multimedia(models.Model):
    id = models.AutoField(db_column='MediaID', primary_key=True)
    media_type = models.IntegerField(db_column='MediaType', blank=True, null=True)
    media_path = models.TextField(db_column='MediaPath', blank=True, null=True)
    media_file = models.TextField(db_column='MediaFile', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)
    thumbnail = models.BinaryField(db_column='Thumbnail', blank=True, null=True)
    caption = models.TextField(db_column='Caption', blank=True, null=True)
    reference_number = models.TextField(db_column='RefNumber', blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)
    sort_date = models.IntegerField(db_column='SortDate', blank=True, null=True)
    description = models.BinaryField(db_column='Description', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MultimediaTable'


class Name(models.Model):
    id = models.AutoField(db_column='NameID', primary_key=True)
    owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    surname = models.TextField(db_column='Surname', blank=True, null=True)
    given = models.TextField(db_column='Given', blank=True, null=True)
    prefix = models.TextField(db_column='Prefix', blank=True, null=True)
    suffix = models.TextField(db_column='Suffix', blank=True, null=True)
    nickname = models.TextField(db_column='Nickname', blank=True, null=True)
    name_type = models.IntegerField(db_column='NameType', blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)
    sort_date = models.IntegerField(db_column='SortDate', blank=True, null=True)
    is_primary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)
    is_private = models.IntegerField(db_column='IsPrivate', blank=True, null=True)
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)
    edit_date = models.TextField(db_column='EditDate', blank=True, null=True)  # This field type is a guess.
    sentence = models.BinaryField(db_column='Sentence', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)
    birth_year = models.IntegerField(db_column='BirthYear', blank=True, null=True)
    death_year = models.IntegerField(db_column='DeathYear', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'NameTable'

    def __str__(self):
        return_str = " ".join([
            self.prefix,
            self.given,
            f'"{self.nickname}"' if self.nickname else '',
            self.surname,
            self.suffix])
        if self.birth_year or self.death_year:
            return_str += f" ({self.birth_year if self.birth_year else ''}-{self.death_year if self.death_year else ''})"
        return return_str


class Person(models.Model):
    id = models.AutoField(db_column='PersonID', primary_key=True)
    unique_id = models.TextField(db_column='UniqueID', blank=True, null=True)
    sex = models.IntegerField(db_column='Sex', blank=True, null=True)
    edit_date = models.TextField(db_column='EditDate', blank=True, null=True)  # This field type is a guess.
    parent_id = models.IntegerField(db_column='ParentID', blank=True, null=True)
    spouse_id = models.IntegerField(db_column='SpouseID', blank=True, null=True)
    color = models.IntegerField(db_column='Color', blank=True, null=True)
    relate_1 = models.IntegerField(db_column='Relate1', blank=True, null=True)
    relate_2 = models.IntegerField(db_column='Relate2', blank=True, null=True)
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)
    is_living = models.IntegerField(db_column='Living', blank=True, null=True)
    is_private = models.IntegerField(db_column='IsPrivate', blank=True, null=True)
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)
    bookmark = models.IntegerField(db_column='Bookmark', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PersonTable'
        verbose_name_plural = "People"


class Place(models.Model):
    id = models.AutoField(db_column='PlaceID', primary_key=True)
    place_type = models.IntegerField(db_column='PlaceType', blank=True, null=True)
    # Place Types:
    #   0 -- "regular" place
    #   1 -- LDS Temple
    #   2 -- "place details" (tied to a regular place)
    name = models.TextField(db_column='Name', blank=True, null=True)
    abbreviation = models.TextField(db_column='Abbrev', blank=True, null=True)
    # used for up to a 5 letter code for a temple
    normalized = models.TextField(db_column='Normalized', blank=True, null=True)
    latitude = models.IntegerField(db_column='Latitude', blank=True, null=True)
    longitude = models.IntegerField(db_column='Longitude', blank=True, null=True)
    exact_latituate_longitude = models.IntegerField(db_column='LatLongExact', blank=True, null=True)
    master_id = models.IntegerField(db_column='MasterID', blank=True, null=True)
    # when set, is the "master" place (place_type 0) for a place_type 2
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaceTable'


class ResearchItem(models.Model):
    id = models.AutoField(db_column='ItemID', primary_key=True)
    log_id = models.IntegerField(db_column='LogID', blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)
    sort_date = models.IntegerField(db_column='SortDate', blank=True, null=True)
    reference_number = models.TextField(db_column='RefNumber', blank=True, null=True)
    repository = models.TextField(db_column='Repository', blank=True, null=True)
    goal = models.TextField(db_column='Goal', blank=True, null=True)
    source = models.TextField(db_column='Source', blank=True, null=True)
    result = models.TextField(db_column='Result', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ResearchItemTable'
        verbose_name = "Research Item"


class Research(models.Model):
    id = models.AutoField(db_column='TaskID', primary_key=True)
    task_type = models.IntegerField(db_column='TaskType', blank=True, null=True)
    owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    reference_number = models.TextField(db_column='RefNumber', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)
    date_1 = models.TextField(db_column='Date1', blank=True, null=True)
    date_2 = models.TextField(db_column='Date2', blank=True, null=True)
    date_3 = models.TextField(db_column='Date3', blank=True, null=True)
    sortdate_1 = models.IntegerField(db_column='SortDate1', blank=True, null=True)
    sortdate_2 = models.IntegerField(db_column='SortDate2', blank=True, null=True)
    sortdate_3 = models.IntegerField(db_column='SortDate3', blank=True, null=True)
    filename = models.TextField(db_column='Filename', blank=True, null=True)
    details = models.BinaryField(db_column='Details', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ResearchTable'
        # verbose_name = "Research Task"
        verbose_name_plural = "Researches"


class Role(models.Model):
    id = models.AutoField(db_column='RoleID', primary_key=True)
    role_name = models.TextField(db_column='RoleName', blank=True, null=True)
    event_type = models.IntegerField(db_column='EventType', blank=True, null=True)
    role_type = models.IntegerField(db_column='RoleType', blank=True, null=True)
    sentence = models.TextField(db_column='Sentence', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoleTable'

    def __str__(self):
        return f"{self.role_name} ({self.event_type})"


class Source(models.Model):
    id = models.AutoField(db_column='SourceID', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    reference_number = models.TextField(db_column='RefNumber', blank=True, null=True)
    actual_text = models.TextField(db_column='ActualText', blank=True, null=True)
    comments = models.TextField(db_column='Comments', blank=True, null=True)
    is_private = models.IntegerField(db_column='IsPrivate', blank=True, null=True)
    template_id = models.IntegerField(db_column='TemplateID', blank=True, null=True)
    fields = models.BinaryField(db_column='Fields', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SourceTable'


class SourceTemplate(models.Model):
    id = models.AutoField(db_column='TemplateID', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    favorite = models.IntegerField(db_column='Favorite', blank=True, null=True)
    category = models.TextField(db_column='Category', blank=True, null=True)
    footnote = models.TextField(db_column='Footnote', blank=True, null=True)
    short_footnote = models.TextField(db_column='ShortFootnote', blank=True, null=True)
    bibliography = models.TextField(db_column='Bibliography', blank=True, null=True)
    field_definitions = models.BinaryField(db_column='FieldDefs', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SourceTemplateTable'
        verbose_name = "Source Template"


class Url(models.Model):
    id = models.AutoField(db_column='LinkID', primary_key=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    link_type = models.IntegerField(db_column='LinkType', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'URLTable'


class Witness(models.Model):
    id = models.AutoField(db_column='WitnessID', primary_key=True)
    event_id = models.IntegerField(db_column='EventID', blank=True, null=True)
    person_id = models.IntegerField(db_column='PersonID', blank=True, null=True)
    witness_order = models.IntegerField(db_column='WitnessOrder', blank=True, null=True)
    role = models.IntegerField(db_column='Role', blank=True, null=True)
    sentence = models.TextField(db_column='Sentence', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)
    given = models.TextField(db_column='Given', blank=True, null=True)
    surname = models.TextField(db_column='Surname', blank=True, null=True)
    prefix = models.TextField(db_column='Prefix', blank=True, null=True)
    suffix = models.TextField(db_column='Suffix', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WitnessTable'
        verbose_name_plural = "Witnesses"
