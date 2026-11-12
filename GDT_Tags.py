import re

from gdo.core.GDT_String import GDT_String


class GDT_Tags(GDT_String):
    def __init__(self, name=None):
        super().__init__(name)
        self._tag_table = None
        self._allow_creation = False

    def table(self, table):
        self._tag_table = table
        return self

    def allow_creation(self, allow=True):
        self._allow_creation = bool(allow)
        return self

    @staticmethod
    def parse_names(value):
        names = []
        seen = set()
        for item in (value or '').split(','):
            name = item.strip()
            if not name:
                continue
            if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{1,63}', name):
                raise ValueError('Invalid tag name')
            if name.lower() not in seen:
                seen.add(name.lower())
                names.append(name)
        return names

    def resolve_tags(self):
        if self._tag_table is None:
            raise ValueError('Tag table is not configured')
        result = []
        for name in self.parse_names(self.get_val()):
            tag = self._tag_table.get_by_vals({'tag_name': name})
            if not tag:
                if not self._allow_creation:
                    raise ValueError(f'Unknown tag: {name}')
                tag = self._tag_table.blank({'tag_name': name}).insert()
            result.append(tag)
        return result
