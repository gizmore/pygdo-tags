from gdo.base.Exceptions import GDOMethodException
from gdo.tags.GDO_Tag import GDO_Tag


class WithTags:

    def gdo_tags_table(self) -> GDO_Tag:
        raise GDOMethodException('tags', 'gdo_tags_table')

    def get_tags(self) -> list[GDO_Tag]:
        return []
    