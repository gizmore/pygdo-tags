from gdo.base.GDO import GDO
from gdo.base.GDT import GDT


class GDO_Tags(GDO):

    def gdo_tagged_object_table(self) -> GDO:
        raise GDOE

    def gdo_columns(self) -> list[GDT]:
        return [

        ]
