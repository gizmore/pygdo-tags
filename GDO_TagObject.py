from gdo.base.Exceptions import GDOMethodException
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Object import GDT_Object
from gdo.date.GDT_Created import GDT_Created


class GDO_TagObject(GDO):

    def gdo_tags_table(self) -> GDO:
        raise GDOMethodException('tags', 'gdo_tags_table')

    def gdo_tag_object_table(self) -> GDO:
        raise GDOMethodException('tags', 'gdo_tag_object_table')

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Object('tag_id').table(self.gdo_tags_table()),
            GDT_Object('obj_id').table(self.gdo_tag_object_table()),
            GDT_Created('tag_created'),
            GDT_Creator('tag_creator'),
        ]
