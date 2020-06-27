# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresslinktable(models.Model):
    linkid = models.AutoField(db_column='LinkID', primary_key=True)  # Field name made lowercase.
    ownertype = models.IntegerField(db_column='OwnerType', blank=True, null=True)  # Field name made lowercase.
    addressid = models.IntegerField(db_column='AddressID', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    addressnum = models.IntegerField(db_column='AddressNum', blank=True, null=True)  # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AddressLinkTable'


class Addresstable(models.Model):
    addressid = models.AutoField(db_column='AddressID', primary_key=True)  # Field name made lowercase.
    addresstype = models.IntegerField(db_column='AddressType', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    street1 = models.TextField(db_column='Street1', blank=True, null=True)  # Field name made lowercase.
    street2 = models.TextField(db_column='Street2', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    phone1 = models.TextField(db_column='Phone1', blank=True, null=True)  # Field name made lowercase.
    phone2 = models.TextField(db_column='Phone2', blank=True, null=True)  # Field name made lowercase.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    latitude = models.IntegerField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.IntegerField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AddressTable'


class Childtable(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    childid = models.IntegerField(db_column='ChildID', blank=True, null=True)  # Field name made lowercase.
    familyid = models.IntegerField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
    relfather = models.IntegerField(db_column='RelFather', blank=True, null=True)  # Field name made lowercase.
    relmother = models.IntegerField(db_column='RelMother', blank=True, null=True)  # Field name made lowercase.
    childorder = models.IntegerField(db_column='ChildOrder', blank=True, null=True)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate', blank=True, null=True)  # Field name made lowercase.
    prooffather = models.IntegerField(db_column='ProofFather', blank=True, null=True)  # Field name made lowercase.
    proofmother = models.IntegerField(db_column='ProofMother', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChildTable'


class Citationtable(models.Model):
    citationid = models.AutoField(db_column='CitationID', primary_key=True)  # Field name made lowercase.
    ownertype = models.IntegerField(db_column='OwnerType', blank=True, null=True)  # Field name made lowercase.
    sourceid = models.IntegerField(db_column='SourceID', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    quality = models.TextField(db_column='Quality', blank=True, null=True)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate', blank=True, null=True)  # Field name made lowercase.
    comments = models.BinaryField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    actualtext = models.BinaryField(db_column='ActualText', blank=True, null=True)  # Field name made lowercase.
    refnumber = models.TextField(db_column='RefNumber', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.
    fields = models.BinaryField(db_column='Fields', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CitationTable'


class Configtable(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    rectype = models.IntegerField(db_column='RecType', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    datarec = models.BinaryField(db_column='DataRec', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfigTable'


class Eventtable(models.Model):
    eventid = models.AutoField(db_column='EventID', primary_key=True)  # Field name made lowercase.
    eventtype = models.IntegerField(db_column='EventType', blank=True, null=True)  # Field name made lowercase.
    ownertype = models.IntegerField(db_column='OwnerType', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    familyid = models.IntegerField(db_column='FamilyID', blank=True, null=True)  # Field name made lowercase.
    placeid = models.IntegerField(db_column='PlaceID', blank=True, null=True)  # Field name made lowercase.
    siteid = models.IntegerField(db_column='SiteID', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    sortdate = models.IntegerField(db_column='SortDate', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate', blank=True, null=True)  # Field name made lowercase.
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    editdate = models.TextField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sentence = models.BinaryField(db_column='Sentence', blank=True, null=True)  # Field name made lowercase.
    details = models.BinaryField(db_column='Details', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventTable'


class Exclusiontable(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    exclusiontype = models.IntegerField(db_column='ExclusionType', blank=True, null=True)  # Field name made lowercase.
    id1 = models.IntegerField(db_column='ID1', blank=True, null=True)  # Field name made lowercase.
    id2 = models.IntegerField(db_column='ID2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExclusionTable'
        unique_together = (('exclusiontype', 'id1', 'id2'),)


class Facttypetable(models.Model):
    facttypeid = models.AutoField(db_column='FactTypeID', primary_key=True)  # Field name made lowercase.
    ownertype = models.IntegerField(db_column='OwnerType', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    abbrev = models.TextField(db_column='Abbrev', blank=True, null=True)  # Field name made lowercase.
    gedcomtag = models.TextField(db_column='GedcomTag', blank=True, null=True)  # Field name made lowercase.
    usevalue = models.IntegerField(db_column='UseValue', blank=True, null=True)  # Field name made lowercase.
    usedate = models.IntegerField(db_column='UseDate', blank=True, null=True)  # Field name made lowercase.
    useplace = models.IntegerField(db_column='UsePlace', blank=True, null=True)  # Field name made lowercase.
    sentence = models.BinaryField(db_column='Sentence', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactTypeTable'


class Familytable(models.Model):
    familyid = models.AutoField(db_column='FamilyID', primary_key=True)  # Field name made lowercase.
    fatherid = models.IntegerField(db_column='FatherID', blank=True, null=True)  # Field name made lowercase.
    motherid = models.IntegerField(db_column='MotherID', blank=True, null=True)  # Field name made lowercase.
    childid = models.IntegerField(db_column='ChildID', blank=True, null=True)  # Field name made lowercase.
    husborder = models.IntegerField(db_column='HusbOrder', blank=True, null=True)  # Field name made lowercase.
    wifeorder = models.IntegerField(db_column='WifeOrder', blank=True, null=True)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate', blank=True, null=True)  # Field name made lowercase.
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)  # Field name made lowercase.
    spouselabel = models.IntegerField(db_column='SpouseLabel', blank=True, null=True)  # Field name made lowercase.
    fatherlabel = models.IntegerField(db_column='FatherLabel', blank=True, null=True)  # Field name made lowercase.
    motherlabel = models.IntegerField(db_column='MotherLabel', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FamilyTable'


class Grouptable(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    startid = models.IntegerField(db_column='StartID', blank=True, null=True)  # Field name made lowercase.
    endid = models.IntegerField(db_column='EndID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupTable'


class Labeltable(models.Model):
    labelid = models.AutoField(db_column='LabelID', primary_key=True)  # Field name made lowercase.
    labeltype = models.IntegerField(db_column='LabelType', blank=True, null=True)  # Field name made lowercase.
    labelvalue = models.IntegerField(db_column='LabelValue', blank=True, null=True)  # Field name made lowercase.
    labelname = models.TextField(db_column='LabelName', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabelTable'


class Linkancestrytable(models.Model):
    linkid = models.AutoField(db_column='LinkID', primary_key=True)  # Field name made lowercase.
    extsystem = models.IntegerField(db_column='extSystem', blank=True, null=True)  # Field name made lowercase.
    linktype = models.IntegerField(db_column='LinkType', blank=True, null=True)  # Field name made lowercase.
    rmid = models.IntegerField(db_column='rmID', blank=True, null=True)  # Field name made lowercase.
    extid = models.TextField(db_column='extID', blank=True, null=True)  # Field name made lowercase.
    modified = models.IntegerField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    extversion = models.TextField(db_column='extVersion', blank=True, null=True)  # Field name made lowercase.
    extdate = models.TextField(db_column='extDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LinkAncestryTable'


class Linktable(models.Model):
    linkid = models.AutoField(db_column='LinkID', primary_key=True)  # Field name made lowercase.
    extsystem = models.IntegerField(db_column='extSystem', blank=True, null=True)  # Field name made lowercase.
    linktype = models.IntegerField(db_column='LinkType', blank=True, null=True)  # Field name made lowercase.
    rmid = models.IntegerField(db_column='rmID', blank=True, null=True)  # Field name made lowercase.
    extid = models.TextField(db_column='extID', blank=True, null=True)  # Field name made lowercase.
    modified = models.IntegerField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    extversion = models.TextField(db_column='extVersion', blank=True, null=True)  # Field name made lowercase.
    extdate = models.TextField(db_column='extDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LinkTable'


class Medialinktable(models.Model):
    linkid = models.AutoField(db_column='LinkID', primary_key=True)  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaID', blank=True, null=True)  # Field name made lowercase.
    ownertype = models.IntegerField(db_column='OwnerType', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase.
    include1 = models.IntegerField(db_column='Include1', blank=True, null=True)  # Field name made lowercase.
    include2 = models.IntegerField(db_column='Include2', blank=True, null=True)  # Field name made lowercase.
    include3 = models.IntegerField(db_column='Include3', blank=True, null=True)  # Field name made lowercase.
    include4 = models.IntegerField(db_column='Include4', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder', blank=True, null=True)  # Field name made lowercase.
    rectleft = models.IntegerField(db_column='RectLeft', blank=True, null=True)  # Field name made lowercase.
    recttop = models.IntegerField(db_column='RectTop', blank=True, null=True)  # Field name made lowercase.
    rectright = models.IntegerField(db_column='RectRight', blank=True, null=True)  # Field name made lowercase.
    rectbottom = models.IntegerField(db_column='RectBottom', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    caption = models.TextField(db_column='Caption', blank=True, null=True)  # Field name made lowercase.
    refnumber = models.TextField(db_column='RefNumber', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    sortdate = models.IntegerField(db_column='SortDate', blank=True, null=True)  # Field name made lowercase.
    description = models.BinaryField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MediaLinkTable'


class Multimediatable(models.Model):
    mediaid = models.AutoField(db_column='MediaID', primary_key=True)  # Field name made lowercase.
    mediatype = models.IntegerField(db_column='MediaType', blank=True, null=True)  # Field name made lowercase.
    mediapath = models.TextField(db_column='MediaPath', blank=True, null=True)  # Field name made lowercase.
    mediafile = models.TextField(db_column='MediaFile', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    thumbnail = models.BinaryField(db_column='Thumbnail', blank=True, null=True)  # Field name made lowercase.
    caption = models.TextField(db_column='Caption', blank=True, null=True)  # Field name made lowercase.
    refnumber = models.TextField(db_column='RefNumber', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    sortdate = models.IntegerField(db_column='SortDate', blank=True, null=True)  # Field name made lowercase.
    description = models.BinaryField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MultimediaTable'


class Nametable(models.Model):
    nameid = models.AutoField(db_column='NameID', primary_key=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    surname = models.TextField(db_column='Surname', blank=True, null=True)  # Field name made lowercase.
    given = models.TextField(db_column='Given', blank=True, null=True)  # Field name made lowercase.
    prefix = models.TextField(db_column='Prefix', blank=True, null=True)  # Field name made lowercase.
    suffix = models.TextField(db_column='Suffix', blank=True, null=True)  # Field name made lowercase.
    nickname = models.TextField(db_column='Nickname', blank=True, null=True)  # Field name made lowercase.
    nametype = models.IntegerField(db_column='NameType', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    sortdate = models.IntegerField(db_column='SortDate', blank=True, null=True)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate', blank=True, null=True)  # Field name made lowercase.
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)  # Field name made lowercase.
    editdate = models.TextField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sentence = models.BinaryField(db_column='Sentence', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    birthyear = models.IntegerField(db_column='BirthYear', blank=True, null=True)  # Field name made lowercase.
    deathyear = models.IntegerField(db_column='DeathYear', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NameTable'


class Persontable(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    uniqueid = models.TextField(db_column='UniqueID', blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='Sex', blank=True, null=True)  # Field name made lowercase.
    editdate = models.TextField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    spouseid = models.IntegerField(db_column='SpouseID', blank=True, null=True)  # Field name made lowercase.
    color = models.IntegerField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    relate1 = models.IntegerField(db_column='Relate1', blank=True, null=True)  # Field name made lowercase.
    relate2 = models.IntegerField(db_column='Relate2', blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='Flags', blank=True, null=True)  # Field name made lowercase.
    living = models.IntegerField(db_column='Living', blank=True, null=True)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate', blank=True, null=True)  # Field name made lowercase.
    proof = models.IntegerField(db_column='Proof', blank=True, null=True)  # Field name made lowercase.
    bookmark = models.IntegerField(db_column='Bookmark', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonTable'


class Placetable(models.Model):
    placeid = models.AutoField(db_column='PlaceID', primary_key=True)  # Field name made lowercase.
    placetype = models.IntegerField(db_column='PlaceType', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    abbrev = models.TextField(db_column='Abbrev', blank=True, null=True)  # Field name made lowercase.
    normalized = models.TextField(db_column='Normalized', blank=True, null=True)  # Field name made lowercase.
    latitude = models.IntegerField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.IntegerField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.
    latlongexact = models.IntegerField(db_column='LatLongExact', blank=True, null=True)  # Field name made lowercase.
    masterid = models.IntegerField(db_column='MasterID', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlaceTable'


class Researchitemtable(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    logid = models.IntegerField(db_column='LogID', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    sortdate = models.IntegerField(db_column='SortDate', blank=True, null=True)  # Field name made lowercase.
    refnumber = models.TextField(db_column='RefNumber', blank=True, null=True)  # Field name made lowercase.
    repository = models.TextField(db_column='Repository', blank=True, null=True)  # Field name made lowercase.
    goal = models.TextField(db_column='Goal', blank=True, null=True)  # Field name made lowercase.
    source = models.TextField(db_column='Source', blank=True, null=True)  # Field name made lowercase.
    result = models.TextField(db_column='Result', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResearchItemTable'


class Researchtable(models.Model):
    taskid = models.AutoField(db_column='TaskID', primary_key=True)  # Field name made lowercase.
    tasktype = models.IntegerField(db_column='TaskType', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    ownertype = models.IntegerField(db_column='OwnerType', blank=True, null=True)  # Field name made lowercase.
    refnumber = models.TextField(db_column='RefNumber', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    date1 = models.TextField(db_column='Date1', blank=True, null=True)  # Field name made lowercase.
    date2 = models.TextField(db_column='Date2', blank=True, null=True)  # Field name made lowercase.
    date3 = models.TextField(db_column='Date3', blank=True, null=True)  # Field name made lowercase.
    sortdate1 = models.IntegerField(db_column='SortDate1', blank=True, null=True)  # Field name made lowercase.
    sortdate2 = models.IntegerField(db_column='SortDate2', blank=True, null=True)  # Field name made lowercase.
    sortdate3 = models.IntegerField(db_column='SortDate3', blank=True, null=True)  # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    details = models.BinaryField(db_column='Details', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResearchTable'


class Roletable(models.Model):
    roleid = models.AutoField(db_column='RoleID', primary_key=True)  # Field name made lowercase.
    rolename = models.TextField(db_column='RoleName', blank=True, null=True)  # Field name made lowercase.
    eventtype = models.IntegerField(db_column='EventType', blank=True, null=True)  # Field name made lowercase.
    roletype = models.IntegerField(db_column='RoleType', blank=True, null=True)  # Field name made lowercase.
    sentence = models.TextField(db_column='Sentence', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoleTable'


class Sourcetable(models.Model):
    sourceid = models.AutoField(db_column='SourceID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    refnumber = models.TextField(db_column='RefNumber', blank=True, null=True)  # Field name made lowercase.
    actualtext = models.TextField(db_column='ActualText', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    isprivate = models.IntegerField(db_column='IsPrivate', blank=True, null=True)  # Field name made lowercase.
    templateid = models.IntegerField(db_column='TemplateID', blank=True, null=True)  # Field name made lowercase.
    fields = models.BinaryField(db_column='Fields', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SourceTable'


class Sourcetemplatetable(models.Model):
    templateid = models.AutoField(db_column='TemplateID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    favorite = models.IntegerField(db_column='Favorite', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    footnote = models.TextField(db_column='Footnote', blank=True, null=True)  # Field name made lowercase.
    shortfootnote = models.TextField(db_column='ShortFootnote', blank=True, null=True)  # Field name made lowercase.
    bibliography = models.TextField(db_column='Bibliography', blank=True, null=True)  # Field name made lowercase.
    fielddefs = models.BinaryField(db_column='FieldDefs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SourceTemplateTable'


class Urltable(models.Model):
    linkid = models.AutoField(db_column='LinkID', primary_key=True)  # Field name made lowercase.
    ownertype = models.IntegerField(db_column='OwnerType', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    linktype = models.IntegerField(db_column='LinkType', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'URLTable'


class Witnesstable(models.Model):
    witnessid = models.AutoField(db_column='WitnessID', primary_key=True)  # Field name made lowercase.
    eventid = models.IntegerField(db_column='EventID', blank=True, null=True)  # Field name made lowercase.
    personid = models.IntegerField(db_column='PersonID', blank=True, null=True)  # Field name made lowercase.
    witnessorder = models.IntegerField(db_column='WitnessOrder', blank=True, null=True)  # Field name made lowercase.
    role = models.IntegerField(db_column='Role', blank=True, null=True)  # Field name made lowercase.
    sentence = models.TextField(db_column='Sentence', blank=True, null=True)  # Field name made lowercase.
    note = models.BinaryField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    given = models.TextField(db_column='Given', blank=True, null=True)  # Field name made lowercase.
    surname = models.TextField(db_column='Surname', blank=True, null=True)  # Field name made lowercase.
    prefix = models.TextField(db_column='Prefix', blank=True, null=True)  # Field name made lowercase.
    suffix = models.TextField(db_column='Suffix', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WitnessTable'
