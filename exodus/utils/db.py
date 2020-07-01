from ..import EXODUS_DB_NAME

class ExodusRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    # django-docs/topics/db/multi-db.html
    route_app_labels = ('exodus', )

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return EXODUS_DB_NAME
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        # TODO: writing should fail to this database, but with
        #       "managed=False", maybe that is already happening
        if model._meta.app_label in self.route_app_labels:
            return EXODUS_DB_NAME
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        # TODO: writing should fail to this database, but with
        #       "managed=False", maybe that is already happening
        if app_label in self.route_app_labels:
            return db == EXODUS_DB_NAME
        return None
