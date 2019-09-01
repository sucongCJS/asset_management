import xadmin

from apps.departments.models import Department, Building, Room


class DepartmentAdmin(object):
    list_display = ["name"]


class BuildingAdmin(object):
    list_display = ["name", "campus", "desc"]
    search_fields = ["name"]
    list_filter = ["campus"]  # add_time
    list_editable = ["desc"]


class RoomAdmin(object):
    list_display = ["name", "building", "department", "desc"]


xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Building, BuildingAdmin)
xadmin.site.register(Room, RoomAdmin)
