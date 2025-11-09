# relationship_app/signals.py
# This file ensures signals are loaded when the app starts
from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        import relationship_app.models  # noqa