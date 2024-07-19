class TailingsRouter:
    """
    A router to control all database operations on models in the
    db2 application.
    """
    def db_for_read(self, model, **hints):
        """Point all read operations to db2."""
        if model._meta.app_label == 'dam_monitor':
            return 'tailings'
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to db2."""
        if model._meta.app_label == 'dam_monitor':
            return 'tailings'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow any relation if a model in db2 is involved."""
        if obj1._meta.app_label == 'dam_monitor' or obj2._meta.app_label == 'dam_monitor':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the app2's models get created on the right database."""
        if app_label == 'dam_monitor':
            return db == 'tailings'
        return None