from gdo.base.Exceptions import GDOError
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name


class GDO_TagsTable(GDO):

    def gdo_tagged_object_table(self) -> GDO:
        raise GDOError("gdo_tagged_object_table: Not implemented for "+self.fqcn())

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('tag_id'),
            GDT_Name('tag_name'),
        ]
