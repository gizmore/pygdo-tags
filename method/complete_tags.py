from gdo.core.MethodCompletion import MethodCompletion
from gdo.tags.GDO_Tag import GDO_Tag


class complete_tags(MethodCompletion):

    def gdo_completion_items(self) -> list[dict[str, str]]:
        query = self.get_query()
        tags = GDO_Tag.table().select().where(
            f"tag_name LIKE '%{GDO_Tag.escape(query)}%'"
        ).order('tag_name ASC').limit(16).exec().fetch_all()
        return [
            {
                'id': tag.get_id(),
                'var': tag.gdo_val('tag_name'),
                'display_var': tag.render_name(),
            }
            for tag in tags
        ]
