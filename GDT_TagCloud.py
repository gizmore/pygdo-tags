from html import escape

from gdo.message.GDT_HTML import GDT_HTML


class GDT_TagCloud(GDT_HTML):
    """A reusable, accessible cloud of (id, name, usage count) links."""

    def entries(self, rows, href_for, selected=None, clear_href=None, clear_label='All'):
        rows = [(str(key), str(name), int(count)) for key, name, count in rows if int(count) > 0]
        if not rows:
            return self.html('')
        maximum = max(count for _, _, count in rows)
        links = []
        if clear_href is not None:
            current = ' aria-current="true"' if selected is None else ''
            links.append(f'<a href="{escape(clear_href, quote=True)}"{current}>{escape(clear_label)}</a>')
        for key, name, count in rows:
            size = 80 + round(60 * count / maximum)
            current = ' aria-current="true"' if str(selected) == key else ''
            links.append(f'<a href="{escape(href_for(key), quote=True)}"{current} '
                         f'style="font-size:{size}%">{escape(name)} ({count})</a>')
        return self.html('<nav class="gdt-tag-cloud" aria-label="Tags">' + ' · '.join(links) + '</nav>')
