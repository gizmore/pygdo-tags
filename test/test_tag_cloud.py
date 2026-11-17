import unittest

from gdo.tags.GDT_TagCloud import GDT_TagCloud


class TagCloudTest(unittest.TestCase):
    def test_weight_selection_and_escaping(self):
        cloud = GDT_TagCloud().entries(
            [(1, '<script>', 1), (2, 'Crypto', 3)],
            lambda key: '/challenges?tag=' + key + '&x="', selected=2,
            clear_href='/challenges', clear_label='All')
        html = cloud.render_html()
        self.assertIn('&lt;script&gt; (1)', html)
        self.assertIn('tag=2&amp;x=&quot;', html)
        self.assertIn('aria-current="true"', html)
        self.assertIn('font-size:140%', html)
        self.assertNotIn('<script>', html)

    def test_empty_cloud(self):
        self.assertEqual('', GDT_TagCloud().entries([], lambda key: key).render_html())


if __name__ == '__main__':
    unittest.main()
