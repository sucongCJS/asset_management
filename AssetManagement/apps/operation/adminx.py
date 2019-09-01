import xadmin

from apps.operation.models import Change, AssetManager


class ChangeAdmin(object):
    list_display = ["summit_user"]


class AssetManagerAdmin(object):
    list_display = ["manager"]


xadmin.site.register(Change, ChangeAdmin)
xadmin.site.register(AssetManager, AssetManagerAdmin)
