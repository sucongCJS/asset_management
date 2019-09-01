import xadmin

from apps.assets.models import Asset


class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "信息化管理办公室"
    # menu_style = "accordion"


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class AssetAdmin(object):
    pass


xadmin.site.register(Asset, AssetAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
