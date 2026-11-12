import unittest
from unittest.mock import MagicMock

from gdo.tags.GDT_Tags import GDT_Tags
from gdo.tags.WithTags import WithTags


class TagsTest(unittest.TestCase):
    def test_parse_names_validates_and_deduplicates(self):
        self.assertEqual(['crypto', 'Web'], GDT_Tags.parse_names(' crypto, Web, CRYPTO '))
        for invalid in ('a', 'bad tag', 'x' * 65):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                GDT_Tags.parse_names(invalid)

    def test_creation_is_opt_in(self):
        table = MagicMock()
        table.get_by_vals.return_value = None
        field = GDT_Tags('tags').table(table).val('new-tag')
        with self.assertRaises(ValueError):
            field.resolve_tags()
        table.blank.assert_not_called()
        self.assertEqual([table.blank.return_value.insert.return_value],
                         field.allow_creation().resolve_tags())
        table.blank.assert_called_once_with({'tag_name': 'new-tag'})

    def test_existing_tag_is_reused_without_creation(self):
        table = MagicMock()
        tag = table.get_by_vals.return_value
        self.assertEqual([tag], GDT_Tags('tags').table(table).val('known').resolve_tags())
        table.blank.assert_not_called()

    def test_creation_can_be_disabled_again(self):
        table = MagicMock()
        table.get_by_vals.return_value = None
        field = GDT_Tags('tags').table(table).allow_creation().allow_creation(False).val('unknown')
        with self.assertRaises(ValueError):
            field.resolve_tags()
        table.blank.assert_not_called()

    def test_assignment_is_idempotent_and_remove_keeps_tag(self):
        obj = MagicMock()
        obj.is_persisted.return_value = True
        obj.get_id.return_value = '7'
        tag, links, table = MagicMock(), MagicMock(), MagicMock()
        tag.get_id.return_value = '3'
        table.get_by_vals.return_value = tag
        obj.gdo_tags_table.return_value = table
        obj.gdo_tag_links_table.return_value = links
        links.get_by_vals.return_value = None
        WithTags.add_tag(obj, 'crypto')
        links.blank.assert_called_once_with({'tag_id': '3', 'obj_id': '7'})
        links.reset_mock()
        link = links.get_by_vals.return_value = MagicMock()
        WithTags.add_tag(obj, 'crypto')
        links.blank.assert_not_called()
        self.assertTrue(WithTags.remove_tag(obj, 'crypto'))
        link.delete.assert_called_once()
        tag.delete.assert_not_called()

    def test_multiple_names_cannot_create_tags_via_add_tag(self):
        obj = MagicMock()
        obj.is_persisted.return_value = True
        with self.assertRaises(ValueError):
            WithTags.add_tag(obj, 'one,two', allow_creation=True)
        obj.gdo_tags_table.assert_not_called()
