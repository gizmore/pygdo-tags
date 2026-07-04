from gdo.base.Exceptions import GDOError
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Name import GDT_Name
from gdo.date.GDT_Created import GDT_Created


class GDO_Tag(GDO):

    def gdo_tag_object_table(self) -> GDO:
        raise GDOError("gdo_tagged_object_table: Not implemented for "+self.fqcn())

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('tag_id'),
            GDT_Name('tag_name'),
            GDT_Created('tag_created'),
            GDT_Creator('tag_creator'),
        ]
