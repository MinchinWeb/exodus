# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from . import EXODUS_DB_NAME, LAT_LONG_SECOND_DECIMAL_PLACES


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
    # no such collation sequence: RMNOCASE
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
    # child_id = models.IntegerField(db_column='ChildID', blank=True, null=True)
    # family_id = models.IntegerField(db_column='FamilyID', blank=True, null=True)
    child = models.ForeignKey('Person', on_delete=models.SET(0), related_name="child", db_column='ChildID', blank=True, null=True)
    family = models.ForeignKey('Family', on_delete=models.SET(0), related_name="child_family", db_column='FamilyID', blank=True, null=True)
    father_relationship = models.IntegerField(db_column='RelFather', blank=True, null=True)
    mother_relationship = models.IntegerField(db_column='RelMother', blank=True, null=True)
    child_order = models.IntegerField(db_column='ChildOrder', blank=True, null=True)
    is_private = models.BooleanField(db_column='IsPrivate', blank=True, null=True)
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
    quality = models.CharField(db_column='Quality', max_length=3, blank=True, null=True)
    # three characters, using "~~~" for "undefined"
    # "PDO" is valid (for "Primary", ? "Original")
    is_private = models.BooleanField(db_column='IsPrivate', blank=True, null=True)
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
    # event_type = models.IntegerField(db_column='EventType', blank=True, null=True)
    event_type = models.ForeignKey('FactType', on_delete=models.PROTECT, db_column='EventType', blank=True, null=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    # owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    # family_id = models.IntegerField(db_column='FamilyID', blank=True, null=True)
    # place_id = models.IntegerField(db_column='PlaceID', blank=True, null=True)
    # site_id = models.IntegerField(db_column='SiteID', blank=True, null=True)
    owner = models.ForeignKey('Person', on_delete=models.CASCADE, db_column='OwnerID', blank=True, null=True)
    family = models.ForeignKey('Family', on_delete=models.CASCADE, db_column='FamilyID', blank=True, null=True)
    place = models.ForeignKey('Place', on_delete=models.PROTECT, related_name='event_place', db_column='PlaceID', blank=True, null=True)
    site = models.ForeignKey('Place', on_delete=models.PROTECT, related_name='event_site', db_column='SiteID', blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)
    sort_date = models.IntegerField(db_column='SortDate', blank=True, null=True)
    is_primary = models.BooleanField(db_column='IsPrimary', blank=True, null=True)
    is_private = models.BooleanField(db_column='IsPrivate', blank=True, null=True)
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
    # 0 -- individual
    # 1 -- couple or family
    name = models.TextField(db_column='Name', blank=True, null=True)
    # english name for the event; useful for tables
    abbreviation = models.TextField(db_column='Abbrev', blank=True, null=True)
    gedcom_tag = models.CharField(db_column='GedcomTag', max_length=4, blank=True, null=True)
    use_value = models.BooleanField(db_column='UseValue', blank=True, null=True)
    use_date = models.BooleanField(db_column='UseDate', blank=True, null=True)
    use_place = models.BooleanField(db_column='UsePlace', blank=True, null=True)
    sentence = models.BinaryField(db_column='Sentence', blank=True, null=True)
    # useful to create a "story" for the facts
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FactTypeTable'
        verbose_name = "Fact Type"

    def __str__(self):
        return self.name


class Family(models.Model):
    id = models.AutoField(db_column='FamilyID', primary_key=True)
    # father_id = models.IntegerField(db_column='FatherID', blank=True, null=True)
    # mother_id = models.IntegerField(db_column='MotherID', blank=True, null=True)
    # child_id = models.IntegerField(db_column='ChildID', blank=True, null=True)
    father = models.ForeignKey('Person', on_delete=models.SET(0), related_name="family_father", db_column='FatherID', blank=True, null=True)
    mother = models.ForeignKey('Person', on_delete=models.SET(0), related_name="family_mother", db_column='MotherID', blank=True, null=True)
    child = models.ForeignKey('Person', on_delete=models.SET(0), related_name="family_child", db_column='ChildID', blank=True, null=True)
    husband_order = models.IntegerField(db_column='HusbOrder', blank=True, null=True)
    wife_order = models.IntegerField(db_column='WifeOrder', blank=True, null=True)
    is_private = models.BooleanField(db_column='IsPrivate', blank=True, null=True)
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)
    spouse_label = models.IntegerField(db_column='SpouseLabel', blank=True, null=True)
    father_label = models.IntegerField(db_column='FatherLabel', blank=True, null=True)
    mother_label = models.IntegerField(db_column='MotherLabel', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FamilyTable'
        verbose_name_plural = "Families"

    def __str__(self):
        return f"MRIN {self.id}"


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
    # 1 -- FamilySearch
    link_type = models.IntegerField(db_column='LinkType', blank=True, null=True)
    rootsmagic_id = models.IntegerField(db_column='rmID', blank=True, null=True)
    ext_id = models.TextField(db_column='extID', blank=True, null=True)
    # ID in link system
    #    e.g. "L82W-Z87" for FamilySearch
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
    # media_id = models.IntegerField(db_column='MediaID', blank=True, null=True)
    media = models.ForeignKey('Multimedia', on_delete=models.CASCADE, db_column='MediaID', blank=True, null=True)
    owner_type = models.IntegerField(db_column='OwnerType', blank=True, null=True)
    # owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    owner = models.ForeignKey('Person', on_delete=models.SET(0), db_column='OwnerID', blank=True, null=True)
    is_primary = models.BooleanField(db_column='IsPrimary', blank=True, null=True)
    # i.e. use this as "the" image for the owner?
    include_1 = models.BooleanField(db_column='Include1', blank=True, null=True)
    include_2 = models.BooleanField(db_column='Include2', blank=True, null=True)
    include_3 = models.BooleanField(db_column='Include3', blank=True, null=True)
    include_4 = models.BooleanField(db_column='Include4', blank=True, null=True)
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
    # 1 -- JPG (and other images?)
    # 2 -- PDF (and other non-images?)
    media_path = models.TextField(db_column='MediaPath', blank=True, null=True)
    # folder the file is located in
    media_file = models.TextField(db_column='MediaFile', blank=True, null=True)
    # filename
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

    def __str__(self):
        return self.media_file


class Name(models.Model):
    id = models.AutoField(db_column='NameID', primary_key=True)
    # owner_id = models.IntegerField(db_column='OwnerID', blank=True, null=True)
    owner = models.ForeignKey("Person", on_delete=models.CASCADE, db_column='OwnerID', blank=True, null=True)
    surname = models.TextField(db_column='Surname', blank=True, null=True)
    given = models.TextField(db_column='Given', blank=True, null=True)
    prefix = models.TextField(db_column='Prefix', blank=True, null=True)
    suffix = models.TextField(db_column='Suffix', blank=True, null=True)
    nickname = models.TextField(db_column='Nickname', blank=True, null=True)
    name_type = models.IntegerField(db_column='NameType', blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)
    sort_date = models.IntegerField(db_column='SortDate', blank=True, null=True)
    is_primary = models.BooleanField(db_column='IsPrimary', blank=True, null=True)
    is_private = models.BooleanField(db_column='IsPrivate', blank=True, null=True)
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
    unique_id = models.CharField(db_column='UniqueID', max_length=36, blank=True, null=True)
    # hexadecimal number, I think used to track people between files' exports
    sex = models.IntegerField(db_column='Sex', blank=True, null=True)
    # 0 -- Male; 1 -- Female
    edit_date = models.TextField(db_column='EditDate', blank=True, null=True)  # This field type is a guess.
    # parent_id = models.IntegerField(db_column='ParentID', blank=True, null=True)
    # spouse_id = models.IntegerField(db_column='SpouseID', blank=True, null=True)
    parent = models.ForeignKey('Family', on_delete=models.SET(0), related_name='parent_family', db_column='ParentID', blank=True, null=True)
    spouse = models.ForeignKey('Family', on_delete=models.SET(0), related_name='spouse_family', db_column='SpouseID', blank=True, null=True)
    color = models.IntegerField(db_column='Color', blank=True, null=True)
    relate_1 = models.IntegerField(db_column='Relate1', blank=True, null=True)
    relate_2 = models.IntegerField(db_column='Relate2', blank=True, null=True)
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)
    is_living = models.BooleanField(db_column='Living', blank=True, null=True)
    is_private = models.BooleanField(db_column='IsPrivate', blank=True, null=True)
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)
    bookmark = models.IntegerField(db_column='Bookmark', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PersonTable'
        verbose_name_plural = "People"

    def __str__(self):
        return f"RIN {self.id}"

    def primary_name(self):
        names = Name.objects.using(EXODUS_DB_NAME).filter(owner_id = self.id)
        if names.exists():
            if names.count() == 1:
                return names[0]
            else:
                names2 = names.filter(is_primary=1)
                if names2.exists():
                    return names2[0]
                else:
                    return names[0]
        else:
            return None

    def sex_str(self):
        if self.sex == 0:
            return "M"
        elif self.sex == 1:
            return "F"
        else:
            raise ValueError(self.sex)


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
    # 7 decimal places, but the decimal is not included
    # "-" included for West (and presumably South)
    longitude = models.IntegerField(db_column='Longitude', blank=True, null=True)
    exact_latituate_longitude = models.IntegerField(db_column='LatLongExact', blank=True, null=True)
    # master_id = models.IntegerField(db_column='MasterID', blank=True, null=True)
    master_place = models.ForeignKey('Place', on_delete=models.SET(0), db_column='MasterID', blank=True, null=True)
    # when set, is the "master" place (place_type 0) for a place_type 2
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaceTable'

    def __str__(self):
        return self.name

    def pretty_latlong(self):
        def _decimal_to_dms_str(latitude):
            latitude = abs(latitude)
            degrees = int(latitude)
            minutes = int((latitude-degrees)*60)
            if minutes == 60:
                degrees += 1
                minutes = 0
            seconds = round((((latitude-degrees)*60)-minutes)*60, LAT_LONG_SECOND_DECIMAL_PLACES)
            if seconds == 60:
                minutes += 1
                seconds = 0
            if seconds == int(seconds):
                seconds = int(seconds)

            # TODO: Use non breaking spaces here
            lat_str = f"{degrees}°"
            if minutes or seconds:
                lat_str += f" {minutes}'"
            if seconds:
                lat_str += f' {seconds}"'
            return lat_str


        if self.latitude and self.longitude:
            lat_str = _decimal_to_dms_str(self.latitude/1e7)
            lat_str += " N" if self.latitude >= 0 else " S"

            long_str = _decimal_to_dms_str(self.longitude/1e7)
            long_str += " E" if self.longitude >= 0 else " W"

            return f"{lat_str} {long_str}"
        else:
            return None


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
    # event_type = models.IntegerField(db_column='EventType', blank=True, null=True)
    event_type = models.ForeignKey('FactType', on_delete=models.PROTECT, db_column='EventType', blank=True, null=True)
    role_type = models.IntegerField(db_column='RoleType', blank=True, null=True)
    sentence = models.TextField(db_column='Sentence', blank=True, null=True)
    # useful to create a "story" for the facts

    class Meta:
        managed = False
        db_table = 'RoleTable'

    def __str__(self):
        return f"{self.role_name} for {self.event_type}"


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
    # no such collation sequence: RMNOCASE
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
    # owner id is not a person?
    link_type = models.IntegerField(db_column='LinkType', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)
    note = models.BinaryField(db_column='Note', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'URLTable'


class Witness(models.Model):
    id = models.AutoField(db_column='WitnessID', primary_key=True)
    # event_id = models.IntegerField(db_column='EventID', blank=True, null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, db_column='EventID', blank=True, null=True)
    # person_id = models.IntegerField(db_column='PersonID', blank=True, null=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, db_column='PersonID', blank=True, null=True)
    witness_order = models.IntegerField(db_column='WitnessOrder', blank=True, null=True)
    # role = models.IntegerField(db_column='Role', blank=True, null=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, db_column='Role', blank=True, null=True)
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
