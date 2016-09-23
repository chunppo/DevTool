"""
Mutiple Database Router
"""
from django.conf import settings

class DatabaseAppsRouter(object):
    def db_for_read(self, model, **hints):
        """Point all read operations to the specific database."""
        print 'A'
        return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label)

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        print 'B'
        return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation between apps that use the same database."""
        print 'C'
        db_obj1 = settings.DATABASE_APPS_MAPPING.get(obj1._meta.app_label)
        db_obj2 = settings.DATABASE_APPS_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """Make sure that apps only appear in the related database."""
        fla = settings.DATABASE_APPS_MAPPING.get(app_label, 'default') == db
        print db + ' | ' + app_label + ' | ' + str(hints.get('model')) + ' | ' + str(fla)
        return settings.DATABASE_APPS_MAPPING.get(app_label, 'default') == db
