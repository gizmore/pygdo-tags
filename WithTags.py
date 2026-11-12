from gdo.base.Exceptions import GDOMethodException
from gdo.tags.GDO_Tag import GDO_Tag
from gdo.tags.GDT_Tags import GDT_Tags


class WithTags:

    def gdo_tags_table(self) -> GDO_Tag:
        raise GDOMethodException('tags', 'gdo_tags_table')

    def get_tags(self) -> list[GDO_Tag]:
        if not self.is_persisted():
            raise ValueError('Tagged object must be persisted')
        links = self.gdo_tag_links_table()
        tags = self.gdo_tags_table()
        rows = links.select().where(f'obj_id={links.quote(self.get_id())}').exec().fetch_all()
        return [tag for row in rows if (tag := tags.get_by_id(row.gdo_val('tag_id')))]

    def gdo_tag_links_table(self):
        raise GDOMethodException('tags', 'gdo_tag_links_table')

    def add_tag(self, name, allow_creation=False):
        if not self.is_persisted():
            raise ValueError('Tagged object must be persisted')
        if len(GDT_Tags.parse_names(name)) != 1 or ',' in name:
            raise ValueError('Expected exactly one tag')
        field = GDT_Tags('tags').table(self.gdo_tags_table()).allow_creation(allow_creation).val(name)
        tags = field.resolve_tags()
        if len(tags) != 1:
            raise ValueError('Expected exactly one tag')
        tag = tags[0]
        links = self.gdo_tag_links_table()
        values = {'tag_id': tag.get_id(), 'obj_id': self.get_id()}
        if not links.get_by_vals(values):
            links.blank(values).insert()
        return tag

    def remove_tag(self, name):
        if not self.is_persisted():
            raise ValueError('Tagged object must be persisted')
        names = GDT_Tags.parse_names(name)
        if len(names) != 1:
            raise ValueError('Expected exactly one tag')
        tag = self.gdo_tags_table().get_by_vals({'tag_name': names[0]})
        if not tag:
            return False
        links = self.gdo_tag_links_table()
        link = links.get_by_vals({'tag_id': tag.get_id(), 'obj_id': self.get_id()})
        if not link:
            return False
        link.delete()
        return True
